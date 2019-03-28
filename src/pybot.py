import re
from slackclient import SlackClient
from src import settings
from src import commands
from src import responses


class PyBot:
    def __init__(self, token):
        self.slack_client = SlackClient(token=token)
        self.slackbot_id = self.slack_client.api_call("auth.test")["user_id"]

    @staticmethod
    def parse_direct_mention(message_text):
        """
            Finds a direct mention (a mention that is at the beginning) in message text
            and returns the user ID which was mentioned. If there is no direct mention, returns None
        """
        matches = re.search(settings.MENTION_REGEX, message_text)
        # the first group contains the username, the second group contains the remaining message
        return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

    def parse_bot_commands(self):
        """
            Parses a list of events coming from the Slack RTM API to find bot commands.
            If a bot command is found, this function returns a tuple of command and channel.
            If its not found, then this function returns None, None.
        """
        slack_events = self.slack_client.rtm_read()

        for event in slack_events:
            if event["type"] == "message" and not "subtype" in event:
                user_id, message = self.parse_direct_mention(event["text"])
                if user_id == self.slackbot_id:
                    return message, event["channel"]
        return None, None

    def handle_command(self, command, channel):
        """
            Executes bot command if the command is known
        """

        # Finds and executes the given command, filling in response
        response = None
        # This is where you start to implement more commands!
        if command.startswith(commands.SAY_HELLO):
            response = responses.SAY_HELLO


        # Sends the response back to the channel
        self.slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=response or responses.DEFAULT_RESPONSE
        )

    def is_connected(self):
        return self.slack_client.rtm_connect(with_team_state=False)
