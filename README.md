# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.
In short, this game provides a user a certain number of attempts to guess a randomly generated secret number. However, this game is also glitchy and is designed for the user/programmar to find bugs, document them, understand why and how they're happening, and fix them.

- [X] Detail which bugs you found.
I found multiple bugs:
   1. Game tells user to go low or go high but the numbers would be in the opposite direction. I.e. secret number is 5 and user guesses 4 but game says to guess lower.
   2. History was not showing correctly or was delayed in showing past attempts.
   3. Score was showing as negative even when user guessed the right number, and then final score was showing as positive.
   4. Attempts allowed vs attempts left vs current attempts were mismatched. i.e. attempts left is 3, attempts allowed is 8, and current attempts is 6.

- [X] Explain what fixes you applied.
I fixed bug 1 and 2! History is no longer delayed and hints are no longer incorrect.

## 📸 Demo

- [Bug 1: Wrong Hint Fixed](delayed_history_fixed.png)
- [Bug 2: Delayed History Fixed](wrong_hint_fixed.png)
