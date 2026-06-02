

* Display space ebs
   lsblk
* Augmenter la Taille du Volume EBS
   - Récupérer l’ID du volume EBS attaché à l’instance :

            aws ec2 describe-instances \
            --instance-ids INSTANCE_ID \
            --query "Reservations[0].Instances[0].BlockDeviceMappings[0].Ebs.VolumeId" \
            --output text

  - Augmenter la taille du volume

        aws ec2 modify-volume \

        --volume-id VOLUME_ID \

        --size 20

   - Vérifier l’état du redimensionnement 

            aws ec2 describe-volumes-modifications \

            --volume-ids VOLUME_ID \

            --query "VolumesModifications[0].ModificationState" \

            --output text
   - Redimensionner la Partition

                sudo growpart /dev/xvda 1