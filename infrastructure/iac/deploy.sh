STACK_NAME="MyStack"
TEMPLATE_FILE="templates/template.yaml"

aws cloudformation deploy \
  --stack-name $STACK_NAME \
  --template-file $TEMPLATE_FILE \
  --capabilities CAPABILITY_NAMED_IAM