# Snapshot
A snapshot is a point-in-time backup of a disk (not the whole VM).

- It captures only disk data.

One-line definition

Snapshot = backup of a persistent disk at a specific time

**What snapshot includes**

-  OS files (if boot disk)  
-  Application files  
-  Data inside the disk  
-  File system state

**What snapshot does NOT include**

- VM settings  
-  Machine type  
-  Network config  
-  IP address  
-  Metadata  
- Running memory (RAM)

Simple example

You have a VM with:

- Ubuntu OS  
- Nginx installed  
- App data in /var/www  

You take a snapshot of the boot disk.

Later:

- Create a new disk from snapshot  
- Attach disk to a new VM

 OS + app files come back  
VM settings you must configure again  

<img width="988" height="478" alt="image" src="https://github.com/user-attachments/assets/05424416-c59c-47c5-877f-0ae160696e5b" />

**Why snapshots are important**

1 Backup

- Accidental delete  
- Corrupted disk  
- Ransomware  

2 Disk cloning

- Copy data disk to another VM

3 Migration

- Move disk to another zone/region

**Snapshot types in GCP**

1.Standard snapshot

- Regional  
- Cheaper  
- Slower restore  

2 Instant snapshot

- Zonal  
- Very fast restore  
- Higher cost

How snapshot works (internally)

First snapshot → full copy

Next snapshots → incremental

Only changed blocks are saved
