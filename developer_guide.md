# Step 1: Clone the repository And Open in VS Code -

1. Open "Git Bash" in windows machine and type below commands to clone the code:
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
    git remote set-url origin https://<user_name>:<access_token>@github.com/TheDataFestAI/thedatafestai_web.git

    git add .
    git commit -m <message>
    git push -u origin main 
    ```

# Step 2: Install the Python Packages/Dependencies -

1. Create & activate Python Virtual Environment in working directory:
    ```shell
    python -m virtualenv .venv
    .\.venv\Scripts\activate
    ```
2. Install the python dependent packages:
    ```shell
    python -m pip install --upgrade pip
    pip install -r .\requirements.txt
    ```

# Step 3: Run the code:
    ```shell
    streamlit run .\app\main.py
    ```

# Supporting Document:
1. Streamlit: https://docs.streamlit.io
2. sample streamlit web app: https://github.com/okld/streamlit-gallery/tree/main
3. Sample Streamlit Folder Structure: https://github.com/ash2shukla/streamlit-heroku/
4. Top Navbar: https://pypi.org/project/hydralit-components/
5. 
