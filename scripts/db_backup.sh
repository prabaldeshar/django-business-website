
db_name=$1
date=$(date +"%Y-%m-%d-%H:%M:%S")
filename=$db_name"_"$date

echo "Starting PostgreSQL database dump..."

sudo docker exec django-business-website-db-1 pg_dump -h localhost -p 5432 -U prabal -d $db_name > $filename

# if [ $? -eq 0 ]; then
#   echo "Database dump completed successfully. Filename: $filename"
# else
#   echo "Database dump failed!"
#   exit 1
# fi

echo "Compressing the dump file..."

gzip $filename

if [ $? -eq 0 ]; then
  echo "Compression completed successfully. Compressed file: $filename.gz"
else
  echo "Compression failed!"
  exit 1
fi

zipfile_name=$filename".gz"

echo "Uploading the compressed file to AWS S3..."

s3_filepath="s3://codesphire-db-backups/"$db_name"/"
aws s3 cp $zipfile_name $s3_filepath

if [ $? -eq 0 ]; then
  echo "Upload to S3 completed successfully."
else
  echo "Upload to S3 failed!"
  exit 1
fi

echo "Removing the local compressed file..."

rm $zipfile_name

echo "Backup process completed."
