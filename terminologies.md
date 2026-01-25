# 1️⃣ Elasticity  
Meaning:
👉 Ability to automatically increase or decrease resources based on demand.

In cloud terms:  
- Traffic ↑ → servers scale up  
- Traffic ↓ → servers scale down  
- You pay only for what you use

Example:  
E-commerce site during sale

- Normal day → 2 EC2 instances  
- Sale day → 20 EC2 instances  
- After sale → back to 2
  
📌 Elasticity = scale up & down quickly

**2️⃣ Resilience**  
Meaning:  
👉 Ability of a system to recover quickly from failures and continue working.

In cloud terms:
- If one component fails, system bounces back  
- Focus is on recovery, not zero failure
  
Example:  
- One EC2 instance crashes  
- Load balancer routes traffic to healthy instance  
- Auto Scaling launches a new instance
  
📌 Resilience = fall down → get back up fast

**3️⃣ Compliance**  
Meaning:  
👉 Following laws, regulations, and standards.

In cloud terms:  
- Data security & privacy rules  
- Industry standards  

Examples:  
- GDPR – EU data privacy  
- HIPAA – healthcare data  
- PCI-DSS – credit card data  
- ISO 27001
- 
📌 Compliance = obey rules & regulations

**4️⃣ High Availability (HA)**  
Meaning:  
👉 System is available most of the time, with minimal downtime.

In cloud terms:  
- Services run across multiple Availability Zones  
- No single point of failure

Example:  
- Web app deployed in 2 or 3 AZs  
- If AZ-1 goes down → AZ-2 serves traffic
- 
📌 High Availability = service stays UP

**5️⃣ Fault Tolerance**  
Meaning:  
👉 Ability to continue operating even when a failure occurs, with no interruption.

Difference from HA:  
HA → small downtime allowed  
Fault tolerance → zero downtime  

Example:  
- Two databases running in active-active  
- One fails → other instantly takes over
- 
📌 Fault tolerance = fail but users don’t notice

**6️⃣ Disaster Recovery (DR)**  
Meaning:  
👉 Ability to restore systems after a major disaster.  

In cloud terms:  
- Handles big failures:  
- Region outage  
- Data center fire  
- Natural disasters
  
DR Strategies:  
- Backup & Restore  
- Pilot Light  
- Warm Standby  
- Multi-Region Active-Active  

Example:  
- Primary region fails  
- App is restored in another region using backups
  
📌 Disaster Recovery = come back after catastrophe

🔑 Quick Comparison Table  
    
     ````
     Term                                 Focus
     Elasticity                       Scaling resources
     Resilience                       Quick recovery
     Compliance                       Legal & regulatory
     High Availability                Minimal downtime
     Fault Tolerance                  Zero downtime
     Disaster Recovery                Large-scale failure recovery
    ```
# Regions
A region is a specific geographical location where GCP resources can be deployed. Each region is an independent geographic area, such as us-east1 (South Carolina) or europe-west1 (Belgium).

Key characteristics:

- Regions are completely independent of each other  
- Each region has multiple zones (typically 3 or more)  
- Helps with data locality, compliance, and latency optimization  
- Resources in different regions are isolated for disaster recovery

**Zones**  
A zone is a deployment area within a region, essentially a single data center or cluster of data centers. Zones within a region are identified by adding a letter suffix, like us-east1-a, us-east1-b, us-east1-c.

Key characteristics:

- Zones within a region have high-bandwidth, low-latency network connections    
- Each zone is isolated from failures in other zones  
- Deploying resources across multiple zones provides high availability within a region    
- Some resources are zonal (exist in a specific zone), while others are regional  

**Common Use Patterns**  
**High availability within a region:** Deploy resources across multiple zones in the same region. For example, running VM instances in both us-central1-a and us-central1-b protects against zone-level failures.
**Disaster recovery across regions:** Deploy critical workloads in multiple regions to protect against region-level outages.
**Latency optimization:** Choose regions closest to your users to minimize network latency.

**Resource Types**

**Zonal resources:** Compute Engine instances, persistent disks (must specify a zone)    
**Regional resources:** Cloud Storage buckets, Cloud SQL instances (automatically replicated across zones in a region)  
**Multi-regional resources:** Some services like Cloud Storage offer multi-region deployment for maximum availability  
**Global resources:** Services like Cloud Load Balancing, Cloud CDN, and IAM operate globally
