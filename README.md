# Weakest-Link

Assistant for running The Weakest Link game show.

Before running, edit the players.txt file to add the names of the players, separated by a comma and a space (e.g. James, John, Jane).

Buttons:
- Correct - Changes the current amount (0, 20, 50, 100, 200, 400, 600, 800, 1000) and changes player
- Incorrect - Resets the current amount and changes player
- Bank - Stores the current amount and sets it to 0
- End Round - Sets the current amount to 0 and displays the number of correct answers and banks for each player

At the end of each round, players discuss who to eliminate, this is done in person and does not require interaction with the program. Once the person has been decided, enter who you they have chosen the remove. Afterwards the host selects the strongest link (typically the player with the most correct answers and/or banks). Both of these are selected by the ID of the player.

In the next round the player removed will not be included and the strongest link will receive the first question
