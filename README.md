🚀 Capstone Project: Serverless RDS to S3 Data Export Pipeline
📌 Project Overview

This project implements a serverless, scheduled data ingestion pipeline that extracts data from an Amazon RDS database and exports it as CSV files into Amazon S3 using modern AWS-native services.

The solution replaces legacy approaches such as EC2 cron jobs or AWS Data Pipeline with a **modern, secure, and cost-efficient serverless architecture** using AWS native services.

---

## ⭐ Key Points

- AWS Lambda runs inside the same VPC as Amazon RDS for secure, private connectivity  
- Database credentials are retrieved securely from AWS Secrets Manager  
- Output files are generated as timestamped CSV files and stored in Amazon S3  

---

## 🧩 Problem Statement

Traditional RDS data exports often rely on:
- Long-running EC2 instances
- Deprecated AWS Data Pipeline
- Hard-coded credentials
- High operational and maintenance overhead

These approaches increase cost, security risk, and operational complexity.

---

## 🛠️ Technologies Used

- AWS Lambda – Serverless compute for data extraction
- Amazon EventBridge – Time-based scheduling
- Amazon RDS – Source database (MySQL / PostgreSQL)
- Amazon S3 – CSV storage
- AWS Secrets Manager – Secure credential storage
- Amazon CloudWatch – Logs and monitoring
- IAM, VPC, Security Groups

---

## 🔐 Security Design

- Database credentials stored in AWS Secrets Manager
- IAM roles follow the principle of least privilege
- Lambda runs inside a private VPC
- RDS is not publicly accessible
- No secrets are hard-coded in the source code

---

## 📄 Data Flow

1. EventBridge triggers the Lambda function based on schedule
2. Lambda retrieves credentials from Secrets Manager
3. Lambda connects to RDS inside the VPC
4. SQL query runs on the target table
5. Result set is converted into CSV format
6. CSV file is uploaded to Amazon S3 with a timestamped name
7. Logs are written to CloudWatch

---

## 📦 Repository Structure

serverless-rds-to-s3-pipeline/
├── README.md
├── lambda/
│ ├── lambda_function.py
│ └── requirements.txt
├── docs/
│ └── architecture.md
└── .gitignore

---

## 📤 Sample Output

s3://my-rds-export-bucket/rds_exports/
├── employees_20260222_101200.csv
├── employees_20260222_221200.csv

---

## 💰 Cost Analysis

| Service | Cost Impact |
|---------|-------------|
| EventBridge | ~$1 per million events |
| Lambda | Pay per execution (milliseconds) |
| S3 | Pennies for small CSV files |
| CloudWatch Logs | Negligible |
| RDS | Existing hourly cost |

**Total cost:** Effectively near zero for low-frequency schedules

---

## ⚠️ Challenges Faced

- **Issue:** Lambda failed with an invalid S3 bucket name
- **Root Cause:** Trailing whitespace in the bucket name
- **Resolution:** Sanitized environment variables and validated S3 naming rules

---

## 📈 Future Enhancements

- Incremental exports using `updated_at`
- Exactly-once delivery using DynamoDB
- SNS alerts on failures
- Glue + Athena integration for analytics
- Terraform / IaC automation
- CDC-based near real-time ingestion

---

## 🧠 Key Learnings

- Serverless networking with VPC
- IAM least-privilege role design
- Secure secrets management
- Event-driven architectures
- Debugging AWS SDK validation errors
- Cost-optimized cloud solutions

---

## 🎯 Solution

Design and implement a **fully serverless pipeline** that:
- Runs on a fixed schedule
- Securely connects to RDS inside a VPC
- Exports relational data as CSV
- Stores output in Amazon S3
- Scales automatically
- Incurs near-zero cost when idle

---

## 🏁 Conclusion

This project demonstrates a real-world, production-ready serverless data pipeline, showcasing strong DevOps and AWS cloud architecture skills suitable for interviews and portfolio presentation.

