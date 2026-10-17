import requests
import sys

if len(sys.argv) < 3:
    print("Uso correto: python3 domains.py <url> <wordlist>")
    sys.exit(1)

url = sys.argv[1]
wordlist = sys.argv[2]

try:
    with open(wordlist, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"Erro: O arquivo de wordlist '{wordlist}' não foi encontrado.")
    sys.exit(1)

print("")
print(f"Iniciando testes em: {url} ({len(lines)} itens carregados)")
print("Pressione 'Ctrl + C' para interromper a execução.")
print("")

for line in lines:
    line = line.strip()
    if not line:
        continue
        
    dns_check = f"http://{url}/{line}/"

    try:
        r = requests.get(dns_check, timeout=5, allow_redirects=False)
        print(f"{dns_check} -> Status: {r.status_code}")
    except requests.exceptions.RequestException as e:
        #print(f"{dns_check} -> Falha na requisição ({e})")
        #ou 
        continue
      