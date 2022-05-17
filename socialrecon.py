import pyfiglet
from pathlib import Path
import time
import sys
from url import urlinfo
from pdfanalysis import pdfinfo
from imagerecon import recon
from exif import gps
from emailverify import email
from iplocator import iplocate
from webscrap import Links
from NameInfo import Nameinfo
from phone import number
# from userrecon import UserReCon
import subprocess

R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'

def reconinput():
    print('')
    print(C+"""Tools available

            1.Image Meta data extraction
            2.Email verifier
            3.Phone number Information
            4.IP location Lookup
            5.URL lookup
            6.PDF meta data analysis
            7.URL lookup in webpages
            8.Information Gathering using Name
            9.Social media hunting using image
            usage : type exit to stop
            """)
    print('')
    inp=(input("Infosysint >> "))
    if(inp == '1'):
        gps()
    elif(inp=='2'):
        email()
    elif(inp=='3'):
        number()
    elif (inp=='4'):
        iplocate()
    elif(inp =='5'):
        urlinfo()
    elif (inp=='6'):
        pdfinfo()
    elif(inp=='7'):
        Links()
    elif (inp=='8'):
        NameInfo()
    elif(inp == '9'):
        recon()
    elif(inp=='exit'):
        exit()
    else:
        text="please enter an valid option "
        print(text)


if __name__=="__main__":
    print(C +
            """
_________ _        _______  _______  _______           _______ _________ _       _________
\__   __/( (    /|(  ____ \(  ___  )(  ____ \|\     /|(  ____ \\__   __/( (    /|\__   __/
   ) (   |  \  ( || (    \/| (   ) || (    \/( \   / )| (    \/   ) (   |  \  ( |   ) (
   | |   |   \ | || (__    | |   | || (_____  \ (_) / | (_____    | |   |   \ | |   | |
   | |   | (\ \) ||  __)   | |   | |(_____  )  \   /  (_____  )   | |   | (\ \) |   | |
   | |   | | \   || (      | |   | |      ) |   ) (         ) |   | |   | | \   |   | |
___) (___| )  \  || )      | (___) |/\____) |   | |   /\____) |___) (___| )  \  |   | |
\_______/|/    )_)|/       (_______)\_______)   \_/   \_______)\_______/|/    )_)   )_(





            ___      _                                  __                                ___
  /\  ._     |  ._ _|_ _  ._ ._ _   _. _|_ o  _  ._    /__  _. _|_ |_   _  ._ o ._   _     |  _   _  |
 /--\ | |   _|_ | | | (_) |  | | | (_|  |_ | (_) | |   \_| (_|  |_ | | (/_ |  | | | (_|    | (_) (_) |
                                                                                     _|

            """
        )
    string="Tool created by - Ujala Tyagi & Tanvi Singh"
    for char in string:
        print(char,end='')
        sys.stdout.flush()
        time.sleep(0.05)
    print()
    mytext = "Welcome to Infosysint"
    print(mytext)
    while True:
        reconinput()
