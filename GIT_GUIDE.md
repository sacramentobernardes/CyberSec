# 🎓 Mini Guia de Git

Um guia rápido para consultas diárias e comandos essenciais do Git.

> **Dica:** Se tiver dúvidas sobre um comando, use `git help <comando>` ou consulte a documentação oficial.

## 1. Configuração Inicial (Apenas uma vez)
Antes de começar, é necessário dizer ao Git quem você é. Isso evita erros de permissão e identidade nos commits.

```bash
git config --global user.name "sacramentobernardes"
git config --global user.email "sacramentobernardes@gmail.com"
```

## 2. Começando um Repositório

### Opção A: Iniciar do zero

Se você está criando um projeto novo na sua máquina:

```bash
git init
```

### Opção B: Baixar um projeto existente

Se o projeto já existe no GitHub/GitLab:

```bash
git clone [https://link-do-repositorio.git](https://link-do-repositorio.git)
```

## 3. Fluxo de Trabalho Diário (O Ciclo de Vida)

Sempre que você modificar, criar ou deletar arquivos, siga estes 4 passos:

### 1️⃣ Verificar o status

Veja quais arquivos foram modificados.

```bash
git status
```

### 2️⃣ Adicionar arquivos (Staging)

Prepare os arquivos para serem salvos.

```bash
# Adicionar um arquivo específico
git add nome_do_arquivo.py

# OU adicionar TUDO de uma vez (mais comum)
git add .
```

### 3️⃣ Salvar a versão (Commit)

Cria um "ponto na história" com uma mensagem descrevendo o que foi feito.

```bash
git commit -m "Descreva aqui o que você alterou"
```

### 4️⃣ Enviar para a nuvem (Push)

Envia suas alterações locais para o repositório remoto (GitHub).

```bash
git push origin main
# Nota: 'main' é o nome da branch principal. Antigamente usava-se 'master'.
```


## 4. Trabalhando com Branches (Ramificações)

Branches servem para trabalhar em novas funcionalidades sem quebrar o código principal.

| Comando                           | Descrição                                                     |
| --------------------------------- | ------------------------------------------------------------- |
| `git checkout -b nome-da-branch`  | Cria e entra em uma nova branch                               |
| `git checkout main`               | Volta para a branch principal                                 |
| `git branch`                      | Lista todas as branches                                       |
| `git merge nome-da-branch`        | Junta a branch criada com a principal (estando na principal)  |

---

## 5. Comandos Úteis de "Salva-Vidas"

* **Ver o histórico:**
```bash
git log --oneline
```


* **Desfazer alterações em um arquivo (antes do add):**
```bash
git checkout -- nome_do_arquivo.txt
```


* **Atualizar seu repositório local (baixar mudanças da nuvem):**
```bash
git pull
```

<br>

* **Caso de o seguinte <i>erro</i>:**

```bash
# error: Your local changes to the following files would be overwritten by merge:
#        GIT_GUIDE.md
#Please commit your changes or stash them before you merge.
#Aborting
```
**Faça:**

```bash
git checkout -- nome_do_arquivo.txt

git pull
```

<br>

### Dica para uso:
Como você costuma trabalhar com projetos em Python (como o de detecção de spam e o site de tradução), lembre-se sempre de criar um arquivo `.gitignore` na raiz do projeto. Isso evita que pastas pesadas ou arquivos de sistema subam para o Git.

**Exemplo de `.gitignore` para Python:**
```text

__pycache__/
*.pyc
venv/
.env

```
