# Endpoint List Creator
# Description: Enter your target's URL and get a clean list of endpoints to test and scan
# Writer: W1ld_Hunt3r
#_________________________________________________________________________________________

import time
import requests
import sys
print(r"""
           
                                                                                                                                        

 __    __     _                            _____          ___           _                  
/ / /\ \ \___| | ___ ___  _ __ ___   ___  /__   \___     / __\   _  ___| | ___  _ __   ___ 
\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \   / /\/ _ \   / / | | | |/ __| |/ _ \| '_ \ / _ \
 \  /\  /  __/ | (_| (_) | | | | | |  __/  / / | (_) | / /__| |_| | (__| | (_) | | | |  __/
  \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \/   \___/  \____/\__, |\___|_|\___/|_| |_|\___|
                                                             |___/                         
                                                        
                 
""")
ok_count = 0
response_data = ""
headers = {'User-Agent': 'Googlebot'}

def start():
    action = input("What would you like to do? \n\n 1- Generate endpoint wordlist \n 2- Crawl the application \n\n Your Choice: ")
    
    #action 1 - just generate an endpoint wordlist
    if action == "1":
        scan_type = input("\n Choose Scan Type\n________________ \n\n 1- Single Target \n 2- Subdomain List \n\n Your Choice: ")

        #Single target scan, user enters a single URL
        if scan_type == "1":    
            target = input("Enter Target URL: ")
            path = input("Enter Path To Save Output file: ")
            URL = target + r"/robots.txt" 
            r = requests.get(URL)

            with open(path+'/endpointWordlist.txt', 'w') as file:
                file.write(r.text)
            file.close

            f = open(path+"/endpointWordlist.txt", "r+")
            new_file = []
            for line in f:
                line = line.replace("*","")
    
                if "Allow: " in line:
                    only_endpoint = line.split("Allow: ")
                    new_file.append(only_endpoint[1])

                elif "Disallow: " in line:
                    only_endpoint = line.split("Disallow: ")
                    new_file.append(only_endpoint[1])
        
        
            with open(path+"/endpointWordlist.txt", "w+") as f:
                for i in new_file:
                    f.write(i+"\n")
        
            f.close()

        #Subdomain list scan, user enters a path to subdomain list text file
        elif scan_type == "2":
            print("\n\n Still In Development... \n\n")
            start()

        else:
            print("\n Invalid Input, Please Choose A Number From The Menu \n")
            start()
    
    #action 2 - crawl and print response code
    if action == "2":
        scan_type = input("\n Choose Scan Type\n________________ \n\n 1- Single Target \n 2- Subdomain List \n\n Your Choice: ")

        #Single target scan, user enters a single URL
        if scan_type == "1":    
            target = input("Enter Target URL: ")
            path = input("Enter Path To Save Output file: ")
            URL = target + r"/robots.txt" 
            r = requests.get(URL)

            with open(path+'/endpointWordlist.txt', 'w') as file:
                file.write(r.text)
            file.close

            f = open(path+"/endpointWordlist.txt", "r+")
            new_file = []
            for line in f:
                line = line.replace("*","")
    
                if "Allow: " in line:
                    only_endpoint = line.split("Allow: ")
                    new_file.append(only_endpoint[1])

                elif "Disallow: " in line:
                    only_endpoint = line.split("Disallow: ")
                    new_file.append(only_endpoint[1])
        
        
            with open(path+"/endpointWordlist.txt", "w+") as f:
                for i in new_file:
                    f.write(i+"\n")
        
            f.close()
            f2 = open(path+"/endpointWordlist.txt", "r+")
            for line in f2:
                r = ''
                while r == '':
                    try:
                        print("Trying to GET " + target + line)
                        r = requests.get((target+line), headers=headers)
                        print("Response Code: "+ r + "\n\n")
                        break

                    except:
                        print("\n\nConnection refused by the server...")
                        print("Let me sleep for 5 seconds")
                        print("ZZzzzz...")
                        time.sleep(5)
                        print("Was a nice sleep, now let me continue... \n\n")
                        break


if __name__ == "__main__":
    start()


