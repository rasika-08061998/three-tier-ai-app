🚀 **DevOps Platform on AWS using EKS, GitOps and CI/CD**


A production-style DevOps platform built on AWS using Terraform, Kubernetes (EKS), GitHub Actions, Docker and GitOps with ArgoCD.

This project demonstrates how modern DevOps teams build automated infrastructure and application deployment pipelines using Infrastructure as Code, CI/CD, and GitOps practices.

📌 **Project Overview**

The goal of this project is to simulate a real-world DevOps environment where:

Infrastructure is provisioned using Terraform

Applications are containerized using Docker

CI/CD pipelines are implemented with GitHub Actions

Deployments are managed through GitOps with ArgoCD

Monitoring is enabled using Prometheus and Grafana

Everything runs on AWS EKS Kubernetes cluster


🏗 **Architecture**

Architecture flow:

Developer
     │
     ▼
GitHub Repository
     │
     ▼
GitHub Actions CI Pipeline
     │
Build Docker Image
     │
     ▼
Push Image to AWS ECR
     │
     ▼
ArgoCD detects manifest changes
     │
     ▼
Deploys application to AWS EKS
     │
     ▼
Monitoring via Prometheus + Grafana


🧰 **Tech Stack**
Category	Tools
Cloud	AWS
Infrastructure as Code	Terraform
Containerization	Docker
Orchestration	Kubernetes (EKS)
CI/CD	GitHub Actions
GitOps	ArgoCD
Container Registry	AWS ECR
Monitoring	Prometheus, Grafana
Networking	VPC, NAT Gateway, Load Balancer

📂 **Repository Structure**

This platform is organized into three repositories.

1️⃣ Infrastructure Repository

eks-devops-platform-infra

Contains Terraform code to provision AWS resources:

1. VPC
2. Subnets
3. NAT Gateway
4. EKS Cluster
5. IAM Roles
6. Bastion Host
7. Security Groups

**Repository link**:

https://github.com/rasika-08061998/eks-devops-platform-infra


2️⃣ **Application Repository**

**three-tier-ai-app
**
**Contains**:

1. Python microservices
2. Dockerfile
3. Application source code
4. GitHub Actions CI pipeline

**Repository link**:

https://github.com/rasika-08061998/three-tier-ai-app


3️⃣ **GitOps Repository**

eks-gitops-deployments

Contains Kubernetes manifests used by ArgoCD to deploy applications.

Includes:

1. Deployments
2. Services
3. ConfigMaps
4. Ingress
5. Monitoring configuration

**Repository link**:

https://github.com/rasika-08061998/eks-gitops-deployments

⚙️ **Infrastructure Provisioning**

Infrastructure is provisioned using Terraform.

Initialize Terraform
terraform init
Validate configuration
terraform validate
Plan infrastructure
terraform plan
Apply infrastructure
terraform apply

After deployment configure kubectl.

**aws eks update-kubeconfig --region <region> --name <cluster-name>**

🐳 **Application Containerization**

**Build Docker image:
**
docker build -t ai-app .

Push image to AWS ECR:

**aws ecr get-login-password --region <region> \
| docker login --username AWS --password-stdin <account>.dkr.ecr.<region>.amazonaws.com**

**docker push <ecr-repository>**


🔄 **CI/CD Pipeline**

The project uses GitHub Actions to automate builds.

Pipeline workflow:

Developer pushes code
       │
       ▼
GitHub Actions triggers pipeline
       │
       ▼
Build Docker image
       │
       ▼
Push image to AWS ECR
       │
       ▼
ArgoCD syncs Kubernetes manifests
       │
       ▼
Application deployed to EKS

🚀 GitOps Deployment

ArgoCD continuously monitors the GitOps repository.

When manifest changes occur:

**Git commit → ArgoCD detects change → Sync → Deployment updated**

Install ArgoCD:

**kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml**

Access UI:

**kubectl port-forward svc/argocd-server -n argocd 8080:443
**

📊 **Monitoring**

Monitoring stack includes:
Prometheus for metrics collection
Grafana for dashboards

Metrics monitored:

CPU usage
Memory usage
Pod health
Application metrics

📈 **DevOps Skills Demonstrated**

This project demonstrates real-world DevOps practices:

Infrastructure as Code
Kubernetes cluster management
CI/CD automation
GitOps deployment strategy
Containerized applications
Cloud-native monitoring
Production-style repository separation

👩‍💻 **Author**

Rasika Deshmukh

DevOps / Cloud Engineer

GitHub
https://github.com/rasika-08061998

⭐ If you like this project, give it a star!
