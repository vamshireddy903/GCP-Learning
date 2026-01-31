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

**Snapshot types**  
You can backup a disk with snapshots. The 3 types of snapshots—standard, instant, and archive—all capture the contents of a disk at a specific point-in-time.

The following are the key differences between the snapshot types:

- Retention after source disk deletion  
- Data recovery time (RTO)  
- Storage location

**Retention after source disk deletion**
An instant snapshot of a disk only exists until the source disk is deleted. Standard and archive snapshots aren't deleted with the source disk. Therefore, if you want to retain a backup of a disk after you delete the disk itself, use archive or standard snapshots.

**Data recovery time**  
The data recovery time is the length of time needed to create a new disk from a snapshot and varies by snapshot type.

- Instant snapshots offer the lowest and best recovery times.  
- Standard snapshots have faster data recovery times than archive snapshots.  
- Archive snapshots have the longest data recovery times, but offer the most cost efficient storage.

**Storage location by snapshot type**
The storage location is the zone or region where Compute Engine stores the snapshot.

- Instant snapshots are local disk backups that are stored in the same zone or region as the source disk.  
- Archive and standard snapshots are remote backups of disk data stored separately from the source disk.

**Limitations**  
- You can't change the storage location of an existing standard snapshot.   
- You can snapshot a specific disk at most 6 times every 60 minutes.   
- You can't edit the data stored in a snapshot.  
- You can't recover deleted snapshots.  
- You can create an unlimited number of standard snapshots of a given disk.  
- You can store regionally scoped snapshots only in Cloud Storage regional locations, such as asia-south1 or us-central1. You can't store regionally scoped snapshots in multi-regional locations, such as asia.  
- You can't convert a globally scoped snapshot to a regionally scoped snapshot. You must create a new snapshot with the appropriate scope.  
- You can't create regionally scoped snapshots with source disks that are protected by a customer-supplied encryption key (CSEK).  
- Regionally scoped snapshot names are unique only within a region. You can have regionally scoped snapshots with the same name in different regions.  
