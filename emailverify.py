import requests
import json
from gtts import gTTS
from playsound import playsound
R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'
def email():
    dictemail={}
    email=input("Email address to check >> ")
    # url="https://app.verify-email.org/api/v1/mFyMW4NCYyyI8mRcK3mIzkIYNu1BnWskMNPabWyOJU007FVH1I/verify/"+email
    url = "https://api.hunter.io/v2/email-verifier?email=" +email + "&api_key=9f32356c225abc29986cbd4eb4fb8aedd7b1e2e2"
    r=requests.get(url)
    # text = r.text
    # dictemail = json.loads(r)

    dictemail=r.json()
    # print(dictemail)
    # for key, value in dictemail.items():
    #     print(key, value)
    #     print(" ")
    #
    print("Email     : ",dictemail['meta']['params']['email'])
    print("status : ", dictemail['data']['result'])
    stat=dictemail['data']['status']
    language='en'
    if(stat):
        text="Email address found "
        # aud=gTTS(text=text,lang=language,slow=False)
        # aud.save("valid.mp3")
        # playsound("valid.mp3")
        print(text)
        print(G+"Status     : "+stat)
    else:
        text="Email address not found "
        # aud=gTTS(text=text,lang=language,slow=False)
        # aud.save("valid.mp3")
        # playsound("valid.mp3")
        print(text)
        print(R+"Status     : "+stat)
if __name__=="__main__":
    email()
