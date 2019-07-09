# create
Autonomously create project directories and GitHub repos from the CLI.

## Description
Inspired by Kalle Hallden's 'One Day Builds: Automating My Projects With Python'. This is my implementation of his project, Some things have been altered such as the implementation of a configuration file to determine if the repo created is private or public and to also handle 2FA upon logging in to GitHub. Currently this project is only functional on Windows machines.

## Requirments
- Python 2.7.X
- Visual Studio Code
- Windows OS

## Installation
1. Complete the 'config.json' file with the required fields. When providing the project directory please use the following format: C:\\Users\\name\\documents\\github_projects 
2. Replace the rem lines in 'create.bat' with the respective paths and GitHub origin. 
3. After completeing step 2, drag 'create.bat' to your System32 folder located typically at path C:\Windows\System32

## Usage
This script, when implemented correctly, will allow the user to create a new project directory and GitHub repository autonomously from the command line. After doing this, the script will then proceed to open up the newly created directory in Visual Studio Code.

After the steps above have been completed, the user should be able to use the command as follows from any directory on their machine:
>create project_name

## What I Learnt?
- Automation of CLI inputs using batch (.bat) files.
- Browser automation of user inputs.
- Reaffirmed Python skills.
