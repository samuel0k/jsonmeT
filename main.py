from tabulate import tabulate 
import requests
import sys

# Local files
import startCraler
import clear

clear.clear()


print("""\033[35m
 ╦╔═╗╔═╗╔╗╔┌┬┐┌─┐
 ║╚═╗║ ║║║║│││├┤ 
╚╝╚═╝╚═╝╝╚╝┴ ┴└─┘

Author: \033[32mSamuel k\033[0m\033[35m
Youtube: \033[32mhttps://www.youtube.com/channel/UCGE2cz5KNAEA8Fc79VuIYZQ\033[35m
Github: \033[32mhttps://github.com/samuel0k\033[35m
Version: \033[32mv1.0\033[0m
""")

options = [
    ["help", "Show all commands"],        
    ["craw","web crawler, use: craw https://websitetotest.com"],
    ["exit or quit", "Exit the program"],
    ["clear or clean ", "Clean the shell"]
]

while True:
    try:
        resp = str(input('\033[32m>\033[0m '))

        if resp:
            if resp == 'exit' or resp == 'quit':
                print('\033[34mBye!\033[0m')
                sys.exit(1)
            elif resp == 'help':
                print('\033[33m')
                print(tabulate(options, headers=['Command', 'Info']))
                print()
            elif resp.split()[0] == "craw":
                if not len(resp.split()) == 2:
                    print('\033[31mERRO: no url!\033[0m')
                    print('\033[32mexemple: craw https://websitetotest.com\033[0m')
                else:
                    startCraler.start(resp.split()[1])
            elif resp == "clear" or resp == "clean":
                clear.clear()
            else:
                print('\033[31mERRO: invalid command!\033[0m')
        else: 
            print('\033[31mERROR: type something!\033[0m')

    except KeyboardInterrupt:
        print('\033[34mBye!\033[0m')
        sys.exit(1)
