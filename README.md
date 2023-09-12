# Bot_Template
A template that removes much of the boilerplate for Pycord Bots.

## Main
The actual script to run. Loads the intents, the cogs, and connects to Discord. Reports the start-up time upon connection.

## Data
A convenience file where you can easily set the intents, the bot owner's Discord ID, and the bot's current activity.
Token is, of course, not kept here, but instead kept inside a secure .env file.

## Cogs Folder
Contains an example extension that has a basic slash command, a slash command group, and a task.
