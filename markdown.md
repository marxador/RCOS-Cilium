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

## Phase 2: Testing/Learning how to make Microservices

### Building a Microservice on Docker Desktop
- Make a simple microservice that says a message and run it on Docker
  - install flask through the terminal (pip install flask)
  - make a serviceA.py say a message using jsonify
  - run the service by typing, python service.py, in the terminal
  - then can click on the link and see the message in your browser
- Adding routes
  - by adding some more code you can add routes to the links
  - then if you add /route_name at the end of the link it will do the new task
- Build and running a Container
  - cd path\to\your\project
  - docker build -t service-a
  - docker run -d -p 5000:5000 service-a
  - Check running containers. (docker ps)
  - Stopping a container. (docker stop<container_id>)

### Adding a Second Microservice
- Make a second service that works with the first
  - make sure to add the URL in a variable somewhere
    - SERVICE_A_URL = "http://127.0.0.1:5000/data"
  - need to install requests library
    - pip install requests
  - run both services at the same time and see the communication between them
    - go to http://127.0.0.1:5001/fetch to check
- Build both together on Docker
  - make a docker file for both services
    - make a new file called Dockerfile
  - build both services and run them like before
    - docker build -t service-a -f Dockerfile.serviceA_test .


## Phase 3: Deploy Microservices

### Build Two Microservices
- Develop two complex service APIs:
  - **Service A** (provides core functionality)
  - **Service B** (communicates with Service A)
- Containerize both services using Docker.
### Using the Spotify API
1. **Create a Spotify Developer Account**:
   - Visit [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
   - Create an application and obtain `client_id` and `client_secret`

2. **Install Required Library**:
   ```sh
   pip install spotipy
   ```

### Deploy the Services on Kubernetes
Steps Taken to Build & Deploy the Spotify Monthly Wrapped App
1. Created Two Microservices Using Flask
Service A handles Spotify OAuth, collects the user's desired month and year, and sends that data along with the access token to Service B.

Service B receives the data and access token, fetches the user's top Spotify tracks using the Spotify Web API (short-term range), and returns the results.

2. Configured Spotify OAuth
Registered a Spotify Developer application and obtained a Client ID and Client Secret.

Set a valid Redirect URI (http://localhost:30000/callback) in the Spotify dashboard and matched it in the application code and environment variables.

3. Created Dockerfiles for Both Services
Wrote Dockerfiles for service_a and service_b to package each microservice with its dependencies.

Used Python 3.10 slim base images for lightweight containers.

4. Built Docker Images
Configured Docker to use the Minikube daemon with eval $(minikube docker-env).

Built both services locally inside Minikube using:

bash
Copy
Edit
docker build -t spotify-service-a ./service_a
docker build -t spotify-service-b ./service_b
5. Wrote Kubernetes YAML Manifests
Created:

A ConfigMap to store Spotify credentials and redirect URI.

A Deployment and Service YAML for each microservice.

Configured:

service-a as a NodePort so it’s accessible externally.

service-b as a ClusterIP service for internal communication.

6. Deployed to Kubernetes
Applied all Kubernetes manifests using kubectl apply -f ....

Started the Minikube cluster and accessed service-a through:

bash
Copy
Edit
minikube service service-a
7. Tested the Application Flow
Logged in with Spotify via the frontend (service-a).

Provided a target month and year.

Verified that the backend (service-b) returned top track data using the user’s access token.



## Additional Notes
- Used **Chocolatey** for some installations on Windows.
- Docker took ~20 minutes to enable Kubernetes; required a restart.
- Have a working plan for coding the two microservices.
