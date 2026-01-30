
# 1️⃣ IAM Users in GCP

IAM (Identity and Access Management) in GCP controls:  

- Who (principals like users, groups, service accounts)  
- Can do what (roles/permissions)  
- On which resources (projects, buckets, VMs, etc.)  

In short:

IAM = “Who can do what on which GCP resource?”

<img width="1064" height="542" alt="image" src="https://github.com/user-attachments/assets/07cd5674-f1dc-442c-b2e6-d9685d5d6b8b" />

** Role**

Defines what actions a principal can do.

**Basic roles (Primitive roles)**

 - Viewer → read-only   
 - Editor → read + modify  
 - Owner → full control   (Not recommended in production; too broad)

**Predefined roles (Recommended)**

- Fine-grained roles for specific services

Example:

- roles/storage.admin → full control over Cloud Storage  
- roles/compute.instanceAdmin → manage Compute Engine instances  

**Custom roles**

You can create roles with specific permissions you define.


- In GCP, you don’t create IAM users directly like in AWS.  
- Instead, you grant permissions to existing Google identities:

   - Google Accounts (like Gmail addresses)
   - Service Accounts (used by applications/services)
   - Google Workspace accounts (for organizations)

- When you assign a role in IAM, you need to specify the principal as an email (the Google identity), not just a name.
Example:
```
principal = "user:someone@gmail.com"
role = "roles/viewer"
```

# 2️⃣ Password for the principal

- GCP does not create passwords for IAM users.  
- The user you assign permissions to already has their own Google account credentials.  
- So there’s no separate password in GCP like AWS IAM users. The person logs in with their existing Google account password.  

   🔹 In AWS IAM, you can create a user with a username and password for AWS console.  
   🔹 In GCP, you cannot create a username/password for GCP console login — you always use an existing Google identity.

# 3️⃣ How to allow someone to log in to GCP Console

- You just invite their Google account and assign roles.  
- They use their own Google login to access your project according to the roles you gave.

  <img width="1045" height="343" alt="image" src="https://github.com/user-attachments/assets/ddf9f29d-5c70-4fa8-a69c-662942b8377d" />

  Principal = the identity you’re granting permissions to.

# Types of principals:

**Google Account**

- A normal Gmail or Google login  
- Example: user:someone@gmail.com  
- Used for humans accessing the console

**Service Account**

- A special account for applications or services  
- Example: serviceAccount:my-app@project.iam.gserviceaccount.com  
- Used for automation, APIs, or apps, not humans

**Google Workspace / Cloud Identity account**

- Managed accounts in your organization  
- Example: user:employee@company.com  
- Used for team members in org projects

**Groups (optional)**

- You can grant a role to a group of users  
- Example: group:devs@company.com

In GCP,

- A group is basically a collection of multiple Google Accounts (or Workspace accounts).  
- When you assign a role to a group, all members of that group automatically get the role.  
- So instead of adding permissions one by one for each user, you can just assign it to the group.

Example:  
Suppose you have 3 people:
 
- alice@gmail.com  
- bob@gmail.com  
- charlie@gmail.com  

- You create a Google Group: devs@company.com and add these 3 emails.  
- Then in IAM, you give the role:  
```
principal: group:devs@company.com
role: roles/editor
```

✅ Result: Alice, Bob, and Charlie all get editor access automatically.

# IAM Deny Policy

 - With deny policies, you can define deny rules that prevent certain principals from sing certain permission, regardless of roles they're granted  
 - Deny policies are used to implement explicit denial of access, even if other IAM policies grant access.  
 - They are particularly useful for enforcing security boundaries and ensuring that certain actions can't be performed by specific users or groups under any circumstances.  
 - IAM deny policies take precedence over allow policies. If a deny rule explicitly denies a permission to principal, that principal can't perform the action, even if other policies grant it.  
 - To view, update and delete deny policies: Deny Admin(roles/iam.denyAdmin)
 
