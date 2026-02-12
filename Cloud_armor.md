# Cloud Armor

Cloud Armor in Google Cloud Platform (GCP) is a security service that protects your applications from attacks on the internet.

**It works mainly with:**

- HTTP(S) Load Balancer  
- Cloud CDN  
- Applications running on GKE, Compute Engine, App Engine
  
**🔐 What Cloud Armor Does**

**1️⃣ Protects from DDoS attacks**  
Stops large amounts of fake traffic trying to crash your website.

**2️⃣ Web Application Firewall (WAF)**
- Protects from common web attacks like:  
- SQL Injection  
- Cross-site scripting (XSS)  
- Remote code execution  
- OWASP Top 10 attacks  

**3️⃣ IP Filtering**  
You can:  
- Allow specific IP addresses  
- Block specific IPs  
- Block entire countries  

**Example:**  
Block traffic from a suspicious IP range.

**4️⃣ Rate Limiting**  
- Limits how many requests a user can send.  
  **Example:**
- Only 100 requests per minute per IP.
  
**🏗 How It Works (Simple Flow)**  
```
User → Load Balancer → Cloud Armor checks rules → If allowed → Backend (VM / GKE / App)
If rule fails ❌ → Request is blocked before reaching your app.

```
**💼 Business Perspective**   

- Protects website uptime  
- Prevents financial loss from attacks  
- Maintains customer trust  
- Reduces security risk
  
**🎯 Client Perspective**

- Client doesn't see Cloud Armor directly.  

**They just experience:**  
- Secure website  
- Less downtime  
- Safe transactions
  
**🔥 Example Scenario**  

**If you host an e-commerce app on GKE:**    
**Without Cloud Armor:**

- Hackers can send SQL injection  
- Bot traffic can overload app  

**With Cloud Armor:**
- Malicious requests blocked at edge  
- Only clean traffic reaches your app  
