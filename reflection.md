# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

1. When I first ran it, I guessed number 20, and it told me to go lower even though the number is 81. I expected it to tell me to go higher.

2. The history is buggy. When I click submit guess, it does not add guess to the history until I add another guess. I expect the guess to be immediately added.

3. It shows me score is -20 but when I guessed the right number, it shows final score as 10.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude and Copilot.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I had an issue with my tests where the original test starter tests assert that the function returns a plain string whereas my updated implementation of check_guess returns a tuple.
So, Copilot correctly fixed the tests by making each case extract the outcome from the tuple and use that to compare results.
I was able to verify the results from the AI's response through running the tests and seeing that they pass, while also running the application live and going through those test cases manually.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
To fix my second bug of history being shown delayed, Copilot suggested I make Streamlit start a fresh sun so the top-of-page expander will see the updated history immediately using `st.experimental_rerun()`.
However, this response was misleading as I verified the response through trying the suggestion and I ended up getting an AttributeError saying that stream does not have this function.
Turns out, Copilot did not mention that this function was added recently and that my Streamlit version does not have it. I had to steer Copilot to fix this UI bug another way.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
How did you decide whether a bug was really fixed?
I made sure to pass the given tests in the test file while also running the code live and going through the happy path to see if it got fixed or if it is reoccurring. Passing the tests told me that my code at least is passing the happy path.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran the test_game_logic.py and passed all tests like test_guess_too_high() and test_guess_too_low().
  
- Did AI help you design or understand any tests? How?
The AI wrote the tests for me on top of the additional existing test. I also ran into issues with the data type the functions returned so I had AI work with alternating all tests to receive a specific data type.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
