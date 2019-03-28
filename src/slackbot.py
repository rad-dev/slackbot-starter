import time
from src.pybot import PyBot

from src import settings

if __name__ == "__main__":
    pybot = PyBot(settings.SLACKBOT_TOKEN)

    if pybot.is_connected():
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        while True:
            command, channel = pybot.parse_bot_commands()
            if command:
                pybot.handle_command(command, channel)
            time.sleep(settings.RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
