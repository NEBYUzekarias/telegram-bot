conf = {
    'telegram_token'     : 'YOUR_TELEGRAM_TOKEN',
    'msg_on_empty_query' : 'hey, forgot the query, command is: {} keywords',
    'no_results'         : 'did\'t find anything',
    'getting_gif'        : 'found it, hang on a sec',
    'help_msg'           : '/photo keywords - find image \n/gif keywords - find gif\n/thought - print a fortune\n/help - show help',
    'mysql'     : {                                                
        'user'         : 'MYSQL_USER',                             #mysql user
        'password'     : 'MYSQL_PASS',                             #mysql password
        'host'         : 'localhost',                              #mysql host
        'database'     : 'telebot',                                #mysql database
        'port'         : 3306,                                     #mysql port
        'unix_socket'  : '/var/run/mysqld/mysqld.sock',            #mysql unix socket file
        'raise_on_warnings': True
    }
}
