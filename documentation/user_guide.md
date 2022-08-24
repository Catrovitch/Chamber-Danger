# User Guide

## Installing

To install the program you can either clone the project or download the latest release.

### Cloning the project

1. Go to the project's Github page, se link [Chamber-Danger](https://github.com/Catrovich/Chamber-Danger). 

2. Click the green "Code" button at the upper right corner. This will drop down a menu where you should choose "HTTPS". Copy the "https://..." url to your clipboard.

[](./pictures/code_button.png)
Here you can see the button which needs to be pressed.
To clone the project open your terminal and  


3. Open Terminal

4. Change working directory to the location where you want to clone the project to.

5. Type "git clone" and then paste (ctrl + shift, v) the URL which you just copied. Alternatively copy and paste the command below.

```
$ git clone https://github.com/Catrovich/Chamber-Danger.git
```

6. Press Enter.


### Downloading Release

to be completed...

## Setting the correct dependencies

Dependencies in this project are managed through Poetry. If you don't have Poetry installed on your computer already you can install it according to the instructions below.

### Installing Poetry

1. First check that you have the correct version of python installed by typing the command:

```
python3 --version
```

If "python3" for some reason can't be found, try:

```
python --version
```

If the version is under 3.8 install the newest version of [Python](https://www.python.org/downloads/)


2. Install Poetry by typing the command:

```
curl -sSL https://install.python-poetry.org | POETRY_HOME=$HOME/.local python3 -
```

3. After this we need to set the correct PATH. Type the command:

```
echo "export PATH=\"\$HOME/.local/bin:\$PATH\"" >> $HOME/.bashrc
```

If you are using .zsh, switch .bashrc to .zshrc.

4. You have now installed Poetry on yout computer and are ready go on to actually setting the dependencies.


### Setting the Dependencies

1. Run the command in the project directory:

```
Poetry shell
```

This puts you in a virtual environment which makes sure that it doesn't mess with the rest of your computer.

2. Run the command in the project directory:

```
Poetry install
```

This installs all the correct dependencies.

3. You are now ready to start the actual program.


### Starting and closing the program. 

1. Start the program by running this command in the project directory:

```
Poetry run invoke start
```

2. After this you are asked by the program what type of dungeon you want to generate. Type 1 for a dungeon with straight corridors and 2 for a more organic look.

3. The program then asks you how big the dungeon should be at a scale from 1-10. Answer what you want.

4. The program will now generate a dungeon of your chosen type and size.

5. Close the program by hitting the "x" at the right corner of the window.
