## Mini treinamento em GIT para os bolsistas/voluntários do Laboratório de Inovação Tecnológica - IFCE.

### Objetivos:
Abordar conceitos básicos, seguindo a documentação e aplicando neste simples projeto em python.

O código neste repositório mostra como consumir uma API Rest, utilizando a biblioteca requests, em python.


### Requisitos:
- Git
- Python ^3.6
- Virtualenv ^15.1
- Bash
- Editor de texto (preferível VSCode)
- Rodar pelo menos uma vez na vida "man git" ou "git --help"

### Rodando o código
Clone o projeto e entre na pasta
```
git clone https://github.com/IsaiasDimitri/minitreinamento-em-git.git
cd minitreinamento-em-git
```
Dentro da pasta raiz
```
virtualenv -p python3 .env
. .env/bin/activate
pip install -r requirementes.txt
```
### Tópicos:
- Porque Git?

- Pedindo ajuda

- Iniciando um repositório
   - o que é um repositorio?
   - workflow
       - git clone   (clonar um repositorio que já existe)
       - git init    (repositorio vazio ou num que já existe)
       - git remote add ["nome do link"] ["link do repositorio"] (aponta para um repositorio remoto)
       - git diff    (ver alteraçoes...)
       - git add -p   (salva as alterações)
       - git reset -p    (descarta as alterações)
       - git commit (identifica as mudanças com um hash e dá um comentário)
       - git push    (se houver um repositorio remoto, empurra as mudanças para lá)

- Branchs
    - o que é uma branch?
        linha principal -> master + ramificações

    - convenções
        - master
        - develop
        - feature
        - hotfix
    
    - comandos
        - git branch -l (lista as branchs locais)
        - git branch ["nome da branch aqui"] (criar branch)
        - git checkout ["nome da branch aqui"] (caminhar pelas branchs)
        - git branch -D ["nome da branch aqui"] (deletar branch)
        - git branch -C ["nome da branch aqui"] ["nome da nova branch"] (copiar branch)
        - git branch -M ["nome da branch aqui"] ["nome da nova branch"] (mover branch)

- Commits
    - o que é um commit?
    - listando commits
        - git log ou git log --oneline
    - boas práticas ao commitar
        - mensagens de log
    - quando usar o .gitignore

- Merge
    - o que é um merge?
    - executando um merge 
    - merge request



### Fontes:
- Documentações: 
    - Git https://git-scm.com/docs

    - Requests https://pypi.org/project/requests/

- Artigo Convenções para Branchs https://medium.com/@lucianoratamero/git-e-github-parte-3-boas-pr%C3%A1ticas-de-organiza%C3%A7%C3%A3o-de-branches-lucianoratamero-4d786c759bd2

- Boas práticas https://python-guide-pt-br.readthedocs.io/pt_BR/latest/
