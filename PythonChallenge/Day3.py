import requests
import os
#os 쓰기 싫으면 print("\x1B[H\x1B[J") 사용하기!

saved_urlList = []
http = "http://"
loop_value = True

while loop_value:
    userinput_urlList = input("Please write a URL or URLs you want to check. (separated by comma)\n").split(",")

    for x in userinput_urlList:
        if x.islower() == False:
            x = x.lower()
        else:
            pass

        if http in x:
            pass
        else:
            x = http + x

        if "." in x:
            pass
        else:
            print("invailable URL")
            continue

        if " " in x:
            x = x.replace(" ","")
            saved_urlList.append(x)
        else:
            saved_urlList.append(x)

    for z in saved_urlList:

        web_url = z
            
        try:
            web_url_result = requests.get(web_url)
            if web_url_result.status_code == 200:
                print(f"{web_url} is up!")
            else:
                print(f"{web_url} is down!")
        except:
            print(f"{web_url} is down!")
    
    saved_urlList = []

    restartFunction = input("Do you want to start over? y / n")

    if restartFunction == "y":
        os.system('cls')
        continue
    elif restartFunction == "n":
        os.system('cls')
        break
    else:
        restartFunction = input("Plz input again. y / n")
        if restartFunction == "y":
            os.system('cls')
            continue
        elif restartFunction == "n":
            os.system('cls')
            break