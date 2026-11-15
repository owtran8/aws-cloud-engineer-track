# AWS Week 7 — Serverless & Event-Driven Architecture

## Lab 7.1 — API Gateway + Lambda + DynamoDB

Moved PropertyLite's property lookup from EC2 to AWS Lambda.

### Architecture

Client (curl)
    |
    v
API Gateway (GET /properties/{id})
    |
    v
Lambda (get-property)
    |
    v
DynamoDB (Properties)
    |
    v
JSON Response

### Results
- HTTP 200 OK
- Successfully retrieved property R100234
- Lambda IAM policy allows DynamoDB GetItem only

## Lab 7.2 — SQS + Dead-Letter Queue

Created:
- property-queue
- property-dlq

Configured maxReceiveCount = 3.

Successfully sent and received:
{"PropertyId":"P1002"}

## Lab 7.3 — CloudWatch Debugging

Inspected Lambda execution logs in CloudWatch.

Verified successful execution using:
- INIT_START
- START
- END
- REPORT

No Lambda execution errors were observed.

## Testing

Run:

bash test-api.sh
