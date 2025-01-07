# Python Virtual Environment (venv) Guide

## Creating a Virtual Environment
Create a virtual environment in your project directory:
```bash
python3 -m venv venv
```
> Note: First `venv` is the module name, second is the directory name (customizable).

## Activating the Virtual Environment

### macOS/Linux:
```bash
source venv/bin/activate
```

### Windows:
```bash
# In Command Prompt
venv\Scripts\activate.bat

# In PowerShell
venv\Scripts\Activate.ps1
```

## Managing Dependencies

### Installing Packages
```bash
pip install <package-name>
```

### Saving Dependencies
```bash
pip freeze > requirements.txt
```

### Installing from Requirements
```bash
pip install -r requirements.txt
```

## Deactivating and Cleaning Up

### Deactivate Environment
```bash
deactivate
```

### Delete Environment
```bash
rm -rf venv
```

## Version Control
Add to `.gitignore`:
```
venv/
```
