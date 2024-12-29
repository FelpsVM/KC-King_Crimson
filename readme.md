# Discord Bot Project

This is a Discord bot project built using Python, `discord.py`, and `dotenv`. The bot is designed to use prefix commands and slash commands for interaction with users on a Discord server.

## Prerequisites

Before running the bot, you need to properly set up the environment. Here are the steps to ensure everything is configured correctly:

### 1. Install Dependencies

This project depends on several Python libraries, which can be installed using the `requirements.txt` file. To install the dependencies, follow the steps below:

1. Clone or download the repository to your computer.
2. Create and activate a Python virtual environment (optional, but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/MacOS
   venv\Scripts\activate     # On Windows
   ```
3. Install the necessary dependencies:
```bash
  pip install -r requirements.txt
```
### 2. Set Up Environment Variables
This bot uses a .env file to store sensitive environment variables, such as the bot token and server ID. To configure it:

Create a .env file in the root of the project.

In the .env file, add the following variables:
```bash
guild_id=YOUR_GUILD_ID_HERE
token=YOUR_BOT_TOKEN_HERE
minimum_role_id=YOUR_MINIMUM_ROLE_ID
```
Replace YOUR_GUILD_ID_HERE with the ID of the server (guild) where the bot will run.
Replace YOUR_BOT_TOKEN_HERE with your Discord bot token.
Replace YOUR_MINIMUM_ROLE_ID with the ID of the minimum role to make some commands.

### 3. Bot Commands
(atual prefix)prefix
This command shows the bot's atual prefix for interacting with the server. The slash command (/prefix) is also available.
(atual prefix)setprefix
This command changes the bot's current prefix to the value of the argument. The slash command (/setprefix) is also available.