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

# Connect to Other Resources:
1. **MongoDB with VScode:**
    <br>Ref: https://www.mongodb.com/docs/mongodb-vscode/playgrounds/
    1. Click on "View" and open "Command Palette."
    2. Search "MongoDB: Connect" on the Command Palette and click on "Connect with Connection String."
    3. Paste your connection string into the Command Palette.
        ```
        mongodb+srv://<user_name>:<db_password>@<cluster_name>.xmoc8.mongodb.net/
        ```
    4. Click “Create New Playground” in MongoDB for VS Code to get started
2. Mongodb Atlas with Compass:
    1. installCompass: https://downloads.mongodb.com/compass/mongodb-compass-1.45.0-win32-x64.exe
    2. copy: mongodb+srv://<user_name>:<db_password>@<cluster_name>.xmoc8.mongodb.net/
3. Backblaze Python SDK -
    1. https://b2-sdk-python.readthedocs.io/en/master/quick_start.html#by-name

# Step 3: Run the code:
    ```shell
    streamlit run .\app\streamlit_app.py
    ```

# Supporting Document:
1. Streamlit: https://docs.streamlit.io
2. sample streamlit web app: https://github.com/okld/streamlit-gallery/tree/main
3. Sample Streamlit Folder Structure: https://github.com/ash2shukla/streamlit-heroku/
4. Top Navbar: https://pypi.org/project/hydralit-components/
5. emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
6. https://materializecss.com/icons.html

# Streamlit App Development Ref: 
1. https://docs.streamlit.io/get-started/tutorials/create-an-app
2. https://docs.streamlit.io/develop/concepts/multipage-apps
	1. https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation
	2. https://docs.streamlit.io/develop/concepts/multipage-apps/pages-directory
