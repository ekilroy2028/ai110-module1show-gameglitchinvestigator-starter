# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  •When the game is over, we cannot reset after pressing the new game button. The number of attempts is not recording correctly, which causes the game to end early.  
  •The hints for the number of guesses are incorrect; they always aim higher. And the number guessed is put in.   
  •The secret guest shows the answer. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

• I went into Copilot, listed all three fixes I wanted to address. Then, I also included a note with each fix explaining why it was fixed and what happened. Afterward, I reran the test and discovered that the higher/lower issue still appeared as higher. I took that information and entered it into Copilot again, asking it to fix the problem once more, and repeated the process. This time, the game is working.  

• I only use Copilot for this project. I wanted to establish a solid foundation for how to fix code, and I didn't want another program to interfere. In the previous activity, Tinker_ByteBites, I used Claude just to get a feel for how this process works. I found that using Claude is kind of like having a tutor or teacher; they talk to the program as if I were talking to a professor. It was very helpful in understanding how the coding process we're learning actually works. And from the insight I gained into the Tinker_ByteBites project, I carried that knowledge into The Game Glitch project.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was fixed by running the pytest tests and observing the game behavior. If the tests passed and the game no longer exhibited the buggy behavior (like incorrect hints or inability to reset), I considered it fixed. I also manually tested the app to ensure the UI worked correctly.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran pytest multiple times: initially it failed due to import issues, then after fixing package structure, it passed. The tests showed that the check_guess function correctly returns "Too High" or "Too Low" outcomes. I also manually ran the Streamlit app to verify hints displayed correctly ("Go LOWER!" for high guesses, "Go HIGHER!" for low guesses).

- Did AI help you design or understand any tests? How?
Yes, Copilot helped me understand the test failures and suggested fixes like adding __init__.py files to make the project a proper package. It explained why the imports were failing and guided me to update the test assertions to unpack the tuple returned by check_guess. Copilot also helped refactor the code and add comments documenting our collaboration.

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
