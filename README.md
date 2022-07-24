# Redis-TGBot
Sourcode and Resources for Telegram and Redis Integration
<p align="center">
 <img src="./stat/img.jpg" width="400" style="border-radius: 10px;">
</p>

# Installation
* 1 - clone repo https://github.com/Muhammadali-Akbarov/redis-tgbot.git
* 2 - create a virtual environment and activate
*  -  ```pip3 install virtualenv```
*  - ```virtualenv venv```
*  - ```source venv/bin/activate```
* 3 - cd into project "cd redis-tgbot"
* 4 - ```pip3 install -r requirements.txt```
* 5 - ```python3 main.py```

# Features
* 1 - redis-cli
* 2 - SUBSCRIBE mychannel
* 3 - PUBLISH telegram_notifications ```'{"chat_id": "any chat id if bot connected as admin or has private chat", "message": "Hello from redis"}'```



