import pandas as pd
import camelot
import cv2
import phonenumbers
from phonenumbers import geocoder
from urllib import request
import requests
import os
import hashlib
import encodings
# wikipedia web tables
# simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')
# sesonOne = simpsons[1]
# print(sesonOne,simpsons[2])
# print(len(simpsons))

# open cmd 

cmd = 'date'

cwd = os.getcwd()
print(cwd)
ping ="ping"

# reading cvs file from website
# footballData = pd.read_csv("https://www.football-data.co.uk/mmz4281/2324/E0.csv")
# print(footballData)
# footballData.rename(columns={'AwayTeam':'Team','HomeTeam':'Away'} , inplace=True)
# print(footballData)

# reding pdf file with camleot frame..

# tables = camelot.read_pdf("foo.pdf", pages="1")
# print(tables)

# phone numbers

# noVar = phonenumbers.parse("+48518774622",None)
# geo = geocoder.description_for_number(noVar,"en")
# print(geo,noVar)
# 
# currency exchange rate json

# moneyA = requests.get("http://api.nbp.pl/api/exchangerates/tables/A")
# moneyB = requests.get("http://api.nbp.pl/api/exchangerates/tables/B")
# moneyC = requests.get("http://api.nbp.pl/api/exchangerates/tables/C")

# # print(moneyA.json())
# # print(moneyB.json())
# print(moneyC.json())

class expClass:
    name ="john"
    lastname = "doe"
a = expClass()

x = "aaa"
urlTxt = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords-1000.txt'

local_file = 'local_copy.txt'

pathTxt = './local_copy.txt' 



def exp():
    local_file = 'local_copy.txt'

    pathTxt = './local_copy.txt' 
    if os.path.exists(pathTxt) == True:
        with open('./local_copy.txt') as file:
            lines = [line.strip() for line in file]

        print(lines)
    
    else:
        take = request.urlretrieve(urlTxt, local_file)
        print(take)

def convert_text_to_sha1(password):
    # /////////////////////////////////////////?????????
    digest = hashlib.sha1(password.encode()).hexdigest()
    print(digest)
    return digest

def main():
    user_dha1 = input("Enter the SHA1 password to Crack:")
    cleaned_user_sha1 = user_dha1.strip().lower()

    with open('./local_copy.txt') as f:
        for line in f:
            password = line.strip()
            converted_sha1 = convert_text_to_sha1(password) 
            if cleaned_user_sha1 == converted_sha1:
                print("converted password:{password}")
                return
    print("not_pass")        

if __name__ == '__main__':
    main()