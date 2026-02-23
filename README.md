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

## 🎯 Solution

Design and implement a **fully serverless pipeline** that:
- Runs on a fixed schedule
- Securely connects to RDS inside a VPC
- Exports relational data as CSV
- Stores output in Amazon S3
- Scales automatically
- Incurs near-zero cost when idle

---

## 🏗️ Architecture

```text
Amazon EventBridge (Scheduled Trigger)
            ↓
        AWS Lambda
            ↓
        Amazon RDS
            ↓
        Amazon S3
