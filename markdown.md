# Docker & Kubernetes Setup Guide

## Phase 1: Environment Setup 

### Install Required Tools
1. **Docker**: Install Docker for containerization ([Download Docker](https://www.docker.com/get-started)).
    a. Verify installation
        docker --version
        kubectl version --client

2. **Kubernetes**: Install Minikube or Kind for a local Kubernetes cluster.
    a. Verify installation
        kubectl version --client
3. **kubectl**: Install the Kubernetes CLI tool ([Install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)).
    a. Install using **Chocolatey**
        choco install kind
    b. Verify installation
        kind create cluster
        kubectl get nodes
4. **Helm**: Install Helm for managing Kubernetes applications ([Install Helm](https://helm.sh/docs/intro/install/)).
    a. Install using **Chocolatey**
        choco install kubernetes-helm
    b. Verify installation
        helm version
5. **Cilium**: Install Cilium for networking and security in Kubernetes ([Install Cilium](https://docs.cilium.io/en/stable/gettingstarted/)).
    a. Install using **Chocolatey**
        choco install cilium-cli
        cilium install
    b. Verify installation
        helm version
        cilium status

## Phase 2: Deploy Microservices

### Build Two Microservices
- Develop two complex service APIs:
  - **Service A** (provides core functionality)
  - **Service B** (communicates with Service A)
- Containerize both services using Docker.

### Deploy the Services on Kubernetes
1. **Create YAML Manifests**:
   - Deployment and Service definitions for **Service A**.
   - Deployment and Service definitions for **Service B**.
2. **Expose Services**:
   - Use **ClusterIP** (internal communication) or **NodePort** (external access).

## Additional Notes
- Used **Chocolatey** for some installations on Windows.
- Docker took ~20 minutes to enable Kubernetes; required a restart.
- Have a working plan for coding the two microservices.
