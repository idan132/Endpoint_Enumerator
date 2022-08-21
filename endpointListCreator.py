# Endpoint List Creator
# Description: Enter your target's URL and get a clean list of endpoints to test and scan
# Writer: W1ld_Hunt3r
#_________________________________________________________________________________________


import requests
import sys
print(r"""
           
                                                                                                                                        
,------.           ,--.            ,--.          ,--.      ,------.                                                ,--.                 
|  .---',--,--,  ,-|  |,---. ,---. `--',--,--, ,-'  '-.    |  .---',--,--, ,--.,--.,--,--,--.,---. ,--.--.,--,--.,-'  '-. ,---. ,--.--. 
|  `--, |      \' .-. | .-. | .-. |,--.|      \'-.  .-'    |  `--, |      \|  ||  ||        | .-. :|  .--' ,-.  |'-.  .-'| .-. ||  .--' 
|  `---.|  ||  |\ `-' | '-' ' '-' '|  ||  ||  |  |  |      |  `---.|  ||  |'  ''  '|  |  |  \   --.|  |  \ '-'  |  |  |  ' '-' '|  |    
`------'`--''--' `---'|  |-' `---' `--'`--''--'  `--'      `------'`--''--' `----' `--`--`--'`----'`--'   `--`--'  `--'   `---' `--'    
,-----.               `-,--.   ,--.                     ,-----.,--.                                                                     
|  |) /_,--. ,--.--.    |  | ,-|  | ,--,--.,--,--,     '  .--./|  ,---. ,---. ,--,--,                                                   
|  .-.  \\  '  /'--'    |  |' .-. |' ,-.  ||      \    |  |    |  .-.  | .-. :|      \                                                  
|  '--' / \   ' .--.    |  |\ `-' |\ '-'  ||  ||  |    '  '--'\|  | |  \   --.|  ||  |                                                  
`------'.-'  /  '--'    `--' `---'  `--`--'`--''--'     `-----'`--' `--'`----'`--''--'                                                  
        `---'                                                                                                                           
                 
""")
def start():
    scan_type = input("Choose Scan Type\n________________ \n\n 1- Single Target \n 2- Subdomain List \n\n Your Choice: ")

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
        


    #Subdomain list scan, user enters a path to subdomain list text file
    elif scan_type == "2":
        print("\n\n Still In Development... \n\n")
        start()

    else:
        print("\n Invalid Input, Please Choose A Number From The Menu \n")
        start()


if __name__ == "__main__":
    start()


