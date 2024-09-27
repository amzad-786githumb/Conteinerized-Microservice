# Functions-from-zero
live training

[![Python application test with Github Actions](https://github.com/amzad-786githumb/Functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/amzad-786githumb/Functions-from-zero/actions/workflows/main.yml)

###To call Microservice

something like this
'''bash
curl -X 'POST' \
  'https://noahgift-functions-from-zero-r7g59wcxx6x-8080.githubpreview.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
'''

### Build Container
`docker build .`
`docker image ls`

###Run container
`docker run -p 127.0.0.1:8080:8080 0cc4de44ba58`

###Invoke 

run `invoke.sh`