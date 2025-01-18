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

Attached is a .ipynb file for CS Trees
Please review and help me organize it better.
Below I provided an outline of what I'm looking for as far as structure goes.

Please polish and help me remove redundancy as well as provide more accurate infor where needed.
Please review my solutions. If you feel something should change (minus documentation in the code) for whiteboard on an actual white board, please
note where the change is happening and fix.

Thank you in advanced.

## File Outline

# Title

- Intro paragraph
- Example
- Highlights

# Theory

- Explain the underlining algorithmn or data structure
- Pseudo code explanation if deemed necessary

# Problems

    - Section for actual code for various problems related to content

# Walkthrough

    - After each problem A walkthrough should be provided that maps out how the problem solution works

# Summary

    - Summarize what was learned
    - Time and space complexity

Note: I don't like how .ipynb files render dividers. So with that in mind, please no dividers should be added in the markdown lanugage

In a complete binary tree, all levels are fully filled except possibly the last level. The nodes in the last level are filled from left to right, meaning that if there are any missing nodes, they will be on the right side of the tree.

Here's a visual representation to help you understand:

Complete Binary Tree:
1
/ \
 2 3
/ \ / \
 4 5 6

Not Complete Binary Tree:
1
/ \
 2 3
/ \ \
 4 5 6

In a complete binary tree, all levels are fully filled except possibly the last level. The nodes in the last level are filled from left to right, meaning that if there are any missing nodes, they will be on the right side of the tree.

Here's a visual representation to help you understand:

In the first tree, all levels are fully filled except the last level, which is filled from left to right. In the second tree, the last level is not filled from left to right because node 6 is missing a left sibling.

- **Complete:** All levels filled except possibly the last level, which is filled from left to right.

- **Perfect:** A tree where all levels are fully filled, and all leaf nodes are at the same depth.
