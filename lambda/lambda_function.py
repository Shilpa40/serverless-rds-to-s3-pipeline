import json
import boto3
import pymysql
import csv
import os
from datetime import datetime
from io import StringIO

# AWS clients
secrets_client = boto3.client("secretsmanager")
ssm_client = boto3.client("ssm")
s3_client = boto3.client("s3")

# Environment variables
SECRET_NAME = os.environ["SECRET_NAME"]
S3_BUCKET = os.environ["S3_BUCKET"]
S3_PREFIX = os.environ.get("S3_PREFIX", "")

# SSM parameter name
SSM_PARAM_NAME = "/rds-export/last-success-ts"


def get_last_export_ts():
    """Fetch last successful export timestamp from SSM"""
    response = ssm_client.get_parameter(Name=SSM_PARAM_NAME)
    return response["Parameter"]["Value"]


def update_last_export_ts(timestamp):
    """Update last successful export timestamp in SSM"""
    ssm_client.put_parameter(
        Name=SSM_PARAM_NAME,
        Value=timestamp,
        Type="String",
        Overwrite=True
    )


def lambda_handler(event, context):
    # 1️⃣ Read DB credentials
    secret = secrets_client.get_secret_value(SecretId=SECRET_NAME)
    creds = json.loads(secret["SecretString"])

    # 2️⃣ Connect to RDS MySQL
    connection = pymysql.connect(
        host=creds["host"],
        user=creds["username"],
        password=creds["password"],
        database=creds["dbname"],
        port=creds["port"],
        cursorclass=pymysql.cursors.DictCursor,
        connect_timeout=5
    )

    # 3️⃣ Read last export timestamp
    last_export_ts = get_last_export_ts()

    # 4️⃣ Query incremental data
    query = """
        SELECT id, name, updated_at
        FROM employees
        WHERE updated_at > %s
        ORDER BY updated_at ASC
    """

    with connection.cursor() as cursor:
        cursor.execute(query, (last_export_ts,))
        rows = cursor.fetchall()

    if not rows:
        print("No new or updated rows found.")
        return {
            "status": "NO_DATA",
            "exported_rows": 0
        }

    # 5️⃣ Write CSV in-memory
    csv_buffer = StringIO()
    fieldnames = rows[0].keys()
    writer = csv.DictWriter(csv_buffer, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

    # 6️⃣ Upload CSV to S3
    timestamp_str = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    s3_key = f"{S3_PREFIX}employees_{timestamp_str}.csv"

    s3_client.put_object(
        Bucket=S3_BUCKET,
        Key=s3_key,
        Body=csv_buffer.getvalue()
    )

    # 7️⃣ Update last successful export timestamp
    latest_ts = max(row["updated_at"] for row in rows)
    update_last_export_ts(str(latest_ts))

    return {
        "status": "SUCCESS",
        "exported_rows": len(rows),
        "s3_key": s3_key
    }
