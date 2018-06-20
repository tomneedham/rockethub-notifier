# Rocketchat Github Project Notifier

Use this tool to ping a channel in Rocketchat when a card in added to a Github Project. You can use this for workflows where teams are given tickets (issues or pull requests), they are automatically added to an 'inbox' column, and are processed by that team. To help with communication, this bot pings a specific channel with a notification that a card was assigned to the project.

## Usage

Build it:
`docker build -t rockethub-notifier .`

Run it:
`docker run -e "GITHUB_ACCESS_TOKEN=123" -e "ROCKET_USERNAME=solutionsbot" -e "ROCKET_PASSWORD=123" -e "ROCKET_DOMAIN=https://rocket.company.com" -e "ROCKET_CHANNEL=solutions" -e "WEBHOOK_SECRET=secret" -e "WEBHOOOK_PORT=8888" -p 8888:8888 rockethub-notifier`

Config options:
 - GITHUB_ACCESS_TOKEN
 - ROCKET_USERNAME
 - ROCKET_PASSWORD
 - ROCKET_DOMAIN
 - ROCKET_CHANNEL
 - WEBHOOK_SECRET
 - WEBHOOOK_PORT