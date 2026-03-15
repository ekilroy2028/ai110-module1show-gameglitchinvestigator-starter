# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used GitHub Copilot in VS Code for this project, including Chat, Inline Chat, and Agent mode for refactoring.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Copilot suggested refactoring the core game logic functions (check_guess, parse_guess, etc.) from app.py to logic_utils.py for better separation of concerns. I verified this by running the refactored code - the functions imported correctly, tests passed, and the app still worked as expected.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Initially, Copilot's hint fix in check_guess had the messages backwards (saying "Go HIGHER!" for too high guesses). I verified this by running the app and seeing incorrect hints, then corrected it by swapping the messages and confirmed the fix with pytest.

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
This might be a testing habit, a prompting strategy, or a way you used Git. I want to reuse the habit of adding detailed comments with #FIX tags explaining AI collaboration, as it helps document the development process and makes code more maintainable. I also fixed the functionality and ensured that the program works and the game can be played. However, I didn't fix the cosmetic aspects, which are equally important—such as making sure the game is fun and attractive. For example, when it's in dark mode, the buns are green. Why not use a different color, like a brighter one such as yellow or orange? In dark mode, instead of having it black, consider using a dark gray or a different dark color, like a deep dark red or orange. Making these small changes can make the experience more fun and unique for the viewer. Currently, when you switch to dark mode, the background is black and the text is white, which is boring and a common choice. A simple change like this could make it more engaging and distinctive.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I will start with more specific prompts and verify AI suggestions more thoroughly before applying them, rather than accepting complex changes all at once. Yes, doing it one step at a time. It's not just that; doing it one step at a time will also be more beneficial. Learning and identifying the problem is still difficult when you have a bunch of code in front of you, not knowing where to start or where to go. If you try to do everything at once, your code will become cluttered, and your learning process and discoveries will get lost because there's so much in front of you that you won't know which is which.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me that AI-generated code can be a great starting point but often contains subtle bugs that require a 'human-touch' debugging skills. It taught me to approach AI suggestions critically, test thoroughly, and collaborate with AI as a teammate rather than relying on it completely. Also, just to point out again really quick that I discovered so far through this class, it's not the process that AI is not a calculator, but it should be used more as talking to a human being. When I do that, it seems to me I get more clear-cut and direct answers. Versus when I treat AI as a calculator, I get an answer but I find it's not the best or the correct answer I need to be successful in this class so far.  
