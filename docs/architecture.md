# Architecture

EventBridge triggers AWS Lambda on a fixed schedule.
Lambda connects to RDS inside a VPC, extracts data, and exports it as CSV into S3.
Secrets Manager is used for secure credential storage.

## 🏗️  Architecture

```text
Amazon EventBridge (Scheduled Trigger)
            ↓
        AWS Lambda
            ↓
        Amazon RDS
            ↓
        Amazon S3

![Pipeline Diagram](images/pipeline_diagram.png)
