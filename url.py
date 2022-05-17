import requests
import json
BOLD = '\033[1m'
R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'
def urlinfo():
    inurl=input("URL >> ")
    print('')
    # print('url >> '+inurl)
    api_key = 'your api key'

    print("[+] Checking URl......")

    scanurl = 'https://endpoint.apivoid.com/urlrep/v1/pay-as-you-go/?key='+api_key+'&url=https%3A%2F%2Fwww.google.com%2F'
    response = requests.get(scanurl)
    dict=response.json()

    mydict1 = []

    for i in range(len(dict['data']['report']['domain_blacklist']['engines'])):
        mydict = {}
        for key, val in dict['data']['report']['domain_blacklist']['engines'][i].items():
            if key == "name" or key == "detected":
                mydict[key] = val
        mydict1.append(mydict)


    redirection = dict['data']['report']['redirection']
    risk = dict['data']['report']['risk_score']


    print("The Threat and Detection Log for given URL : ")
    for i in mydict1:
        print(', '.join("{}: {}".format(k, v) for k, v in i.items()))


    if (redirection['found'] == False):
        print (G +"No Redirection detected")
    else :
        print(R +"Redirection Detected!!")
        print("Redirected to URL : ", redirection['url'])

    if(risk['result']==0):
        print(G+"URL is Legitimate")
    else:
        print(R+"The URL is not Legitimate")




if __name__=="__main__":
    urlinfo()
