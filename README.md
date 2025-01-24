# Python Web Application with Docker and Kubernetes

A web application displaying environment variable status, containerized with Docker and deployed on Kubernetes.

## Components

- `app.py` - Flask application serving status endpoint
- `Dockerfile` - Container image definition
- `requirements.txt` - Python dependencies
- `deployment.yaml` - Kubernetes deployment configuration
- `secret.yaml` - Kubernetes secret for environment variables

## Setup

1. Build Docker image:
```bash
docker build -t my-python-app .
```

2. Deploy to Kubernetes:
```bash
kubectl apply -f secret.yaml
kubectl apply -f deployment.yaml
```

3. Access application:
```bash
minikube service python-app-service
```

## Environment Variables

- `MY_WEB_APP_STATUS`: Application status displayed at /status endpoint

## Endpoints

- `/status`: Returns JSON with timestamp and environment variable value
