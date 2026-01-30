# Migration
In the world of Google Cloud Platform (GCP), migration is the process of moving your data, applications, and workloads from an "on-premises" environment (your own physical servers) or another cloud provider (like AWS or Azure) into Google’s infrastructure.

- 🖥️ On-premises data center  
- ☁️ Another cloud (AWS, Azure, etc.)  
- 🧪 Old VM / legacy environment inside GCP itself

**What can be migrated to GCP**  
 **1️⃣ Compute (Servers / VMs)**

Moving physical servers or virtual machines into GCP.

**Examples:**

- On-prem VMware → GCE VM  
- AWS EC2 → GCE VM  

**GCP tools:**

- Migrate to Virtual Machines
- VM import/export

**2️⃣ Applications**

Moving applications running on those servers.

Types:

- Lift & Shift – move as-is (no code change)   
- Re-platform – small changes (e.g., move to managed DB)  
- Re-architect – redesign using cloud-native services

**Examples:**

- Monolithic app → GKE (Kubernetes)  
- Java app → App Engine / Cloud Run

**3️⃣ Databases & Data**

Moving data from existing databases or storage.

**Examples:**

- MySQL on EC2 → Cloud SQL  
- On-prem DB → Cloud Spanner

**GCP tools:**

- Database Migration Service  
- Storage Transfer Service  
- Transfer Appliance (for huge data)

**4️⃣ Networking**

Re-creating your network in GCP.

Includes:

- VPCs  
- Subnets  
- Firewall rules  
- VPN / Interconnect

**5️⃣ Identity & Access**

Moving or integrating users and permissions.

Examples:

- LDAP / AD → Cloud Identity  
- IAM role mapping from AWS/Azure → GCP IAM roles

**Why do companies migrate to GCP?**

💰 Lower cost / better pricing for some workloads  
- Switching from capital expenses (buying hardware) to operational expenses (pay-as-you-go).

🤖 AI / ML services (BigQuery, Vertex AI)
- Innovation: Getting instant access to Google’s AI and BigQuery data analytics tools.

📈 Auto-scaling & managed services  
- Scalability: Handling 10 users or 10 million users without buying new servers.

# Migration Process

Migrate to Virtual Machines lets you migrate (Lift and shift) your virtual machines (VMs), with minor automatic modifications, from your source environment to Compute Engine. Migrate to Virtual Machines uses data replication technology which continuously replicates disk data from the source VMs to Google Cloud without causing any downtime on the source. You then create VM clones from replicated data for testing and perform predictable VM cut-over to your final workloads running on Google Cloud.


