# How to set up Sublime text
Sublime text is the program that is used to run our python experiments on the lab PC's.
But before Sublime can run python code using our own virtual environment, a couple of files need to be changed.

## Installing package control
In Sublime, go to:
Tools > Command Palette
Type `Install Package Control` and press enter

## Make build file
An example of a build file is included in this folder, this needs to be copied to the location of build files in Sublime.
To find this folder, go to:
Tools > Build System > New Build System...

Immediately try to save this file and copy the folder location to the finder/explorer (the newly created file can be closed without saving).
Move the `sublime-build` file to that folder.

Open it and edit the file so that it points to the location of the virtual environment.

## Select and test build file
To select the build file, fo to:
Tools > Build System > phd_behavioural_1_environment

Create a simple hello world function to see if the build file was adjusted correctly.
(If the build file does not show up in the build system list, it is not placed in the correct folder or the extension might be missing)