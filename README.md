# Project 5 — Login Form Validation

    A responsive HTML/CSS login page with JavaScript username/password validation, Git source management, a Docker image, and Selenium browser tests.

    ## Requirements
    - Git and a GitHub account
    - Docker Desktop (Linux containers enabled)
    - For Selenium projects: Python 3.10+ if running tests locally, or Docker Compose
    - For Kubernetes projects: kubectl and Minikube (or another Kubernetes cluster)
    - Jenkins is required for the CI/CD exercise

    ## Run locally
    Follow the project-specific instructions below.

    ## Git and GitHub
    Create an empty GitHub repository, then run these commands from this project folder:

    ```powershell
    git init
    git add .
    git commit -m "Initial project"
    git branch -M main
    git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
    git push -u origin main
    ```

    Replace the remote URL with your own repository URL. Do not commit passwords, tokens, or other secrets.


    ## Run and test with Docker Compose
    ```powershell
    docker compose up --build --abort-on-container-exit tests
    ```
    Open `http://localhost:8085` to view the page. Demo login: `student` / `Student@123`.

    To run the app alone:
    ```powershell
    docker build -t login-validation .
    docker run --rm -p 8085:80 login-validation
    ```

    Selenium tests cover valid login, empty username, invalid username format, short password, and incorrect credentials. The Compose test service uses Selenium Standalone Chrome.


    ## Important note
This is a front-end academic demonstration. The demo credential is visible in JavaScript and is not suitable for real authentication. A real system must validate credentials on a secure server.

    ## Submission checklist
    - Source code is present in your GitHub repository.
    - Application runs locally.
    - Docker image builds and container starts (where required).
    - Selenium tests pass (where required).
    - Jenkins pipeline is configured (where required).
    - Kubernetes Deployment and Service are running (where required).
