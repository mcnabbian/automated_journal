# Automated Journal
The goal of this project is to create a script which automatically sends me a form to fill out asking me about my day.
The idea is that this will teach me valuable skills about how to start, map out, build, and eventually complete a
personal project. It will also, once completed, encourage me to write out my thoughts about the day and conveniently
store them, creating a log that I can reflect on over time.

[Source Code](https://github.com/mcnabbian/automated_journal/blob/master/gui.py)

**How to use:**
 - Download gui.py and questions.txt to the same folder
 - run gui.py (execute it through terminal, IDE, etc.)
 - gui.py will read questions.txt to create the question labels in the GUI line by line. If desired, write your own questions, but be sure to write each one to a new line.

I will break this project down into the following steps:
1. Write a program that I can run and send an automated email. ✅
2. Get that email to send everyday at the same time. ❌
  - Developed GUI instead
3. Format that message with relevant language.. HTML? ✅
  - Kinda, emails sends HTML and if that's blocked by the receiver, uses plain-text
4. Save replies to database/file. ❌
  - Using and saving emails not a priority
5. I will then modify the program to send a message to my desktop using a GUI. 	✅
  - This seems like the same idea as step #7. Not a priority for right now.
6. Continue to save replies/entries into database/file. ✅
7. Send desktop push notifications. ❌

*everything below is something to look into in the future*

8. Create a mobile app. ❌
9. Ensure sending of daily push notifications. ❌
10. Synchronise entries between desktop app and mobile app. ❌

Possible questions:

- What have I learned today?
- What have I learned about myself?
- What went well today?
- What would I do differently about today?
- Did I achieve everything I set out to do today?
- What am I going to do tomorrow?
