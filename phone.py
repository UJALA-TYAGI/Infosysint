import requests

cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
Y = '\033[1;33;40m'
def number():
    phonenum = input("Enter Mobile Number with country code >> ")
    key = "your key here"
    url = ("http://apilayer.net/api/validate?access_key="+key+"&number="+phonenum
    # url = ("https://api.telnyx.com/anonymous/v2/number_lookup/" + phonenum)
    resp = requests.get(url)
    details = resp.json()
    print('')
    print(cyan+"Country : "+ details["country_name"])
    print(cyan+"Location : "+ details["location"])
    print(cyan+"Carrier : "+ details["carrier"])
    print(cyan+"Line Type: "+ details["line_type"])

if __name__=="__main__":
    number()
