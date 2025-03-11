# Flask Application Deployment on Kubernetes

This repository contains Kubernetes manifests and application code for deploying a Flask application with PostgreSQL database.

## Prerequisites

- Minikube
- kubectl
- Docker

## Deployment Steps

1. Start Minikube:
```bash
minikube start --driver=docker
```

2. Build the Flask application:
```bash
cd app
minikube image build -t flask-app .
```

3. Deploy PostgreSQL:
```bash
kubectl apply -f manifests/configmap/postgres-configmap.yaml
kubectl apply -f manifests/secret/postgres-secret.yaml
kubectl apply -f manifests/deployment/postgres-deployment.yaml
kubectl apply -f manifests/service/postgres-service.yaml
```

4. Deploy Flask application:
```bash
kubectl apply -f manifests/deployment/flask-deployment.yaml
kubectl apply -f manifests/service/flask-service.yaml
```

5. Access the application:
```bash
minikube service flask-app
```

## Testing

1. Check all resources:
```bash
kubectl get all
```

2. Scale the deployment:
```bash
kubectl scale deployment flask-app --replicas=5  # Scale up
kubectl scale deployment flask-app --replicas=2  # Scale down
```

3. Test database connection:
```bash
curl http://<service-ip>/db-test
```

## Cleanup

To delete all resources:
```bash
kubectl delete -f manifests/
``` 