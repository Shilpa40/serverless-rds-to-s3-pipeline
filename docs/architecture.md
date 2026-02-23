# Architecture

EventBridge triggers AWS Lambda on a fixed schedule.
Lambda connects to RDS inside a VPC, extracts data, and exports it as CSV into S3.
Secrets Manager is used for secure credential storage.

