# PhD study 1
## Behavioural experiment code

## Install correct version of python and dependancies
Since Python is sensitive to packages unexpectedly interacting with each other when one of them is updated, it is important to ensure that every member of the project is working with the same versions of both Python and each package.
It is good practice to do this by creating a virtual environment for each separate project, which we do using `pyenv` and `pipenv`.

## Managing Python versions

### Start by installing Homebrew (similar to pip, macos only)
We will start by installing the package manager Homebrew so that we can install the necessary packages in subsequent steps.
Go to the [Homebrew website](https://brew.sh) and input the command into your terminal window.
After it is finished installing, it will present one or two commands in the terminal that you need to run to add Homebrew to the terminal path. If you skip this step Homebrew cannot be found by the terminal, meaning that you can't use the package manager.

* Have not been able to test a suitable replacement for windows.

### Setup pyenv
Install pyenv using brew:
`brew install pyenv`
* Note that pyenv cannot be installed using pip

The following commands needs to be executed so that the system wide python directory contains aliasses to the default pyenv.
```
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi

export PYENV_ROOT="$HOME/.pyenv/shims"
export PATH="$PYENV_ROOT:$PATH"
export PIPENV_PYTHON="$PYENV_ROOT/python"
```

#### Installing the desired python version
Check what version of Python is described in the pipfile found in the project folder. We will be installing the same version.
Let's say the used Python version is 3.8.18.

We will install it using the command: `pyenv install 3.8.18`
To see what python versions are installed in pyenv you can type: `pyenv versions`

#### Activate pyenv on startup of new terminal
Type the following into the terminal for further instructions:
`pyenv init`
It probably warns you to copy something akin to the following code block into the '.zprofile' file:
```
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```
You can find this file in the home directory (unhide using command + shift + period).
Simply add the set of commands to the end of it and save the file.
Any new terminal window should now be able to load the correct local and global python versions.

#### Set a global python environment
If you haven't installed python before you will need to set one as the system default.
This can be done using: `pyenv global 3.8.18`
Check if this is executed correctly by typing `python --version`
* You can use any version of python installed in pyenv.

#### Set a local python environment for each project
The main reason for using this is obviously to set a python version for each project.
This can be done using the following:
Navigate to the project folder: `cd ~/Documents/python_tests`
Then, set the local python environment using `pyenv local 3.8.18`

## Managing package versions

### Pipenv
Try this to see if (and what version of) pipenv is installed: `pipenv -h`.

If not, you install it by typing the following (this is where pip comes in): `brew install pipenv`.

Define python paths for pipenv (test if this is necessary):
```
C:\Users\<username>\AppData\Roaming\Python\Python38\Site-Packages
C:\Users\<username>\AppData\Roaming\Python\Python38\Scripts
```

### Installing the virtual environment and its packages using pipenv
Since this is an existing project, you will have to install the packages described in the `pipfile`.

One way to do this is by navigating to the folder using the terminal command `cd ~/Documents/python_tests`.
Subsequentially, you will need to create the environment using `pipenv install --python 3.8.18`.
These steps are the same for when you create a new project or install the packages of an existing project, so you can also use this command for your own work.
* Note that if you don't specify the Python version installed in the folder, pipenv will default to the global environment.

## Opening the project with the correct interpreter

### Using PyCharm or DataSpell
Open the project first.
Then, you will need to select the interpreter manually.
Go to the interpreter menu (bottom right) and add a new interpreter.
Select the pipenv environment. Use the base interpreter and leave the 'install packages from pipfile' option enabled.
Next, check whether the correct version of python and its packages are installed in the 'python interpreter' menu. the Python version will be listed at the top.

* Note that when having installed new packages into the pipenv, the interpreter still needs to be updated in PyCharm/DataSpell. This can be done by typing `pipenv update` into the terminal in PyCharm/DataSpell itself.

### Using Sublime Text
Sublime text is the program that is used to run our python experiments on the lab PC's.
Here, we will set up a build system (interpreter) for Sublime that links directly to your project.

#### Installing package control
We need this to make new build files.
In Sublime, go to: Tools > Command Palette.
Type `Install Package Control` and press enter.

#### Make build file
An example of a build file is included in the documentation folder, you need to change the location on `cmd` to your environment's Python alias.
To find the location on your pc, go to the location of your project folder: `cd Documents/python_tests` and activate your environment by typing `pipenv shell`.
This will also present the location of the activation script (for me: `/Users/kenneth.van.der.zee/.local/share/virtualenvs/python_tests-cAsClIPH/bin/activate`).
You then copy most of this to the build file but replace the word `activate` at the end with `python`.
This should result in `/Users/kenneth.van.der.zee/.local/share/virtualenvs/python_tests-cAsClIPH/bin/python`.

The filename will be used in the build menu so make sure you give it a name linked to the project.

#### Move the build file
In order for Sublime to access it, build files have to be places in the dedicated folder.
To find this folder, go to: Tools > Build System > New Build System... 
A new build file will be created that we are not going to use other than to determine the default save location of build files.

You can find this location by trying to save this file and copying the folder location to the finder/explorer (the newly created file can be closed without saving).

Move the file you changed in the previous step to that folder.

#### Select and test build file
If done correctly you should be able to select the build file in the following menu:
Tools > Build System > phd_behavioural_1_environment

Create a simple hello world function to see if the build file was adjusted correctly.
(If the build file does not show up in the build system list, it is not placed in the correct folder or the extension might be missing)

# Happy coding!

## External links
Additional documentation on how to install or update packages in your virtual environment [pip tutorial](https://jcutrer.com/python/pipenv-pipfile).
[Additional documentation on pyenv and pipenv](https://www.rootstrap.com/blog/how-to-manage-your-python-projects-with-pipenv-pyenv)