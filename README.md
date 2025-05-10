# AWS Event-Driven Order Processing System

**Author:** Mamdouh Hazem  
**ID:** 10001816  
**Section:** T|20  

##  Project Summary

This repository contains the implementation of a **serverless, event-driven order processing system** using AWS services such as **SNS**, **SQS**, **Lambda**, and **DynamoDB**. The system allows asynchronous and decoupled message handling and supports failure monitoring through a **Dead Letter Queue (DLQ)**.

All components were configured through the AWS Console, without using any Infrastructure as Code.

---

##  Architecture Overview

**Workflow:**

1. **SNS** (`OrderTopic`) receives an order notification published by a producer.
2. The message is automatically passed to an **SQS Queue** (`OrderQueue`).
3. The arrival of a new message in the queue invokes a **Lambda function** (`ProcessOrderLambda`).
4. Lambda parses the message and inserts the order into a **DynamoDB** table (`Orders`).
5. If processing fails after 3 attempts, the message is redirected to an **SQS DLQ** (`OrderQueueDLQ`).

This structure promotes scalability, fault tolerance, and low operational overhead.

---

##  Services Used

- **Amazon SNS**: Acts as the entry point for new order messages.
- **Amazon SQS**: Buffers messages for Lambda and enables retry control.
- **AWS Lambda**: Executes business logic for order persistence.
- **Amazon DynamoDB**: NoSQL table for storing order records.
- **Amazon SQS DLQ**: Captures unprocessable messages for debugging.
- **Amazon CloudWatch**: Used to monitor Lambda logs and system behavior.

---

##  How It Was Built

1. Created DynamoDB table `Orders` with `orderId` as the primary key.
2. Set up `OrderTopic` as the SNS topic.
3. Created `OrderQueue` as the SQS buffer and linked it to the DLQ `OrderQueueDLQ`.
4. Subscribed the queue to the topic.
5. Built the `ProcessOrderLambda` function in Python 3.12.
6. Added IAM permissions for the Lambda to access DynamoDB, SQS, and CloudWatch.
7. Connected the Lambda function to the SQS queue via a trigger.
8. Sent a test order through SNS and verified full flow:
   - Message forwarded → SQS → Lambda executed → DynamoDB updated → Logs confirmed in CloudWatch.

---

##  Key Concepts

- **Visibility Timeout**: Prevents duplicate message processing by hiding a message during Lambda execution. If Lambda fails, the message reappears for retry.
- **DLQ**: Collects failed messages after multiple processing attempts, allowing isolation and debugging without impacting normal traffic.

---

##  Screenshots

All configuration steps and successful test results are included in the attached screenshots PDF.

---

##  Optional: CloudFormation Attempt

A CloudFormation template was prepared, but deployment failed due to existing resources with conflicting names. Manual configuration remained the verified path.

---

##  Outcome

This project demonstrates how AWS-native services can be used to construct a resilient, decoupled, and cost-efficient order processing system. The design adheres to serverless and event-driven principles, ensuring real-time processing with fault isolation.
