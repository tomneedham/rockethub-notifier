# Webhoook helper
from github_webhook import Webhook
# For webserver
from flask import Flask
# For Rocketchat API
from rocketchat.api import RocketChatAPI
# For Github API
from github import Github
# For env vars
import os

ghAccessToken = os.environ.get('GITHUB_ACCESS_TOKEN')
rocketChatBotUsername = os.environ.get('ROCKET_USERNAME')
rocketChatBotPassword = os.environ.get('ROCKET_PASSWORD')
rocketChatDomain = os.environ.get('ROCKET_DOMAIN')
rocketChatChannel = os.environ.get('ROCKET_CHANNEL')
webhookSecret = os.environ.get('WEBHOOK_SECRET')
webhookPort = os.environ.get('WEBHOOOK_PORT')

g = Github(ghAccessToken)

rocketAPI = RocketChatAPI(settings={'username': rocketChatBotUsername, 'password': rocketChatBotPassword, 'domain': rocketChatDomain})

app = Flask(__name__)
webhook = Webhook(app, secret=webhookSecret) 

def notifyInboundSolutionFocusTicket(data):
	app.logger.info('Checking if event is suitible...')
	# Check we really want to notift about this post
	if data['action'] != 'created':
		app.logger.info('Action is not type created, ignoring')
		return
	app.logger.info('Generating message')
	sender = data['sender']['login']
	contentUrl = data['project_card']['content_url']
	issueId = contentUrl.rsplit('/', 1)[-1]
	githubRepo = g.get_repo(data['repository']['id'])
	githubIssue = githubRepo.get_issue(int(issueId))
	htmlURL = 'https://github.com/' + data['repository']['full_name'] + '/issues/' + issueId
	message = ':robot: New inbound ticket: `' + githubIssue.title + '` - ' + htmlURL
	app.logger.info('Sending message' + message)
	rocketAPI.send_message(message, 'solutions')

@webhook.hook(event_type='project_card')
def on_project_card_events(data):
	notifyInboundSolutionFocusTicket(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=webhookPort)