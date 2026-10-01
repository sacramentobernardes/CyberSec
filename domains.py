import requests
import sys

file = open('WordLists/subdomains100.txt')

url = sys.argv[1]

# lista = ["admin","login", "css", "sport", "shop"]
print("")
print("Caso queira parar a ferramenta aperte 'ctrl + Z'.")
print("")

for line in file:
    
    line = line.strip()
    dns_check = f"https://{url}/{line}"

    try:
        r = requests.get(dns_check)
        print(dns_check + " " + str(r.status_code))
    except:
        continue