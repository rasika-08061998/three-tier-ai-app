# 🚀 DevOps Platform on AWS using EKS, GitOps and CI/CD

---

## 📌 Project Overview

This project demonstrates a **production-style DevOps platform** built on AWS using modern DevOps practices.

The platform automates the deployment of a **containerized three-tier application** using the following technologies.

### Technologies Used

1. **Terraform**
   - Infrastructure as Code tool used to provision AWS infrastructure.
   - It creates resources such as VPC, subnets, NAT gateway, and EKS cluster.

2. **GitHub Actions**
   - CI/CD automation platform.
   - Used to build Docker images and push them to AWS ECR.

3. **Docker**
   - Containerization platform.
   - Packages the application and its dependencies into portable containers.

4. **Kubernetes (AWS EKS)**
   - Container orchestration system.
   - Used to deploy and manage application containers.

5. **ArgoCD**
   - GitOps continuous delivery tool for Kubernetes.
   - Automatically deploys Kubernetes manifests from a Git repository.

6. **Prometheus**
   - Monitoring system used for collecting metrics from Kubernetes.

7. **Grafana**
   - Visualization tool used to create monitoring dashboards.

---

## 🏗 Overall Architecture

The architecture follows a **GitOps-based DevOps workflow**.

Developer → GitHub → CI/CD Pipeline → Docker Image → AWS ECR → ArgoCD → Kubernetes (EKS) → Monitoring

---

## 📊 Architecture Diagram:



