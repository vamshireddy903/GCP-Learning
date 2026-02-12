# ✅ Practical Task: Nightly Log Processor Job  
# 🎯 Scenario:

You have an application generating logs.

**Every night:**
- Read a log file  
- Count number of lines  
- Save result to output file  
- Exit

This is a perfect Cloud Run Job use case because:

- It runs once  
- Completes task  
- No HTTP needed  
- Batch-style processing

🚀 What We’ll Build

A Python container that:

- Reads input.txt  
- Counts lines  
- Writes result to output.txt  
- Prints result  
- Exits

# First Clone the repo to your terminal

# Build & Push Image

**1. Make sure you are logged in:**
```
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

**2. Enable APIs (if not enabled):**

     gcloud services enable run.googleapis.com artifactregistry.googleapis.com


**3. Build & push:**

Make sure you have created artifact registry in the gcp

    docker build -t asia-south1-docker.pkg.dev/vamshi-project-486305/demo:v1 .

**4. Push image to the artifact registry**

    docker pus asia-south1-docker.pkg.dev/vamshi-project-486305/demo:v1

