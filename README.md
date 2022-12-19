# FastApi + TeleBot
```
# Edit webhook address
$ python3 -m uvicorn main:app
```
#### How to setup it with deta.sh?
```
# Create new bot with @BotFather.
# Paste your token to BOT_TOKEN.

$ deta login  
Please, log in from the web page. Waiting...
https://web.deta.sh/cli/{some_id}
Logged in successfully.

$ deta new
{
        "name": "FastApi-TeleBot",
        "endpoint": {HOST}
}
# Edit HOST with yours endpoint.

$ deta deploy

# Write any message to telegram bot.
```
