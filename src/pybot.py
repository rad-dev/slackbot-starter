from slackclient import SlackClient

MENTION_REGEX = '^<@(|[WU].+?)>(.*)'
EXAMPLE_COMMAND = 'do'

class PyBot:
    def __init__(self, token):
        self.slack_client = SlackClient(token=token)
        self.slackbot_id = None
