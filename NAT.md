# What is Cloud NAT in GCP?

Cloud NAT (Network Address Translation) lets private VMs (no public IP):

- Access the internet (outbound only)  
- Without being reachable from the internet

👉 This is exactly what we want for private subnets.

**Key points about Cloud NAT**

- It is a managed service (no VM to maintain)  
- Works with Compute Engine VMs  
- Uses Cloud Router  
- Outbound traffic only (no inbound connections)

<img width="514" height="418" alt="image" src="https://github.com/user-attachments/assets/e1edb409-59f5-4bcc-b1e3-f0b06c94845e" />

- VM has only private IP  
- Cloud NAT uses public IPs on behalf of the VM  
- Internet never sees the VM’s private IP

**Why we use Cloud NAT**  
- Secure outbound internet access  
- No public IP exposure

Required for:  
 - OS updates  
 - Pulling Docker images  
 - Calling external APIs  
