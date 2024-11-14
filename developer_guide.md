# Step 1: Clone the repository And Open in VS Code

1. Open "Git Bash" in windows machine and type below commands to clone the code
    ```shell
    cd <working_dir>
    git clone https://github.com/TheDataFestAI/thedatafestai_web.git
    ```
2. Open the cloned repo in VS Code for Development:
    ```shell
    cd thedatafestai_web
    code .
    ```
3. Add/Modify the Code and Push to GitHub:
    ```shell
    git remote add origin https://github.com/TheDataFestAI/thedatafestai_web.git
    git remote set-url origin https://<user_name>:<access_token>@github.com/TheDataFestAI/<repo_name>.git
    
    git add .
    git commit -m <message>
    git push -u origin main 
    ```