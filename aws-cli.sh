#GUIA DE COMANDOS PARA USAR AWS CLI

#instalacion de aws cli
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

#validacion de instalacion
aws --version

#listar perfiles actuales, inicialmente sale vacío
aws configure list-profiles

#configurar un nuevo perfil, solo se ejecuta una vez
# AWS_ACCESS_KEY_ID= creado en IAM de AWS , robert lo compartió en planner
# AWS_SECRET_ACCESS_KEY= creado en IAM de AWS, robert lo compartió en planner
# REGION= us-west-2
# OUTPUT= json
aws configure --profile devops-compumundo

#set current profile, cada vez que se ingresa al sh se debe correr salvo que se configure en el .bashrc
export AWS_PROFILE=devops-compumundo


#list iam users
aws iam list-users --output table


#create code build project
# idea es que construya una imagen de contenedor en un S3
aws codebuild create-project \
    --name "compumundo-black-list-CI" \
    --source "{\"type\": \"GITHUB\",\"location\": \"https://github.com/DaGamez/202415-devops-grupo9-compumundohipermegared.git\",\"buildspec\": \"buildspec.yml\",\"gitCloneDepth\": 1,\"gitSubmodulesConfig\": {\"fetchSubmodules\": false},\"reportBuildStatus\": false}" \
    --source-version "main" \
    --artifacts "{\"type\": \"NO_ARTIFACTS\"}" \
    --environment "{\"type\": \"LINUX_CONTAINER\",\"image\": \"aws/codebuild/standard:5.0\",\"computeType\": \"BUILD_GENERAL1_SMALL\"}" \
    --service-role "arn:aws:iam::061039766984:role/service-role/codebuild-devops_grupo09-service-role" \
    --timeout-in-minutes 5

#listar codebuild projects
aws codebuild list-projects --output table

#delete codebuild project
aws codebuild delete-project --name "compumundo-black-list-CI"
