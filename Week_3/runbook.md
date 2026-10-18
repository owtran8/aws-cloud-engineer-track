# Week 3 — EC2

## Deployment
- Launched `property-api-01` with Amazon Linux 2023.
- Instance type: [instance type].
- Saved `training-key` in `~/.ssh/`.
- Opened ports 22 (SSH) and 8080 (API).
- Used user data to install Python/Flask and start PropertyLite.

## Testing
- `/health` returned `{"status":"ok"}`.
- `/properties/R100234` returned the Sacramento listing.
- Connected through SSH after running `chmod 400` on the key.
- Saved screenshots.

## Troubleshooting
Opening port 8080 fixed the API timeout.
For SSH timeouts, check the instance, public IP, firewall rules, and internet route. “My IP” must be updated when your IP changes.

## Snapshot
- ID: [snapshot ID].
- Status: [snapshot status].
- A snapshot backs up disk data so it can be restored to a new volume.

## Cleanup
[Confirm instance terminated, root volume deleted, and lab security group deleted.]