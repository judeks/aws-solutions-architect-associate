

aws s3api get-object-lock-configuration --bucket s3-object-loack-bucket
echo "Donne de LeCloudFacile.com qui sont sensibles" > document.txt

aws s3api put-object \
     --bucket s3-object-loack-bucket \
     --key document.txt \
     --body document.txt \
     --object-lock-mode GOVERNANCE \
     --object-lock-retain-until-date "$(date -d '+5 minute' --utc +%Y-%m-%ddT%h:%m:%SZ)"   

Result

{
    "ETag": "\"9de625c722ce2dca494a4eff96678385\"",
    "ChecksumCRC64NVME": "tNqrAmTuZfY=",
    "ChecksumType": "FULL_OBJECT",
    "ServerSideEncryption": "AES256",
    "VersionId": "uu8ulHwO0f8jDO2KBnAr.EBBQR0K7OXX"
}


aws s3api get-object-retention --bucket s3-object-loack-bucket --key document.txt

result

~ $ aws s3api get-object-retention --bucket s3-object-loack-bucket --key document.txt
{
    "Retention": {
        "Mode": "GOVERNANCE",
        "RetainUntilDate": "2026-08-04T13:46:22+00:00"
    }
}

les periodes de retention permet d'empecher quiconque d'effectuer des actions(supprimer et ecraser sur le fichier)

LegalHolder

echo "Donnees sensibles" > document_legal.txt
aws s3 cp docuement_legal.txt s3://s3-object-loack-bucket

aws s3api put-object-legal-hold \
      --bucket s3-object-loack-bucket \
      --key document_legal.txt \
      --legal-hold Status=ON

Verification

aws s3api get-object-legal-hold \
       --bucket s3-object-loack-bucket \
       --key document_legal.txt
{
    "LegalHold": {
        "Status": "ON"
    }
}