# 🚀 DevOps Platform on AWS using EKS, GitOps and CI/CD

![AWS](https://img.shields.io/badge/Cloud-AWS-orange)
![Terraform](https://img.shields.io/badge/IaC-Terraform-blue)
![Docker](https://img.shields.io/badge/Container-Docker-blue)
![Kubernetes](https://img.shields.io/badge/Orchestration-Kubernetes-blue)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub%20Actions-black)
![ArgoCD](https://img.shields.io/badge/GitOps-ArgoCD-red)
![Monitoring](https://img.shields.io/badge/Monitoring-Prometheus%20%26%20Grafana-green)

---

# 📌 Project Overview

This project demonstrates a **production-style DevOps platform built on AWS** using modern DevOps tools and practices.

The platform automates the deployment of a **containerized three-tier application** using infrastructure automation, CI/CD pipelines, GitOps deployment, and Kubernetes orchestration.

The goal of this project is to simulate how **real DevOps teams build automated cloud infrastructure and application delivery pipelines.**

---

# 🏗 Overall Project Architecture

The architecture follows a **GitOps-based DevOps workflow**.

Developer → GitHub → CI/CD Pipeline → Docker Image → AWS ECR → ArgoCD → Kubernetes (EKS) → Monitoring

This project is organized using **three separate GitHub repositories**, which reflects real-world DevOps platform architecture.

---

# 📂 GitHub Repositories Used in This Project

### 1️⃣ Infrastructure Repository

**Repository Name**

eks-devops-platform-infra

**Repository Link**

https://github.com/rasika-08061998/eks-devops-platform-infra

Purpose of this repository:

1. Contains Terraform code for provisioning AWS infrastructure
2. Creates networking components such as VPC and subnets
3. Deploys the Amazon EKS cluster
4. Configures IAM roles and security groups

---

### 2️⃣ Application Repository

**Repository Name**

three-tier-ai-app

**Repository Link**

https://github.com/rasika-08061998/three-tier-ai-app

Purpose of this repository:

1. Contains the application source code
2. Includes Dockerfile for containerizing the application
3. Includes GitHub Actions workflow for CI/CD pipeline

---

### 3️⃣ GitOps Deployment Repository

**Repository Name**

eks-gitops-deployments

**Repository Link**

https://github.com/rasika-08061998/eks-gitops-deployments

Purpose of this repository:

1. Contains Kubernetes manifest files
2. Stores deployment configurations for the application
3. Enables GitOps deployment using ArgoCD

---

# 🧰 Tools Used in This DevOps Platform

## 1️⃣ AWS (Amazon Web Services)

Definition:

AWS is a cloud computing platform that provides scalable infrastructure services such as compute, networking, and storage.

Purpose in this project:

1. Host the Kubernetes cluster using Amazon EKS
2. Provide networking infrastructure using VPC and subnets
3. Store Docker images using Amazon ECR
4. Run monitoring tools for observability

---

## 2️⃣ Terraform

Definition:

Terraform is an **Infrastructure as Code (IaC)** tool that allows infrastructure to be defined and managed using configuration files.

Purpose in this project:

1. Automates creation of cloud infrastructure
2. Ensures consistent infrastructure provisioning
3. Allows infrastructure to be version-controlled

Infrastructure created using Terraform:

1. VPC
2. Subnets
3. NAT Gateway
4. EKS cluster
5. IAM roles

---

## 3️⃣ Docker

Definition:

Docker is a containerization platform used to package applications and dependencies into lightweight containers.

Purpose in this project:

1. Package application into container images
2. Ensure consistent runtime environment
3. Enable portability across environments

---

## 4️⃣ Kubernetes

Definition:

Kubernetes is an open-source container orchestration platform that automates deployment, scaling, and management of containerized applications.

Purpose in this project:

1. Run application workloads
2. Manage pods and services
3. Provide high availability and scalability

---

## 5️⃣ Amazon EKS

Definition:

Amazon Elastic Kubernetes Service (EKS) is a managed Kubernetes service provided by AWS.

Purpose in this project:

1. Host the Kubernetes cluster
2. Manage container workloads
3. Provide managed control plane for Kubernetes

---

## 6️⃣ GitHub Actions

Definition:

GitHub Actions is a CI/CD automation platform integrated with GitHub repositories.

Purpose in this project:

1. Build Docker images automatically
2. Push images to AWS ECR
3. Trigger application deployment pipelines

---

## 7️⃣ ArgoCD

Definition:

ArgoCD is a GitOps continuous delivery tool designed for Kubernetes.

Purpose in this project:

1. Monitor Git repository for manifest changes
2. Synchronize Kubernetes cluster state
3. Deploy application automatically

---

## 8️⃣ Prometheus

Definition:

Prometheus is a monitoring system used to collect metrics from infrastructure and applications.

Purpose in this project:

1. Monitor Kubernetes cluster metrics
2. Track CPU and memory usage
3. Provide application observability

---

## 9️⃣ Grafana

Definition:

Grafana is a visualization tool used for creating dashboards from monitoring data.

Purpose in this project:

1. Display Prometheus metrics
2. Visualize system performance
3. Monitor application health

---

# ⚙️ Project Workflow (Start to Finish)

### 1️⃣ Infrastructure Provisioning

Infrastructure is created using Terraform.

Commands used:

terraform init  
terraform plan  
terraform apply  

This provisions the following resources:

1. AWS VPC
2. Subnets
3. NAT Gateway
4. Amazon EKS cluster
5. Bastion host

---

### 2️⃣ Application Containerization

The application is packaged into Docker containers.

Example command:

docker build -t ai-app .

The Docker image is then pushed to **AWS ECR**.

---

### 3️⃣ Continuous Integration (CI Pipeline)

GitHub Actions automatically runs when code is pushed.

Pipeline tasks:

1. Build Docker image
2. Push image to AWS ECR
3. Update Kubernetes deployment configuration

---

### 4️⃣ GitOps Deployment

ArgoCD monitors the GitOps repository.

Workflow:

1. Developer updates deployment manifests
2. Changes pushed to GitHub repository
3. ArgoCD detects change
4. Kubernetes cluster is synchronized
5. Application is deployed automatically

---

### 5️⃣ Application Deployment on Kubernetes

The application runs inside Kubernetes pods.

Application architecture includes:

1. Frontend service
2. Backend API
3. Database layer

---

### 6️⃣ Monitoring and Observability

Monitoring stack includes:

Prometheus → collects metrics  
Grafana → visualizes metrics  

Metrics monitored include:

1. CPU usage
2. Memory usage
3. Pod health
4. Application performance

---

# 📊 Architecture Diagram

![Project Architecture](docs/Project_Architecture.png)

---

# 🧹 Cleanup (Stop AWS Costs)

To destroy the infrastructure and stop AWS billing:

terraform destroy

Also verify removal of:

1. EKS cluster
2. NAT Gateway
3. Load balancers
4. ECR repositories
5. EC2 instances

---

# 👩‍💻 Author

Rasika Deshmukh  
DevOps / Cloud Engineer  

GitHub Profile  
https://github.com/rasika-08061998
