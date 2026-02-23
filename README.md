🚀 Capstone Project: Serverless RDS to S3 Data Export Pipeline
📌 Project Overview

This project implements a serverless, scheduled data ingestion pipeline that extracts data from an Amazon RDS database and exports it as CSV files into Amazon S3 using modern AWS-native services.

The solution replaces deprecated AWS Data Pipeline–based workflows with a Lambda + EventBridge architecture that is cost-efficient, secure, and production-ready.

🧩 Problem Statement

Traditional RDS data exports often rely on:

Long-running EC2 instances

Deprecated AWS Data Pipeline

Hard-coded database credentials

High operational overhead

These approaches increase cost, security risk, and maintenance effort.

🎯 Solution

Design and implement a fully serverless pipeline that:

Runs on a fixed schedule (every 5 minutes / 12 hours)

Securely connects to RDS inside a VPC

Exports relational data as CSV

Stores output in S3

Scales automatically

Costs nearly nothing when idle

🏗️ Architecture
Amazon EventBridge (schedule)
        ↓
AWS Lambda (Python)
        ↓
Amazon RDS (MySQL / PostgreSQL)
        ↓
Amazon S3 (CSV exports)
🛠️ Technologies Used

AWS Lambda – Data extraction and export logic

Amazon EventBridge – Time-based orchestration

Amazon RDS – Source database

Amazon S3 – CSV storage

AWS Secrets Manager – Secure credential storage

Amazon CloudWatch – Logging & monitoring

IAM, VPC, Security Groups

⚙️ Key Features

✅ Fully serverless (no EC2, no cron servers)

✅ Secure credential handling (no plaintext secrets)

✅ Runs inside VPC for private RDS access

✅ Scheduled execution using EventBridge

✅ Automatic CSV generation and upload

✅ Extremely low cost (pay-per-use)

✅ Production-ready IAM least privilege model

🔐 Security Design

Database credentials stored in Secrets Manager

Lambda execution role follows least privilege

RDS access restricted via security groups

No public DB access

No hard-coded secrets in code

📄 Data Flow

EventBridge triggers Lambda based on schedule

Lambda retrieves DB credentials from Secrets Manager

Lambda connects to RDS inside VPC

SQL query runs on target table

Result set is converted to CSV

CSV file is uploaded to S3 with timestamped name

Execution logs written to CloudWatch

📦 Sample Output
s3://my-rds-export-bucket/rds_exports/
 ├── employees_20260222_101200.csv
 ├── employees_20260222_221200.csv
💰 Cost Analysis
Service	Cost Impact
EventBridge	~$0.000001 per run
Lambda	~$0.000005 per execution
S3	Few MBs → negligible
CloudWatch Logs	Negligible
RDS	Existing hourly cost

Total: Effectively free for low-frequency schedules.

⚠️ Challenges Faced & Fixes
Issue: Lambda could not upload to S3

Cause: Trailing whitespace in bucket name
Fix: Sanitized environment variables using .strip() and validated S3 naming rules

📈 Enhancements (Future Scope)

Incremental exports using updated_at

Exactly-once processing using DynamoDB state tracking

SNS alerts on failure

Glue/Athena integration for analytics

Terraform/IaC automation

CDC-style near real-time ingestion

🧠 Learnings

Deep understanding of serverless networking with VPC

Practical IAM role design

Secrets Manager integration

Cost-optimized event-driven architectures

Debugging AWS SDK validation errors

Designing production-grade pipelines without EC2

🏁 Conclusion

This project demonstrates a modern DevOps + Cloud data engineering workflow, replacing legacy AWS services with a scalable, secure, and cost-effective serverless solution.

It is suitable for:

Production workloads

Cloud/DevOps interviews

Real-world data export automation
