# AWS Cloud Engineer Journey (Week1)
<!-- Commit a week-01/ folder to your repo containing: 
a screenshot of MFA enabled, a screenshot of the budget, 
and a README.md describing what root vs IAM vs Shared Responsibility Model means, in yourown words (5–8 sentences).
-->

The root user is da main AWS account that has unlimited access to the whole site, including services, billing, and security settings. 
The root user decides whether or not to create or delete resources like EC2 instances and S3 buckets, so it's like the owner. 

An IAM user is a separate AWS user that can be given specific permissions depending on what they need to do. IAM stands for 
Identity and Access Management so the IAM user helps control who can access certain AWS services and what actions they are allowed to perform. 

The Shared Responsibility Model just means AWS is responsible for securing the cloud infrastructure  
while the user is still responsible for securing their own data, accounts, permissions, and resources inside AWS so AWS does not operate those services for the user just the settings you can think. 