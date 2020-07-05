# PythonTemplate
A template layout of a Python project

1. Create repository in github - No additional files
2. Navigate to desire local repository location
3. ```git clone https://github.com/marmstr93ng/___.git``` - Refer to the url of the github repo
4. Download Python template files and place in the local directory
5. ```git add .``` - Adds all files
6. ```git commit -m "first commit"``` - Commit all added files
7. ```git push -u origin master``` - Push to the github repo

All git commands entered through git bash (Right click on Repo and click "Git Bash Here").

## Virtual Enviroments (Venv)
Pipenv has been depricated in all my projects and I have reverted back to Venv which is part of the standard library (I try and keep to the standard lib as much as possible). To overcome the shortfall of having to manually keep the requirements up-to-date, use [GitRequire](https://github.com/marmstr93ng/GitRequire.git) to automatically update the requirements.txt file.

1. ```python -m venv venv```
2. ```cd venv/Scripts```
2. Add wheel ```python -m pip install --upgrade pip setuptools wheel```
3. To enter the virtual enviroment ```activate```
4. To exit the virtual enviroment ```deactivate```

[Venv Tutorial](https://chriswarrick.com/blog/2018/09/04/python-virtual-environments/)

## Visual Studio Code Tips

- Use a custom virtual enviroment by selecting it with the command ```python: Select Interpreter```
- Open intergrated terminal ```ctrl+'``` or View > terminal

## Setup Git:
1. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
2. ```git init``` - creates an empty git repository in the local directory (.git subdir with necessary metadata)
3. ```git config --global user.name "<name>"``` - Change the user's name
4. ```git config --global user.email "<email>"``` - Change the user's email address
5. Setup SSH if necessary (see below)

### Setup SSH Key
```Generate SSH Keyssh-keygen -t rsa -b 4096 -C "your_email@example.com"```
- On "Enter a file in which to save the key," press Enter. This accepts the default file location.
- At the prompt, type a secure passphrase.

#### Add SSH Key to SSH-Agent
- Ensure ssh-agent is enabled: ```eval "$(ssh-agent -s)"```
- Add your SSH key to the ssh-agent: ```ssh-add ~/.ssh/id_rsa```

#### Add SSH key to Github Account
- Copy the SSH key to your clipboard. ```clip < ~/.ssh/id_rsa.pub```
- In the top right corner of any page, click your profile photo, then click Settings
- In the user settings sidebar, click SSH keys.
- Click New SSH key.
- Name and add Key

#### Test SSH Connection
```ssh -T git@github.com```

# Other Links
1. [Documenting with Sphinx](http://www.sphinx-doc.org/en/stable/tutorial.html)
2. [Unit tests](https://docs.python.org/3.5/library/unittest.html)
3. [Packages](https://uoftcoders.github.io/studyGroup/lessons/python/packages/lesson/
