# Clear S3 bucket.
cd angular
if [ -d dist ]
then
   aws s3 rm s3://${S3_BUCKET} --recursive
   echo S3 bucket is cleared.
   # Copy dist folder to S3 bucket, As of Angular 6, builds are stored inside an app folder in distribution and not at the root of the dist folder
   aws s3 cp dist s3://${S3_BUCKET} --recursive
   echo Build completed on `date`
else
   echo "no dist folder, aborting build"
fi