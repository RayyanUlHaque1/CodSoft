# **Rock, Paper, Scissors Game**

This is a simple implementation of the classic Rock, Paper, Scissors game where the player competes against the computer. The player inputs their move, and the computer randomly selects one from the available choices: Rock, Paper, or Scissors. The game evaluates the player's choice against the computer's choice and determines the outcome based on the standard rules:

- **Rock** beats **Scissors**.
- **Scissors** beats **Paper**.
- **Paper** beats **Rock**.
- If both players choose the same option, it's a **tie**.

# **Features:**
1. **User Input:** The player is asked to enter their move (Rock, Paper, or Scissors). The input is validated to ensure only valid choices are accepted.
2. **Computer Choice:** The computer randomly selects its move from the list of available choices.
3. **Score Tracking:** The game keeps track of the score for both the player and the computer. Each win increments the respective player's score.
4. **Game Continuation:** After each round, the player is asked if they want to play again. The game continues until the player decides to stop.
5. **Real-time Feedback:** The outcome of each round is displayed immediately, including the choices made by both the player and the computer, as well as who won or if it was a tie.

# **Project Flow:**
1. The player makes their move.
2. The computer randomly picks a move.
3. The winner is determined based on the game rules.
4. Scores are updated and displayed.
5. The player is asked if they want to play again.

# **Technologies Used:**
- **Python**: The game is implemented using Python programming language. 
- **Random Module**: The `random.choice()` function is used to randomly select the computer's move.

---

This description gives a clear overview of the project, including its features and how it works. Feel free to adjust it according to any additional features or details you may want to include!