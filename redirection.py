import requests
import os
import bcolors
import sys, argparse
import random

def banner():
    print("""
       
                ██████╗░███████╗██████╗░██╗██████╗░███████╗░█████╗░████████╗░░░░░░███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
                ██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗╚══██╔══╝░░░░░░██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
                ██████╔╝█████╗░░██║░░██║██║██████╔╝█████╗░░██║░░╚═╝░░░██║░░░█████╗█████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
                ██╔══██╗██╔══╝░░██║░░██║██║██╔══██╗██╔══╝░░██║░░██╗░░░██║░░░╚════╝██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
                ██║░░██║███████╗██████╔╝██║██║░░██║███████╗╚█████╔╝░░░██║░░░░░░░░░██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
                ╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░░░░╚═╝░░░░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
                      
          """)

if len(sys.argv) > 1:
    banner()
    if (sys.argv[1] == '-d'):
        try:
          input_url = sys.argv[2]
          if (os.path.exists(input_url) == True):
            parser = argparse.ArgumentParser()
            parser.add_argument("-d", required=True)
            args = parser.parse_args()
            input_file = open(input_url, "r")
            input_file_line = input_file.readlines()

            for file_url in input_file_line:
                try:
                    url = file_url.strip()
                    urlRediection = requests.get(url, allow_redirects=False)
                    print(bcolors.BITALIC + "Testing for Rediection")
                    if((urlRediection.status_code == 301 ) or (urlRediection.status_code == 302)):
                        urlHistory = urlRediection.history
                        print('Redirected URL::' + urlRediection.headers['Location'])
                    elif(urlRediection.status_code == 200 ):
                        print('Rediection not possible')
                except:
                        print(bcolors.ERRMSG + 'This is not valid URL ' + url)
          elif(os.path.exists(input_url) == False):
                    input_header = requests.get(input_url)
                    parser = argparse.ArgumentParser()
                    parser.add_argument("-d", required=True)
                    args = parser.parse_args()

                    print(bcolors.BITALIC + "Testing for Rediection")
                    url = requests.get(input_url, allow_redirects=False)
                    if ((url.status_code == 301) or (url.status_code == 302)):
                        urlHistory = url.history
                        print('Redirected URL::' + url.headers['Location'])
                    elif(url.status_code == 200):
                        urlHistory = url.history
                        print('Redirected URL::' + url.headers['Location'])
                        print('Rediection not possible')
        except:
            print('Please enter python redirection.py -d <valid domain name> ')
            print("Give Domain with http:// or https://")

    elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: redirection.py [-h] -d DOMAIN' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-d Domain,   --domain Domain')
    elif (sys.argv[1] != '-d'):
        print('Please enter -d <valid domain name> ')
else:
    banner()
    print(bcolors.ERR + 'Please select atleast 1 option from (-d,-o) or -h, with a valid domain name')


