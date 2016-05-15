# telegram-bot

Simple python telegram bot using pyTelegramBotAPI

The bot will accept 3 commands /photo, /gif, /thougth, /help, /start

    * /photo   [keywords to search] - will do a search at bing and will return a random result
    * /gif     [keywords to search] - will do a search at giphy and will return a random result
    * /thought - will return the outut of the fortune command
    * /help    - show help
    * /start   - show help

# Requeriments

    * python telegram api 
	[link telegram api](https://github.com/eternnoir/pyTelegramBotAPI)

    * other python libs  
	beautifulsoup4 
	requests
	urllib2
	urllib

    * fortune command
	root@box:~# apt-get install fortune 	(for aptitude based system)
	root@box:~# yum install fortune 	(for yum based system) 

# Install
    
    ** If you are new with telegram bots read

       [link bot](https://core.telegram.org/bots)

    * Create bot using the botfather [link botfather](https://telegram.me/botfather)
    * Add token to line 13 in bot.py
    * Create directory pics/

    And that's pretty much it, enjoy.
