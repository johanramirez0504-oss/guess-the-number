# guess-the-number
A Python console game where players have to guess a random number generated between two numbers chosen by the player.
# Guess the Number (Python)

A Python console game where players have to guess a randomly generated number between two numbers chosen by the player. Players can also choose the maximum number of attempts and earn points based on their performance.

## Features

- Random number generation using the `random` module.
- Custom minimum and maximum range.
- Custom maximum number of attempts.
- Input validation.
- Hints indicating whether the secret number is higher or lower.
- Score system based on:
  - Number of attempts.
  - Range size.
  - First-attempt bonus.
  - Large-range bonus.
- Total score accumulated across multiple games.
- Replay option after each match.
- Error handling with `try`/`except`.

## Technologies

- Python 3
- `random` module

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/guess-the-number.git
```

2. Open the project folder.

3. Run the program:

```bash
python guess_the_number.py
```

## Gameplay

1. Choose the minimum number.
2. Choose the maximum number.
3. Choose the maximum number of attempts.
4. Try to guess the secret number.
5. Earn points depending on your performance.
6. Decide whether to play another round.

## Scoring System

- Points are awarded based on the selected range and the number of attempts.
- Bonus points are awarded for guessing the number on the first attempt.
- An additional bonus is awarded for large ranges (100 numbers or more).
- The total score is accumulated during the session.

## Skills Demonstrated

- Implementing game logic in Python.
- Generating random numbers with the `random` module.
- Validating user input.
- Handling exceptions with `try`/`except`.
- Managing program flow with loops and conditional statements.
- Designing a customizable scoring system.
- Building an interactive console application.

## Future Improvements

- Difficulty presets (Easy, Medium, Hard).
- Save the highest score.
- Timer mode.
- Graphical user interface (GUI).
- Multiplayer mode.

## Author

**Johan Gabriel Ramírez Durán**
