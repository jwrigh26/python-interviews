A venv (short for virtual environment) in Python

Create a Virtual Environment: Run the following command in your project directory:
python3 -m venv venv

The first venv is the module name.
The second venv is the directory name where the virtual environment will be created (you can name it anything, but venv is a common convention).

Activate the Virtual Environment:
MAC OS
source venv/bin/activate
Windows
venv\Scripts\activate

 venv/Scripts/activate.bat //In CMD
 venv/Scripts/Activate.ps1 //In Powershel

Once activated, your shell prompt will change to show the environment name (e.g., (venv)), indicating the virtual environment is active.

Install Dependencies in the Virtual Environment: Use pip to install packages while the virtual environment is active:
pip install <package-name>

Deactivate the Virtual Environment: To exit the virtual environment, simply run:
deactivate

Delete a Virtual Environment: If you no longer need it, you can delete the venv directory:
rm -rf venv

Use a .gitignore file to exclude the venv directory from your version control system (e.g., Git):
venv/

Use pip freeze > requirements.txt to save dependencies for sharing or reproducing the environment:
pip freeze > requirements.txt

Reinstall dependencies using: 
pip install -r requirements.txt
