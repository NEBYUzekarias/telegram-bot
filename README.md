# telegram-bot

Simple python telegram bot using pyTelegramBotAPI

The bot will accept 5 commands /photo, /gif, /thougth, /help, /start

    * /photo   [keywords to search] - will do a search at bing and will return a random result
    * /gif     [keywords to search] - will do a search at giphy and will return a random result
    * /thought - will return a random phrase
    * /help    - show help
    * /start   - show help

# Requeriments

    * python telegram api 
	https://github.com/eternnoir/pyTelegramBotAPI

    * other python libs  
	beautifulsoup4 
	urllib2
	urllib
    python-mysql.connector

# Install
    
    ** If you are new with telegram bots read
       https://core.telegram.org/bots

    * Install dependecies
    * Create bot using the botfather https://telegram.me/botfather
    * Rename the config.sample.py to config.py and complete it with your parameters
    * Create directory pics/
    * Create mysql database matching the name at config.py
    * Run the sql/telebot.sql to create the database to storage phrases
    * Choose a file from sql/phrases/ and configure it in sql/file2mysql.py
    * Run sql/file2mysql.py to add phrases from sql/phrases to database

    **NOTE: phrases used here are from fortune command

    And that's pretty much it, enjoy.
