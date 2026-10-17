# 🔍 CyberSec Toolkit

> Ferramentas de reconhecimento web em Python — enumeração de diretórios, subdomínios e WHOIS.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Topic](https://img.shields.io/badge/Topic-Reconnaissance-green?style=flat-square)
![Warning](https://img.shields.io/badge/⚠-Uso%20ético%20apenas-orange?style=flat-square)

---

## Sobre

Coleção de scripts Python para reconhecimento passivo e ativo de alvos web. Voltada para estudos de *bug bounty*, CTFs e testes de penetração autorizados. Inclui ferramentas de força-bruta de diretórios, enumeração de subdomínios e consulta WHOIS, além de wordlists prontas para uso.

---

## Ferramentas

### `domains.py`
Brute-force de caminhos e diretórios via requisição HTTP. Versão inicial, sem timeout nem validações extras.
- Protocolo: HTTPS
- Estratégia: wordlist → GET por caminho → exibe status code

### `DomainsV2.py` *(recomendada)*
Versão aprimorada: valida argumentos, trata erros de arquivo, timeout de 5 s por requisição e ignora redirecionamentos.
- Protocolo: HTTP (com `allow_redirects=False`)
- Timeout: 5 segundos por requisição
- Validações: argumentos e existência da wordlist

### `subdomains.py`
Enumeração de subdomínios por wordlist. Testa `subdomain.alvo.com` via GET e reporta o status HTTP de cada resposta.
- Protocolo: HTTPS
- Formato testado: `https://<palavra>.<alvo>`

### `whois.py`
Wrapper simples sobre o comando `whois` do sistema. Passa o alvo como argumento e imprime o resultado no terminal.

---

## Uso

**Enumeração de diretórios (v2 — recomendada)**
```bash
python3 DomainsV2.py <alvo> <wordlist>

# Exemplo:
python3 DomainsV2.py exemplo.com WordLists/raft-small-directories.txt
```

**Enumeração de subdomínios**
```bash
python3 subdomains.py <alvo> <wordlist>

# Exemplo:
python3 subdomains.py exemplo.com WordLists/subdomains100.txt
```

**Consulta WHOIS**
```bash
python3 whois.py <alvo>

# Exemplo:
python3 whois.py exemplo.com
```

---

## WordLists

| Arquivo | Entradas | Uso indicado |
|---|---|---|
| `subdomains100.txt` | 100 | Testes rápidos e CTFs |
| `common.txt` | 4 752 | Diretórios e arquivos comuns |
| `raft-small-directories.txt` | 20 115 | Fuzzing de diretórios (médio) |
| `subdomains-1million.txt` | 110 000 | Enumeração abrangente de subdomínios |

---

## Instalação

**1. Clone o repositório**
```bash
git clone https://github.com/sacramentobernardes/CyberSec.git
cd CyberSec
```

**2. Instale a dependência**
```bash
pip install requests
```

**3. Execute qualquer ferramenta** conforme os exemplos acima.

---

## Estrutura do Repositório

```
CyberSec/
├── domains.py                    # Brute-force de diretórios (v1)
├── DomainsV2.py                  # Brute-force de diretórios (v2)
├── subdomains.py                 # Enumeração de subdomínios
├── whois.py                      # Consulta WHOIS
├── GIT_GUIDE.md                  # Guia de uso do Git
└── WordLists/
    ├── subdomains100.txt
    ├── common.txt
    ├── raft-small-directories.txt
    └── subdomains-1million.txt
```

---

## ⚠ Aviso Legal

> **Uso ético e autorizado apenas.**
>
> Estas ferramentas destinam-se exclusivamente a ambientes controlados, programas de *bug bounty* com escopo definido e testes de penetração com autorização expressa do proprietário do sistema. O uso não autorizado contra sistemas de terceiros é ilegal e sujeito a penalidades civis e criminais.
