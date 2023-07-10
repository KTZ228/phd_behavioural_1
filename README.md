# PhD study 1
## Behavioural experiment code

## Install correct version of python and dependancies
Since Python is sensitive to dependencies unexpectedly interacting with each other when one of them is updated, it is important to ensure that every member of the project is working with the same versions of each dependency.
It is good practice to do this by creating a virtual environment for each separate project, which we do using `pipenv`.

### Check version number
Only needs to be checked for some dependencies that we use for the virtual environment.

#### Python
Check which python version is installed (should be at least 3.8 for PsychoPy):
`python --version`

If a newer version of Python needs to be installed:
- Go to python.com/downloads
- Install a newer stable version
* When installing, make sure to add python to the path so that you can easily execute python commands using the command window.

#### Pip
Aside from needing pip for the use of pipenv, pip also makes installing dependencies a lot easier in the future.

Try this to see if (and what version of) pip is installed:
`pip --version`

If pip is not installed:
`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`

`python get-pip.py`

#### Pipenv
Try this to see if (and what version of) pipenv is installed:
`pipenv -h`

If not, you install it by typing the following (this is where pip comes in).
`pip install pipenv`

Define python paths for pipenv (test if this is necessary):
```
c:\Users\<username>\AppData\Roaming\Python\Python38\Site-Packages
C:\Users\<username>\AppData\Roaming\Python\Python38\Scripts
```

## Open the project and install the virtual environment
Since this is an existing project, you will have to install the dependencies described in the `Pipfile`.
This is done by specifying the path to the pipfile and the IDE will download the correct version of every dependency automatically.

When a warning saying 'no python interpreter configured' is displayed, the pipfile was not read correctly and you should try specifying it manually.