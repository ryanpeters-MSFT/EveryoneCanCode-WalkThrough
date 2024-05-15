kubectl create deploy todo --image binarydad/todo:latest --replicas 1 --port 5000

kubectl expose deploy todo --type LoadBalancer --port 80 --target-port 5000