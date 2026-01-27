# GCP Compute Engine VM Pricing Models

**1️⃣ On-Demand (Standard VMs)**

🔹 What it is  
- Pay per second  
- No commitment  
- Start/stop anytime

🔹 Best for

- Development & testing  
- Unpredictable workloads  
- Short-term usage

🔹 Pros

- Full flexibility  
- No upfront cost

🔹 Cons  
- Most expensive option

 Example:

     Create a VM → use it → delete it → pay only for usage

**2️⃣ Committed Use Discounts (Reserved Instances equivalent)**

🔹 What it is

- Commit to using resources for 1 year or 3 years    
- Automatically applied discount  
- No upfront payment required  

🔹 Discount

- Up to 57% for general VMs    
- Up to 70% for memory-optimized VMs

🔹 Best for

Long-running production workloads  
Predictable usage  

🔹 Pros

- Big cost savings  
- No need to reserve specific VM instances

🔹 Cons

- Commitment required

📌 Equivalent to AWS Reserved Instances

**3️⃣ Spot VMs (Preemptible VMs – earlier name)**

🔹 What it is

- Uses unused Google capacity  
- Can be terminated anytime (usually with 30s notice)

🔹 Discount

- Up to 90% cheaper

🔹 Best for

- Batch jobs  
- CI/CD workloads  
- Big data processing  
- Fault-tolerant apps  

🔹 Pros

- Extremely cheap

🔹 Cons

- Not reliable   
- Can be stopped at any time

📌 Equivalent to AWS Spot Instances
