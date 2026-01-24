# GCP Resource Hierarchy

Resource hierarchy is the way GCP organizes all your resources (projects, VMs, storage, databases, etc.) in a tree-like structure, from top-level organization down to individual resources.

It defines:  
- Who owns what (projects, folders, resources)  
- How permissions are inherited across resources

**Why Resource Hierarchy Exists**

**Centralized Management**

- You can manage all resources, users, and permissions from one place (Organization or Folder).  
- Example: Add a new employee to the devs group and give access to all dev projects at once.

**Permission Inheritance**

- IAM roles assigned at higher levels automatically apply to lower levels, so you don’t have to assign roles for every resource individually.  
- Example: Giving Viewer role at Organization → all projects and resources inherit it.

**Organization and Clarity**

- Helps structure resources by teams, departments, environments.  
- Example: Folders for Engineering, HR; Projects for Dev, Prod.

**Security and Access Control**

- Easier to enforce security rules.  
- Example: Limit Billing Admin role only at Organization, not at individual projects.

**Scalability**

- As your company grows, hierarchy makes it easy to add projects, teams, and resources without breaking access rules.

**Organization (Top level)**

- Represents your company or organization in GCP.  
- Example: mycompany.com  
- You get an Organization node only if you have a Google Workspace or Cloud Identity account.  
- All resources below this node belong to this organization.  
- IAM roles assigned at this level are inherited by all projects and resources under it.  
- Example roles: Organization Admin, Billing Admin.

# Folder (Optional)

- Helps group projects together under the Organization.  
- Useful for departments or teams.  
- Example: Engineering folder, HR folder.  
- Permissions assigned to a folder are inherited by all projects inside it.  
- You can have nested folders if needed.  

**Project**

- Core unit of GCP resources.  
- Every resource (VM, Storage bucket, DB, etc.) must belong to a project.  
- Example: dev-project, prod-project.  
- IAM roles at the project level apply to all resources in that project unless overridden at a lower level.

**Resource (Bottom level)**

- Actual GCP services or resources, like:  
    - Compute Engine VM  
    - Cloud Storage bucket  
    - BigQuery dataset    
    - Pub/Sub topic  
- Permissions can also be assigned at the resource level, overriding inherited roles if necessary.

<img width="581" height="490" alt="image" src="https://github.com/user-attachments/assets/0b5c38f2-b997-4c4b-bb18-f4cc3c58949e" />

<img width="1232" height="696" alt="image" src="https://github.com/user-attachments/assets/33eb0b94-6878-4c09-b957-5357ee1c5c63" />

**Analogy**

Think of GCP resource hierarchy like a company org chart:
```
CEO (Organization)
 └── Departments (Folders)
      ├── Teams (Projects)
      │    └── Employees (Resources)
```

- Assign a role at the CEO level → everyone under it inherits.  
- Assign a role to a team → only that team gets it.  
