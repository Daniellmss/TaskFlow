# TaskFlow

Um gerenciador de tarefas pessoal desenvolvido com Python e Django.

## Sobre o projeto

O TaskFlow é uma aplicação web criada para facilitar a organização e o acompanhamento de tarefas do dia a dia.

## Funcionalidades

- Cadastro de tarefas.
- Listagem de tarefas.
- Edição de tarefas.
- Definição de prioridade.
- Conclusão e reabertura de tarefas.
- Exclusão de tarefas com confirmação.

## Tecnologias utilizadas

- Python
- Django
- SQLite
- HTML5

## Como executar

1. Clonar o repositório.
    - Para clonar o repositório abra seu terminal e execute o comando abaixo:  
    ```bash
    git clone URL_DO_REPOSITORIO
    cd TaskFlow
    ```
2. Criar o ambiente virtual.
    - Para criação do ambiente virtual abra seu terminal e execute o comando abaixo:  
    ```powershell
    python -m venv .venv
    ```
3. Ativar o ambiente virtual.
    - Para ativação do ambiente virtual abra seu terminal e execute o comando abaixo:  
    ```powershell
    .venv\Scripts\Activate.ps1
    ```
4. Instalar as dependências
    - Para instalação das dependências abra seu terminal e execute o comando abaixo:  
    ```powershell
    pip install -r requirements.txt
    ```
5. Aplicar as migrações.
    - Para aplicar as migrações abra seu terminal e execute o comando abaixo:  
    ```powershell
    python manage.py migrate
    ```
6. Iniciar o servidor Django.
    - Para inicializar o servidor Django abra seu terminal e execute o comando abaixo:  
    ```powershell
    python manage.py runserver
    ```