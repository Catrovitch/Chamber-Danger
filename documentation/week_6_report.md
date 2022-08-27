# Week 6 report

This week I decided to focus on implementing and analyzing the changes which where suggested by my peers in their review of my project. I found their critique very informative and constructive and I have implemented almost all of their suggestions. Besides this I have also written detailed instructions on how to download, set up and start the program. I also wrote my second peer-review which also was very interesting. Lastly I also created a more advanced GUI for my project which also lets the user tinker with more than just the dungeon size.


## Suggested edits to my project by my peers:

Here I have shortened the changes which where suggested to me into a consice and easy to read list. Se [review 1](https://github.com/Catrovitch/Chamber-Danger/issues/1) and [review 2](https://github.com/Catrovitch/Chamber-Danger/issues/2) for more details.

 - BSPDungeon: split generate_map - split_nodes into seperate method.
 - node, chamber --> ententies
 - Node: row 74-78 formatting choices.
 - 2 rows between methods
 - Chamber: int() --> //
 - BSPDungeon: get_nodes() not used and should be removed.
 - Instructions at README
 - Typo in README leading to page not found
 - Big dungeon fails at rendering
 - snake_case vs. camelCase
 - Clean UI_service
 - Restructure BSPDungeon and OrganicDungeon

Out of all these changes only the "BSPDungeon: split..." and the "Restructure BSP..." where left out. Although these suggestions were both totally reasonable I had to leave them out due to time constraints. These where more time consuming and since my original structure also worked well I prioritized other suggestions. I especially appriciated the "Big dungeon fails.." suggestion since this was a solution to a problem which I had experienced before already. After doing the correction the program works flawlessly. Thanks a lot Topias!

## User guide

I wrote a rather comprehensive user guide to the program which entailed everything from cloning or downloading the program, to installing python and poetry to launching and shutting down the program.
Here is a link to the [user guide](./user_guide.md)

## New GUI

The new gui lets the user tinker with the new variables that affect how the dungeon is generated. Before you could only tinker with the dungeon size and this method has also changed. Earlier the dungeon size was decided by the map size, but now the size is determined by the max_node_size which the BSP algorithm uses. This means that the higher that value is the smaller the dungeon will be, or smaller in the sense that there aren't that many chambers. Other variables which I added are max_chamber_size and min_chamber_size. The control the spectrum of how big the actual chambers are which are located within the nodes. 

## Time Spent this week:

 - Implementing changes: 5h
 - User guide: 3h
 - Peer review 2: 6h
 - GUI: 8h

 - total: 24h
 
