# Weakest-Link

Assistant for running The Weakest Link game show.

Before running, edit the players.txt file to add the names of the players, separated by a comma and a space (e.g. James, John, Jane).

Buttons:
- Correct - Changes the current amount (0, 20, 50, 100, 200, 400, 600, 800, 1000) and changes player
- Incorrect - Resets the current amount and changes player
- Bank - Stores the current amount and sets it to 0
- End Round - Sets the current amount to 0 and displays the number of correct answers and banks for each player
- Reroll Question - If the question that comes up is too difficult or not what you need, you can reroll for a new one
- Reset Game - If you want to play again, press the button and all the players will be re-added from the text file without all the used questions being re-added - good for multiple games without repeat questions

At the end of each round, players discuss who to eliminate, this is done in person and does not require interaction with the program. Once the person has been decided, enter who they have chosen to remove. 
The host selects the strongest link (typically the player with the most correct answers and/or banks). Both of these are selected using the ID of the player.

In the next round the player removed will not be included and the strongest link will receive the first question

To abort this process, type -1 as the weakest link, this will allow play to continue as normal

The trivia.json file contains a number of trivia questions/answers added by myself. If you would like to use this program, feel free to edit them or use them as they are. They were personally chosen by me for my specific friend group so results may vary
