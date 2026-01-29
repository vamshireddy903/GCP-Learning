# What is a Machine Image in GCP?

A Machine Image is a full snapshot of a VM.

**It captures:**

- ✅ Boot disk (OS + installed software)  
- ✅ All attached data disks  
- ✅ VM metadata  
- ✅ Network interface settings  
- ✅ Service account & scopes  
- ✅ Instance labels  

👉 In short: “Exact copy of a VM at a point in time.”

One-line definition

Machine Image = backup + template + restore point of a VM

**Why Machine Image exists**

Use it when you want to:

- Recreate the same VM exactly  
- Recover a VM after deletion  
- Clone production VM → test VM  
- Migrate VM to another project/region  
- Machine Image vs Snapshot vs Instance Template

This is VERY important 👇

**Machine Image**

- Full VM copy  
- Can recreate identical VM  
- Includes disks + config  
- Heavy but complete  

Use when: backup / restore / cloning

**Snapshot**

- Disk-level only
- No VM config
- OS/data only

Use when: disk backup

**Instance Template (MIG uses this)**

- Blueprint, not backup  
- No running state  
- No data inside VM  
