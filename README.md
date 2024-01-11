# Hackathon

## Overview

This repository contains the source code for Hackathon, which is hosted on github. The development workflow involves two main branches: `main` and `dev`. Changes are developed and tested in the `dev` branch before being merged into `main`. The production deployment of the `main` branch is hosted on Stalingo.

## Infrastructure

### Version Control System (VCS)

The project uses github as its version control system. The main branches are:

- `main`: Represents the stable version of the application.
- `dev`: Development branch where new features and bug fixes are implemented.

### Deployment Platform

Stalingo is used for deploying and hosting the application. 

### Continuous Integration/Continuous Deployment (CI/CD)

 is used for automating the build and deployment processes. The CI pipeline is triggered on each push to the `dev` branch. It includes the following steps:

1. **Build**:
2. **Deploy to Staging**: 
3. **Automated Tests**: 
4. **Deployment to Production**: 

### Development Workflow

1. Developers clone the repository and create feature branches from the `dev` branch.
2. Code changes are made and tested in the feature branches.
3. Pull requests are submitted to merge changes into the `dev` branch.
4. Continuous Integration tests are automatically run on the `dev` branch.
5. Once changes are validated, a pull request is created to merge into the `main` branch.
6. The `main` branch is automatically deployed to the staging environment for further testing.
7. Upon successful testing in the staging environment, changes are manually promoted to the production environment.


