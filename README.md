# 🛠️ Configuração do Projeto:

- Clone o repositório  ->  git clone https://github.com/devrenatol/projeto-conta-bancaria.git
- Vá ate a pasta do projeto no terminal
- Configure uma virtual env para o projeto  ->  python -m venv ./venv
- Instale todas as dependencias do requirements.txt  ->  pip install -r requirements.txt
- Crie um arquivo na raiz do projeto ".env" e dentro desse arquivo coloque "SECRET_KEY = Valor da chave secreta" 
- Faça todas as migrações  ->  python manage.py makemigrations
- Efetue as migrações  ->  python manage.py migrate
- Crie um super usuario para acessar os endpoints da api  ->  python manage.py createsuperuser
- Coloque a API para rodar  ->  python manage.py runserver

# 📌 Endpoints da API:

## - Listar todas as contas bancárias: GET /contasbancarias/

Exemplo de Resposta:
```json
[
    {
        "id": 1,
        "account_number": "99999-99",
        "account_holder": "Nome da Pessoa",
        "balance": "0.00",
        "created_at": "Data da criação da conta",
        "updated_at": "Data do ultimo update da conta"
    }
]
```

Obs: /contasbancarias/?ordering=account_number  ou  /contasbancarias/?ordering=account_holder  ordena os dados pelo número da conta ou pelo nome do titular da conta. Caso nao coloque o "?ordering=" a ordenação será pelo id.

## - Receber os dados de uma conta bancária pelo seu id: GET  /contabancaria/id

Exemplo de Resposta:
```json
{
    "id": 1,
    "account_number": "99999-99",
    "account_holder": "Nome da Pessoa",
    "balance": "0.00",
    "created_at": "Data da criação da conta",
    "updated_at": "Data do ultimo update da conta"
}
```
## - Criar uma nova conta bancária: POST  /contasbancarias/

Exemplo de Requisição:
```json
{
    "account_number": "99999-99",    		# Formato correto para fazer a requisição
    "account_holder": "Nome da Pessoa",		# Nome não pode conter caracteres especiais ou números
    "balance": "0.00"
}
```
Exemplo de Resposta: "201 Created"
```json
{
    "id": 1,
    "account_number": "99999-99",
    "account_holder": "Nome da Pessoa",
    "balance": "0.00",
    "created_at": "Data da criação da conta",
    "updated_at": "Data do ultimo update da conta"
}
```
## - Modificar os dados de uma conta bancária: PUT  /contabancaria/id

Exemplo de Requisição:
```json
{
    "account_number": "88888-88",    		# Formato correto para fazer a requisição
    "account_holder": "Nome da Pessoa",		# Nome não pode conter caracteres especiais ou números
    "balance": "0.00"
}
```
Exemplo de Resposta: "200 OK"
```json
{
    "id": 1,
    "account_number": "88888-88",
    "account_holder": "Nome da Pessoa",
    "balance": "0.00",
    "created_at": "Data da criação da conta",
    "updated_at": "Data do ultimo update da conta"
}
```
## - Deletar uma conta bancária: DELETE   /contabancaria/id

Exemplo de Resposta bem sucedida: "204 No content"
Exemplo de Resposta mal sucedida: "400 Bad Request"

## - Sacar um valor de uma conta bancárica: POST   /transacao/saque/id

Exemplo de Requisição:
```json
{
    "value": "Valor a ser sacado"
}
```
Exemplo de Resposta:
```json
{
    "account_number": "88888-88",
    "account_holder": "Nome da Pessoa",
    "balance": "(balance - valor sacado)"
}
```
## - Depositar um valor em uma conta bancárica: POST  /transacao/deposito/id

Exemplo de Requisição:
```json
{
    "value": "Valor a ser depositado"
}
```
Exemplo de Resposta:
```json
{
    "account_number": "88888-88",
    "account_holder": "Nome da Pessoa",
    "balance": "(balance + valor depositado)"
}
```
## - Transferência entre contas bancáricas: POST   /transacao/transferencia/{id -> Da conta que esta mandando o valor}

Exemplo de Requisição:
```json
{
    "id": "Id da conta que esta recebendo o valor",
    "value": "Valor a ser transferido"
}
```
Exemplo de Resposta (Da conta que transferiu o valor):
```json
{
    "account_number": "88888-88",
    "account_holder": "Nome da Pessoa",
    "balance": "(balance - valor da transferência)"
}
```
