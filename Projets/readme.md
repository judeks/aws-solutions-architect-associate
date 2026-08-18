aws lambda create-function --function-name GenerateThumbnail \
--runtime python3.9 \
--role arn:aws:iam::483996345809:role/LambdaS3ThumbnailRole \
--handler lambda_function.lambda_handler \
--timeout 10 \
--memory-size 256 \
--zip-file fileb://lambda_function.zip