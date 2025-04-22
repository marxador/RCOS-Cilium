# Docker, Kubernetes, and Cilium Deployment Guide for Spotify Monthly Wrapped App

## Phase 1: Environment Setup

### Install Required Tools

1. **Docker**: Install Docker for containerization ([Download Docker](https://www.docker.com/get-started)).
    - Verify installation:
      ```bash
      docker --version
      ```

2. **Kubernetes**: Install Minikube for a local Kubernetes cluster.
    - Verify installation:
      ```bash
      minikube version
      ```

3. **kubectl**: Install the Kubernetes CLI tool ([Install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)).
    - Install using Chocolatey:
      ```bash
      choco install kubernetes-cli
      ```
    - Verify installation:
      ```bash
      kubectl version --client
      ```

4. **Helm**: Install Helm for managing Kubernetes applications ([Install Helm](https://helm.sh/docs/intro/install/)).
    - Install using Chocolatey:
      ```bash
      choco install kubernetes-helm
      ```
    - Verify installation:
      ```bash
      helm version
      ```

5. **Cilium**: Install Cilium for networking and security in Kubernetes ([Install Cilium](https://docs.cilium.io/en/stable/gettingstarted/)).
    - Install using Chocolatey:
      ```bash
      choco install cilium-cli
      cilium install
      ```
    - Verify installation:
      ```bash
      cilium status
      ```

---

## Phase 2: Building Microservices Locally

### Create Flask Microservices

1. **Build Service A**:
    - Handles Spotify OAuth and user input (month/year).
    - Sends data and access token to Service B.

2. **Build Service B**:
    - Receives request from Service A.
    - Uses Spotify Web API to return user's top tracks for the last 4 weeks.

### Run Locally with Docker

1. **Build Docker Images**:
    ```bash
    docker build -t spotify-service-a ./service_a
    docker build -t spotify-service-b ./service_b
    ```

2. **Run Docker Containers**:
    ```bash
    docker run -d --name service-b -p 5001:5001 spotify-service-b
    docker run -d --name service-a -p 5000:5000 spotify-service-a
    ```

3. **Access Application**:
    - Visit `http://localhost:5000` in your browser to start the Spotify login flow.

---

## Phase 3: Spotify API Setup

### Configure Spotify Developer Application

1. **Create Spotify App**:
    - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
    - Create a new app and copy your `Client ID` and `Client Secret`

2. **Set Redirect URI**:
    - Add the following URI to your app settings:
      ```
      http://localhost:30000/callback
      ```

3. **Set Up `.env` File**:
    ```env
    SPOTIPY_CLIENT_ID=your_client_id
    SPOTIPY_CLIENT_SECRET=your_client_secret
    SPOTIPY_REDIRECT_URI=http://localhost:30000/callback
    ```

---

## Phase 4: Kubernetes Deployment

### Prepare Kubernetes Files

1. **Create ConfigMap for Spotify Credentials**
    - `spotify-config.yaml` stores environment variables securely.

2. **Create Deployment and Service Files**
    - `spotify-service-a.yaml`: NodePort service for external access
    - `spotify-service-b.yaml`: ClusterIP service for internal communication

### Start Kubernetes with Minikube

1. **Start Minikube**:
    ```bash
    minikube start
    ```

2. **Use Minikube's Docker Daemon**:
    ```bash
    eval $(minikube docker-env)
    ```

3. **Build Docker Images in Minikube**:
    ```bash
    docker build -t spotify-service-a ./service_a
    docker build -t spotify-service-b ./service_b
    ```

4. **Apply Kubernetes Manifests**:
    ```bash
    kubectl apply -f spotify-config.yaml
    kubectl apply -f spotify-service-b.yaml
    kubectl apply -f spotify-service-a.yaml
    ```

5. **Access the Application**:
    ```bash
    minikube service service-a
    ```

---

## Phase 5: Integrating with Cilium

### Configure and Monitor Cilium

1. **Ensure Cilium is Running**:
    ```bash
    cilium status
    ```

2. **Run Connectivity Tests**:
    ```bash
    cilium connectivity test
    ```

3. **Label Namespace for Cilium (Optional)**:
    ```bash
    kubectl label namespace default "kubernetes.io/metadata.name"="default"
    ```

4. **Deploy Services With Cilium Active**:
    ```bash
    kubectl apply -f spotify-config.yaml
    kubectl apply -f spotify-service-b.yaml
    kubectl apply -f spotify-service-a.yaml
    ```

5. **Monitor Traffic with Hubble** (Optional):
    ```bash
    cilium hubble enable
    cilium hubble port-forward &
    hubble ui
    ```

6. **(Optional) Apply Network Policies**:
    - Example policy to restrict access to Service A:
    ```yaml
    apiVersion: cilium.io/v2
    kind: CiliumNetworkPolicy
    metadata:
      name: allow-service-b-to-a
    spec:
      endpointSelector:
        matchLabels:
          app: service-a
      ingress:
      - fromEndpoints:
        - matchLabels:
            app: service-b
    ```
    - Apply the policy:
    ```bash
    kubectl apply -f cilium-policy.yaml
    ```

---

## Summary of What Was Done

You built and deployed a two-service Flask application that uses Spotify OAuth to generate a personalized monthly music summary, Dockerized both services, and deployed them on Kubernetes with Minikube and Cilium for observability and security.

---

## Additional Notes

- Used **Chocolatey** on Windows for easy tool installation.
- Docker may take ~20 minutes to enable Kubernetes the first time.
- `service-a.py` must use `http://service-b:5001/...` when running inside Kubernetes.
- Use `docker ps`, `docker stop <id>`, and `docker rm <id>` to manage containers.
- Clean up unused Docker images with `docker rmi image-name` after stopping/deleting associated containers.

