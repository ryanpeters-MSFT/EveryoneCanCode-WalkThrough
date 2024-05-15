# build the docker container using the Dockerfile
docker build -f Dockerfile . -t todo:latest

# run the container locally
docker run --name todo -p 5000:5000 todo:latest

# if tagged for docker.com
#docker push binarydad/todo:latest