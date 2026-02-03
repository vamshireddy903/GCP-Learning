# Kubernetes architecture

<img width="1084" height="594" alt="image" src="https://github.com/user-attachments/assets/b42d0f57-85c0-48bb-aba8-ddc62e428fda" />

Kubernetes distributed system follows a client-server architecture with two main components: the control plane(master node) and Data plane (Worker Nodes).

**Control Plane:**

- It is the brain of the Kubernetes cluster.  
- The control plane acts as the central management hub for the entire Kubernetes cluster.

**Components of the Control Plane**

**1. kube-apiserver**  

- The API server is a component of the Kubernetes control plane that exposes the Kubernetes API. The API server is the front end for the Kubernetes control plane.  
- Allows users and other components to create, read, update, and delete Kubernetes resources.

**2. etcd**

A key-value store that stores all cluster data, including configuration and state

- It maintains the current status, desired state, configuration, and metadata for all Kubernetes objects.

  **What info it stores?**
  
- **Cluster Configuration and Metadata:** Nodes, Namespaces, Resource Quotas, Cluster Roles and Role Bindings (RBAC)  
- **Workloads:** Pods, Deployments, ReplicaSets, DaemonSets, StatefulSets, Jobs, and CronJobs.  
- **Services and Networking:** Services, Endpoints, Ingress, Network Policies, and ConfigMaps.  
- **Secrets and Credentials:** Secrets and Service Accounts Tokens.  
- **Persistent Storage:** Persistent Volumes (PVs), Persistent Volume Claims (PVCs), and Storage Classes.  
- **Admission Controllers:** Admission Webhooks  
- **Autoscaling Data:** Horizontal Pod Autoscalers (HPA)  
- **API Server Configuration:** API Server Discovery Info

**3. Scheduler**

The Scheduler is a component of the Kubernetes master that is responsible for selecting the best node for the pod to run on. When a pod is created, the scheduler decides which node to run it on based on resource availability, constraints, affinity and anti-affinity specifications, data locality, inter-workload interference, and deadlines.

**4. kube-cloud-controller**

 Handles background tasks such as maintaining node health, scaling, and other cluster-wide operations

 Few Controllers:
   
- Replication Controller  
- Deployment Controller  
- Node Controller:      
- Namespace Controller  
- Ingress Controller  
- and many more…

**5. Cloud-controller-manager**

Integrates Kubernetes with cloud provider-specific APIs, managing resources like load balancers, persistent volumes, and network routes within a cloud environment.

# Worker Node Components:

**kubelet:** An agent running on each Worker Node, responsible for managing Pods and their containers, communicating with the Control Plane's API server, and ensuring the containers are running as expected.

**kube-proxy:** A network proxy that maintains network rules on nodes, enabling communication between Pods and services both within and outside the cluster. It handles network address translation (NAT) and load balancing for services.


**Container Runtime:** Software responsible for running containers, such as Docker, containerd, or CRI-O. It pulls container images and executes them within Pods.
