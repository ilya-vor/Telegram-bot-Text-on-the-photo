# Telegram bot Text on the photo

# Introduction
I created this bot because I needed to copy text from pictures.
This bot is best used with printed and clear text, such as screenshots.
Otherwise, the recognition result will be worse.

# Description
The following libraries are used in the work of this bot:
1. python-telegram-bot
2. pytesseract
3. logging

Tesseract-OCR is also used to run the program.
I downloaded it from the website:
https://www.softpedia.com/get/Programming/Other-Programming-Files/Tesseract-OCR.shtml

Bot commands: 

1. start:

This function is called when the bot starts.
Sends a welcome message and prompts you to use the /setlang command to select a language. The default language is Russian.

2. set_language:

This feature sets the language for recognizing text in images.
Uses the language passed in the command and stores it for a specific user.
Returns confirmation of the language setting.

3. text_handler:

This function is responsible for processing text messages.
Sends the current recognition language and offers to send an image for recognition.

4. image_handler:

This function processes images submitted by the user.
Extracts a file from a message, saves it to disk, and uses the pytesseract library to recognize text in an image.
Sends recognized text in response, or an error message when processing an image.

# Resources
1. python-telegram-bot - https://github.com/python-telegram-bot/python-telegram-bot
2. pytesseract - https://github.com/h/pytesseract
3. logging - https://docs.python.org/3/library/logging.html

# Getting help
If the resources mentioned above do not answer your questions, write me an email at ilya-vor-github@mail.ru