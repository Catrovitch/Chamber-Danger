# Week 6 report

This week I decided to focus on implementing and analyzing the changes which where suggested by my peers in their review of my project. I found their critique very informative and constructive and I have implemented almost all of their suggestions. Besides this I have also written detailed instructions on how to download, set up and start the program. Lastly I also wrote my second peer-review which also was very interesting.


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
