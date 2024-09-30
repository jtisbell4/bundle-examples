# GitFlow using Databricks Asset Bundles
This is an extension of two great resources available on this topic: [Databrick's bundle examples repo](https://github.com/databricks/bundle-examples) and [@ajalisatgi's dabs-gitflow repo](https://github.com/ajalisatgi/dabs-gitflow/tree/main)

## Overview

This project can be used to bootstrap Databricks deployments that require implementing a GitFlow branching model. Databricks Asset Bundles (DABs) package the relevant Databricks assets together and deploy them across different workspaces. GitHub Actions workflows automate the constructs as they apply to the GitFlow branching model and invoke DABs for deployments. 

The following image represents the end-to-end implementation of the GitFlow branching model for managing Databricks deployments.
![image](https://github.com/user-attachments/assets/ae25ba29-2bb1-4152-8259-76f4fe1895ae)

    
## Prerequisites
Following are the pre-requisites that are needed to use the code in this repository to manage deployments for your specific Databricks workspaces.
* Clone this repository 
* Provision 3 distinct Databricks workspaces: `dev`, `staging` & `prod`
* Create two distinct service principals via the account console for the `staging` and `prod` Databricks workspaces respectively
* Assign the service principals created in the previous step to the respective `staging` and `prod` workspaces
* Create an Oauth secret for both Service Principals and make a note of the the `Client ID` and `Secret`  
* Update the `databricks.yml` file in the root of this repository with the following details pertaining to your environment:
  * workspace host for `dev`, `staging` and `prod` Databricks workspaces
  * service principal name for `staging` and `prod` service principals
* Create GitHub environments for `staging` and `prod`
* Create the following secrets in both `staging` and `prod` GitHub Environments:
  * `DATABRICKS_CLIENT_ID`
  * `DATABRICKS_CLIENT_SECRET`
* Create `DATABRICKS_HOST` as a variable in both `staging` and `prod` GitHub Environments
  
---

## Standard Release Process
The following image represents the steps involved in deploying a Standard Release
![image](https://github.com/user-attachments/assets/e50ef525-60f4-4680-abb2-38ec7ea90e89)


---
## Hotfix Release Process
The following image represents the steps involved in deploying a Hotfix Release
![image](https://github.com/user-attachments/assets/73cbdd53-84b8-43ae-bfb5-2b944a3c7e65)

## Running Tests
To run tests locally, it is recommended that you use VSCode as your IDE. This is because the Databricks VSCode extension and Databricks Connect make it very easy to connect to your interactive cluster, run tests, and debug using the built-in VSCode Python debugger. Please reference the [documentation](https://docs.databricks.com/en/dev-tools/vscode-ext/index.html) to get started. The steps to debug are below:
1. Create local Python environment:
   ```bash
   conda create -n my_env python=3.11
   conda activate my_env
   ```
2.  Install development dependencies:

3. Set `DATABRICKS_HOST` and `DATABRICKS_CLUSTER_ID` environment variables. You will also need `DATABRICKS_TOKEN` if you are using PAT authentication.
> [!TIP]
> The Databricks VSCode extension automatically adds a `.databricks.env` file to your local repo containing the environment variables associated with the workspace and cluster you are currently connected to. You can add the following bash script to your shell profile to automically add these environment variables at session start-up:
> ```bash
> if [[ "$TERM_PROGRAM" == "vscode" && -f ".databricks/.databricks.env" ]]; then
>   source .databricks/.databricks.env && \
>   echo "✅ loaded .databricks.env"
> fi
> ```
4. Run tests:
   ```bash
   pytest
   ```
