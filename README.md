# Rain Alert
A simple python for detecting the rain with a Raspberry Pi and a rain sensor.

## Setup

1. Install [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
2. Copy `config.py.example` to `config.py`
3. [Create a new telegram bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
4. Add your token of the bot into the `config.py`
5. Create a new channel in telegram
6. Add bot to this channel with writing permission
7. Open `https://api.telegram.org/bot<your-token>/getUpdates` and write a message into the channel
8. Copy the `id` and use it as `chat_id` in the `config.py`
9. Set the `gateway` to the ip address of your router

## Start script after boot

Add `@reboot /path/to/rain.py` to `/etc/crontab`.