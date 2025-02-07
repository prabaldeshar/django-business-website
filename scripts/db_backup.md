
# Automate DB backup


## Backup script
Create a script `/root/db_backup/db_backup/db_backup.sh` to create dump, zip the dump file and upload to s3 bucket 

## Crontab config
Create cronjob to run this script at 3:15 pm PM NPT. The time given here is the equivalent UTC time.

Open crontab `crontab -e` 

Add the following cronjob

```
30 9 * * * bash /root/db_backup/db_backup.sh ideal-interior
```

This cron job runs the `db_backup.sh` script at 3:15 pm PM NPT for the database ideal-interior 
