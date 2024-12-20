# Grand Race Randomizer
A randomizer for Grand Races in The Crew Motorfest that will randomly choose which car manufacturer for you to use in each section of the race.

It works by assigning each race category of the Grand Race to three dropdown menus, where each category inside the dropdown menu has a list assigned to it with all the car manufacturer options you can use in said category. Going from left to right you will choose which rotation the current Grand Race is, and then hit the Randomize button. The results will populate underneath for you to follow.

There is also an Add Manufacturer button which can be used to add in a new car manufacturer to one of the car categories. For example, if Ivory Tower adds in a Ferrari to Rally Raid (for some reason), you can update the program yourself by using this option. Once you make atleast one change to the lists, a .JSON file will be created that will store all the updated lists from that point forward, which is what the program will reference to choose the manufacturer. This .JSON file will be created inside the working directory of the .exe.

The last button is a Reset button, which will get rid of the current results and put the program back to its launch state (this will not modify nor delete the .JSON file).
