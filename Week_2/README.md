# Week 2 — IAM & Security Foundations

## Overview:

- **Goal:** Give a test user limited access to one S3 bucket.
- **Permissions:** PutObject and GetObject on that bucket’s objects.
- **Scope:** The exact bucket ARN with /*; no wildcard access to other buckets.
- **Test results:** Listing denied; upload and download succeeded.
- **Access Analyzer:** Analyzer type, region, status, and actual findings.
- **Debugging:** What happened when /* was missing and how restoring it fixed access.

## Lab 2 Objective

Have `s3-test-user` allowed limited access to:

1. S3 bucket
2. Test its permissions using the CLI profile `s3test`.

## Policy Created: S3UploaderOnly-owen

**Policy file:** [s3-uploader-only.json](policies/s3-uploader-only.json)

The IAM policy we made is only enabled for the test user.

| Permission | What it allows |
| --- | --- |
| `s3:PutObject` | Upload files, including replacing existing files. |
| `s3:GetObject` | Download files when the exact file name is known. |

The upload and download files -> only alloed for the S3 bucket we created:

```text
arn:aws:s3:::my-training-bucket-owen-2026/*
```

### Why did we only need upload and download files?

The user only needs to upload and download files in one training bucket. The `/*` covers objects inside that bucket. This policy does not grant permission to list buckets, list files, delete files, or access other buckets. (Least privilege -> only the minimum access given!)

## Tests

All the tests use `--profile s3test`.

| Test | Expected | Actual |
| --- | --- | --- |
| List buckets | AccessDenied | [Fill in] |
| Upload a file | Success | [Fill in] |
| Download a file | Success | [Fill in] |

## Debugging

When we removed the `/*` it made the policy match the bucket itself instead of its objects, so the upload failed. Adding the `/*` back fixes the resource scope.

However, we can also do an explicit Deny that would override an Allow.

- **Upload without `/*`:** AccessDenied
- **Policy Simulator result for `s3:PutObject`:** [Fill in, or Not run]
- **Upload after restoring `/*`:** Works

## Access Analyzer

An external access analyzer checks da supported resources for public access outside the main acc.

- **Analyzer name:** week02-external-access
- **Type and zone of trust:** External access / current AWS account
- **Region:** US East (Ohio) — us-east-2
- **Status:** Active
- **Active findings:** None (0)

Zero findings means no active external access findings within its scope are there.

## Screenshots

Photos include the policy, permission tests, debugging results, and analyzer findings.