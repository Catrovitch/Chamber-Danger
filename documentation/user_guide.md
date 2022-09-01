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

Find the "Realeases" window at the right side of the README document. Click on the release named "Chamber Danger". Download the .zip file. Extract the downloaded file to a location of your choice. Navigate to the extracted folder in terminal. To make sure you are in the correct location, check that the  "pyproject.toml" file is in the folder. You have succesfully downloaded, extracted and navigated to the corrected folder. 

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

2. The program starts a graphical user interface where you can mark some selection according to what sort and size of dungeon you want to create. 


3 Tick the box for either industrial or organic dungeon. After this you can choose to show various layers or leave them all off.

4. Some additional layers. These can be tinkered with at any time.

 -  The "Show chambes" will visualize a separate layer which only visualizes the chambers in the dungeon. The number at the left upper corner of the chamber indicates at what depth the chamber was generated in the BSP algorithm. The higher the number is the deeper in the BSP tree the chamber is located. 
 -  The "Show corridors" will visualize a separate layer which only visualizes the corridors between the chambers. These are colour coded according to the parent chamber.
 -  The "Show dungeon depth" will visualize the depth of all chambers according to how deep in the BSP tree they are found. This can also be seen as the integer at the upper left corner. (same as "Show chambers"). The deeper the chamber is located the darker the colour.
 -  The "Show graph" will visualize a separate layer which only visualizes the vertices of the BSP tree. This gives a clearer indication on which chambers are actually connected, since the basic visualization may confuse this matter since many corridors overlap each other. The "Show chambers" and "Show corridors" layers can be of help, but the "Show graph" should definetly clear things up.

5. Some additional variables. These can not be tinkered with after genration. Generate a new dungeon to play with these.

 -  The "Choose max node size" parameter tinkers with the BSP-algorithm's variable "max_node_size" This means that the larger this number is the larger the subsets of the BSP divisions will be in general. This will lead to a more spread out dungeon with less rooms and longer corridors. 
 -  The "Choose min chamber size" parameter indicates the minimum size of chambers in the dungeon.
 -  The "Choose max chamber size" parameter indicates the maximum size of chambers in the dungeon.
  
6. Close the program by hitting the "x" at the right corner of the window.
