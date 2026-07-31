# File Sync (copy files between storage providers)

Copy files from a source storage provider to a destination storage provider,
overwriting the destination. Useful to distribute exports, mirrors or backups
between SFTP, S3, Dropbox or Google Drive.

## When to use

- The worker needs to copy a set of files between two storage locations
  (e.g. upload nightly exports from an SFTP folder to S3, or a Dropbox folder
  to Google Drive).
- A transfer is already configured and only needs to be run now, or a new
  transfer must be created.

## Prerequisites

- Credentials of type storage (SFTP / S3 / Dropbox / Google Drive) for source
  and destination, created from admin/credentials.

## Implementation via Bizzmod MCP

- List configured transfers with `module.data` on `file-sync` / `transfers`.
- List past runs with `module.data` on `file-sync` / `runs` (and per-file logs
  on `file-sync` / `run_files`).
- Create a transfer with `module.create` on `file-sync` / `transfers`:
  provide `name`, `source_credential_id`, `source_folder`, `source_pattern`
  (e.g. `*.csv`), `recursive`, `destination_credential_id`, `destination_folder`,
  `overwrite`, `enabled`, `trigger_type` (`scheduled` or `manual`) and
  `interval` (hourly/daily/weekly/monthly).
- Run a transfer now with the concrete tool `file-sync.run_transfer`
  (argument `transfer_id`). Scheduled transfers also run automatically on the
  configured interval.
