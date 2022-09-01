# Final report

During this course I have created and recreated a dungeon generator which builds on a BSP tree algorithm and different techniques for creating visuals. The most basic version creates a dungeon with straight corridors and has a more industrial feel to it. The second alternative is a more organic looking dungeon. This version makes use of the Drunkard's Walk algorithm to achieve the organic look. Further the user can tinker with various variables to influence the dungeon in a more detailed way. To better be able to analyze the results I have created a GUI which is able to visualize the generated dungeon in different ways. The most basic visualization displays chambers and corridors in only two colours. At certain points this can create confusion however when corridors overlap that aren't really connected in the actual BSP tree. To circumvent this I have created methods for colour coding chambers and corridors. (More about this in the [user_guide](./user_guide.md)) There is also an option to visualize the depth of the dungeon. The depth at which the chamber is located at correlates with the depth at which it can be found within the BSP-tree. The darker the colour displayed the deeper in the dungeon the chamber can be found. A number at the upper left corner gives the actual numeric value for the depth level. 

The goal for this course was to create a simple and functioning dungeon generator that could be easily expanded upon in the future. I have achieved this and there could be many other variations of what already is. One example which I have started thinking of is a 3D version of this program where the dungeon depth would also be visualized. This would make for an interersting and fun improvement. 

During this last week I also made updates to all documentation documents added some additional commands to the README document and tidied up my code as well as added doc-string documentation to my project. 

Time spent this week: aprox 15h.

Thanks for the course! It's been interesting and fun and still sufficently challenging!
 
