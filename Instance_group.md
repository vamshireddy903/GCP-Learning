# What is an Instance Group?

An Instance Group is a collection of virtual machine (VM) instances that are managed together as a single unit.

👉 Instead of managing VMs one by one, you manage them as a group.

**Used for:**

- Auto scaling  
- Load balancing  
- High availability  
- Rolling updates

**🔹 Types of Instance Groups (GCP)**  
**1️⃣ Managed Instance Group (MIG)**

VMs are identical and controlled by a template.

**Features:**

- Auto scaling (scale in/out)  
- Auto healing (replace unhealthy VMs)
- Rolling updates  
- Easy integration with Load Balancer  

Example:

- Web application servers  
- Microservices

👉 You define:

- VM image  
- Machine type   
- Startup script  

**2️⃣ Unmanaged Instance Group**

VMs are different and managed manually.

**Features:**   
- No auto scaling  
- No auto healing  
- No rolling updates  

**Use case:**

Legacy applications
VMs with different configs

**🔹 Instance Group Scope**  
📍 Zonal Instance Group

VMs are in one zone  
Simple and cheaper  
Zone failure = downtime

**Regional Instance Group**

- VMs spread across multiple zones
- High availability
- Slightly higher cost

**Why use Instance Groups?**

Without instance groups:

- Manual scaling
- Manual recovery
- High downtime risk

With instance groups:  
- Automatic scaling  
- Self-healing  

Load-balanced traffic

Cost optimization
