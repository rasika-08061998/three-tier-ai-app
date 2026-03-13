Three-Tier AI Application (React + FastAPI + PostgreSQL)
Project Overview

This repository contains the application code for a cloud-native three-tier microservices platform deployed on Amazon EKS using GitOps and ArgoCD.

The application follows a modern microservices architecture:

Frontend → React.js

Backend API → Python FastAPI

Database → PostgreSQL

The platform is designed to demonstrate production-grade DevOps practices, including:

Docker containerization

GitHub Actions CI pipeline

AWS ECR image registry

GitOps deployments using ArgoCD

Kubernetes orchestration with Amazon EKS

AWS Application Load Balancer (ALB) ingress

Architecture Overview
User
   |
   v
AWS ALB (Ingress Controller)
   |
   +----------------+
   |                |
Frontend        Backend API
React           FastAPI
   |                |
   +--------> PostgreSQL
Repository Structure
three-tier-ai-app
│
├── backend
│   ├── app
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend
│   ├── src
│   ├── package.json
│   └── Dockerfile
│
├── docker-compose.yml
└── .github
    └── workflows
        └── ci.yaml
Application Components
Frontend (React)

The frontend is built using React.js and communicates with the backend API.

Features:

User interface for AI chat interaction

API communication with backend

Containerized using Docker

Runs on:

Port: 3000
Backend (FastAPI)

The backend is a Python FastAPI microservice providing:

REST API endpoints

Chat AI interface

Database interaction

Example endpoints:

GET  /health
POST /chat

Swagger UI:

/docs

Runs on:

Port: 8000
Database (PostgreSQL)

PostgreSQL stores application data.

In Kubernetes it is deployed using:

StatefulSet

PersistentVolume

AWS EBS CSI driver

Local Development
Prerequisites

Docker

Docker Compose

Node.js

Python 3.10+

Run locally
docker-compose up --build

Access:

Frontend

http://localhost:3000

Backend

http://localhost:8000/docs
CI Pipeline (GitHub Actions)

The CI pipeline automatically builds and pushes Docker images to Amazon ECR.

Pipeline steps:

1️⃣ Checkout code
2️⃣ Configure AWS credentials via OIDC
3️⃣ Build Docker images
4️⃣ Push images to AWS ECR
5️⃣ Update GitOps repository with new image tag

Location:

.github/workflows/ci.yaml
Container Registry

Images are stored in Amazon Elastic Container Registry (ECR).

Example images:

python-microservice-app
react-frontend-app

Image tags are generated using:

Git commit SHA
GitOps Deployment

Application deployment is handled using ArgoCD.

This repository does not contain Kubernetes manifests.

Instead, deployments are managed in a separate repository:

eks-gitops-deployments

The CI pipeline automatically updates image tags there.

Production Deployment

Production deployment includes:

Amazon EKS cluster

AWS Load Balancer Controller

ALB Ingress routing

ArgoCD GitOps

Routes:

/        → frontend
/api     → backend
DevOps Technologies Used

AWS EKS

Terraform

Docker

GitHub Actions

ArgoCD

Kubernetes

AWS ECR

AWS ALB

PostgreSQL

FastAPI

React

Future Improvements

Planned improvements:

Prometheus monitoring

Grafana dashboards

Horizontal Pod Autoscaling

AWS Secrets Manager integration

HTTPS with ACM

AI model integration

Author

Rasika Deshmukh
DevOps Engineer
