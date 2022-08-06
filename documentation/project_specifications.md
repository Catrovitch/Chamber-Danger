# Project specifications

## Introduction

In this project I will create a dungeons generator consisting of rooms or chambers and corridors connecting the chambers. Documentation will be done in English and the programs will be written in python. Python is also the only programming language that I'm currently comfortable with. Officially my field of study is the bachelor's program in geography, but I'm in the process of switching to computer science, and in practice I have about the same amount of study points in both fields. 

## Algorithms and data structres

The algorithm that will be used can be divided into roughly four steps. 

Steps:

1. Generate an empty map of a given size.
2. Use BSP to randomly, but evenly distribute rooms around the map.
3. Connect the chambers either with straight corridors or through drunkard's walk algorithm.
4. Visualize the dungeon.

The dungeons will be stored as a python dictionary in which the key is a tuple of (x,y) coordinates and the value is 0 for a wall and 1 for open space.

## Input

Depending on what size and what sort of dungeon you want to generate the following input values can be calibrated. 

Total size of the dungeon: This will be given as two values; dungeon_width and dungeon_height.

Minimum size of chambers: This will function as a minimum limit value for the size of a chamber.
Maximum size of chambers: This will function as a maximum limit value for the size of a chamber.

Max amount of rooms: This will decide how many chambers the dungeon will be made up of at max.
Min amount of rooms This will decide how many chambers the dungenon will be made up of at min.

## Sources

Herbert Wolverson - Procedural Map Generation Techniques (Roguelike Celebration, 2020)
https://www.youtube.com/watch?v=TlLIOgWYVpI

Create a Random Dungeon with Python (H.J. Petty, 2021)
https://python.plainenglish.io/create-a-random-dungeon-with-python-f17118c1eebd
