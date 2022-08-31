# Implementation document

This document explains specifics about the project structure and implementation methods used in the project.
 
## Project Structure

The program follows the idea of seperation of concerns and simplicity while still retaining a design that is intuitive to a human. 

The main program is split into four main classes, a ui_service class and a function for visualization. The main  program is divided into two parts depending on wether the user wants to generate a more sterile sewer-like dungeon or a more organic limestone-cave-like dungeon. Depending on this decision the program will use either the normal BSPDungeon or OrganicBSPDungeon class. Both of these are structured in a similar way and differs mostly at the stage where chambers/rooms are to be connected. They both make use of the Node class and Chamber class. The Node class is the core of the BSP algorithm as it is used to create and store the binary tree through the Binary space partiitoning algorithm (BSP). The chamber class holds information about chamber dimensions and locations. When the random dungeon has been generated it is exported to the draw_dungeon function which visualizes the dungeon through the pygame module.

### Visualization of the Project structure

![](./ictures/project_structure.png)


## Big O

The program is currently running at a O(n) linear time complexity. This is however not central to this program since it is viewed from a human perspective where the inputs of n are always so small that time complexity hardly matters. The focus will instead be on the quality and variation in dungeons that the program can produce. The O(n) time complexity is backed up by empirical testing (see [testing_document](./testing_document.md)).


## Improvements

There is ofcourse always room for improvement. The focus of the project was to create a solid program that can produce two differing dungeons. This the project achieves. The dungeons uses different algorithms to achieve this and the result is very different. Improvements could be for example a third kind of dungeon, a combiantion of two different techniques.


## Sources

Herbert Wolverson - Procedural Map Generation Techniques (Roguelike Celebration, 2020)
https://www.youtube.com/watch?v=TlLIOgWYVpI

Create a Random Dungeon with Python (H.J. Petty, 2021)
https://python.plainenglish.io/create-a-random-dungeon-with-python-f17118c1eebd
