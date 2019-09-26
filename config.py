conf = {
    'telegram_token'     : '780961097:AAHcGlPrEruUHuwjPhdU5gxeUFun7dbFB4Q',
    'msg_on_empty_query' : 'hey, forgot the query, command is: {} keywords',
    'no_results'         : 'did\'t find anything',
    'getting_gif'        : 'found it, hang on a sec',
    'help_msg'           : '/thought - print a fortune\n/help - show help',
    'mysql'     : {                                                
        'user'         : 'root',                             #mysql user
        'password'     : '26535986',                             #mysql password
        'host'         : 'localhost',                              #mysql host
        'database'     : 'telebot',                                #mysql database
        'port'         : 3306,                                     #mysql port
        'unix_socket'  : '/var/run/mysqld/mysqld.sock',            #mysql unix socket file
        'raise_on_warnings': True
    }
}
