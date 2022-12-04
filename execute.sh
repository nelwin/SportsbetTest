                                                                                                                                #!/bin/bash
#usage:
#sh execute.sh <env> "<tags>" "<RUN_WITHOUT_ALLURE>=no(optional)"

#example

#sh execute.sh dev "--tags=sample"

ENV="$1"
tag_expr="$2"
allure="$3"

export ENV
export tag_expr

echo "ENVIRONMENT: $ENV"
echo "TAG EXPRESSION: $tag_expr"

pip install --prefer-binary -r requirements.txt

if [ -z "$tag_expr" ] ; then
   echo "NO TAGS PROVIDED: TAGS ARE REQUIRED"
   exit 1
else
  if [[ $tag_expr = --tags* ]];then
    tags=$tag_expr
  else
    tags="--tags $tag_expr"
  fi

  echo "EXECUTING FOR TAGS: $tags"
  if [[ $allure = no ]]; then
    python3 -m behave --no-capture --no-skipped $tags features

  else
    python3 -m behave --no-capture --no-skipped $tags -f allure_behave.formatter:AllureFormatter -o test/allure-results features

  fi
fi