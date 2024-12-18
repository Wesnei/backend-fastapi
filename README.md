# 👨🏻‍💻 Projeto FastAPI: API de Gerenciamento de Cursos

## 📄 Descrição do Projeto
Esta API, desenvolvida utilizando **FastAPI**, oferece uma plataforma robusta e eficiente para gerenciar um catálogo de **cursos**, **alunos** e **professores**. Com suporte completo para operações **CRUD** (Create, Read, Update, Delete), a API permite realizar as seguintes operações:

- Adicionar, listar, atualizar e excluir **cursos**.
- Gerenciar dados de **alunos**, incluindo adição, listagem, atualização e remoção.
- Administrar informações de **professores**, com as mesmas funcionalidades de CRUD.

Esta aplicação proporciona uma estrutura simples, mas poderosa, para um gerenciamento eficaz de dados em um sistema educacional.

## 🚀 Tecnologias Utilizadas
- **Python 3.10+** - A linguagem de programação escolhida para o projeto.
- **FastAPI** - Framework para criação de APIs rápidas e eficientes.
- **Uvicorn** - Servidor ASGI para rodar a aplicação FastAPI.
- **PostgreSQL** - Banco de dados relacional utilizado para armazenar os dados.
- **Postman** - Ferramenta para testar as rotas da API durante o desenvolvimento.

## 📦 Como Executar

### Pré-requisitos
Antes de rodar a API, é necessário garantir que você tenha os seguintes pré-requisitos instalados em sua máquina:

- **Python 3.10+**
- **PostgreSQL** em funcionamento

### Criar e Ativar um Ambiente Virtual (venv)
É recomendado criar um ambiente virtual para isolar as dependências do projeto e evitar conflitos com outras bibliotecas do seu sistema. Para isso, siga os passos abaixo:

1. No terminal, navegue até o diretório do seu projeto e execute o seguinte comando para criar um ambiente virtual:

    ```bash
    python -m venv venv
    ```

2. Para ativar o ambiente virtual:

    - **No Windows**:
    ```bash
    .\venv\Scripts\activate
    ```

    - **No macOS/Linux**:
    ```bash
    source venv/bin/activate
    ```

### Instalar as Dependências
Com o ambiente virtual ativado, instale as dependências necessárias para o projeto com o seguinte comando:

```bash
pip install -r requirements.txt
```

### Configurar o Banco de Dados PostgreSQL

1. Certifique-se de ter o **PostgreSQL** instalado e em funcionamento no seu sistema.
2. Crie um banco de dados no PostgreSQL executando o seguinte comando no terminal do PostgreSQL:

    ```sql
    CREATE DATABASE nome_do_banco;
    ```

3. Crie um usuário e conceda permissões ao banco de dados com os comandos abaixo:

    ```sql
    CREATE USER nome_do_usuario WITH PASSWORD 'sua_senha';
    GRANT ALL PRIVILEGES ON DATABASE nome_do_banco TO nome_do_usuario;
    ```

### Configurar Variáveis de Ambiente
Crie um arquivo **.env** na raiz do projeto e adicione as seguintes variáveis de ambiente para configurar a conexão com o banco de dados:

```ini
DATABASE_URL=postgresql://nome_do_usuario:sua_senha@localhost/nome_do_banco
```

## 🚀 Como Rodar a API

### Iniciar o Servidor Uvicorn
Após configurar o ambiente e as dependências, inicie o servidor da API com o seguinte comando:

```bash
uvicorn app.main:app --reload
```

A API estará disponível localmente em `http://localhost:8000`. O parâmetro `--reload` permite que as mudanças no código sejam automaticamente aplicadas durante o desenvolvimento.

### Testar as Rotas com Postman
Use o **Postman** ou qualquer outra ferramenta de API para testar as rotas da aplicação. Aqui estão as principais rotas disponíveis na API:

### **Rotas de Cursos**  
- **GET /cursos** – Listar todos os cursos cadastrados.
- **POST /cursos** – Adicionar um novo curso.
- **PUT /cursos/{id}** – Atualizar um curso existente.
- **DELETE /cursos/{id}** – Deletar um curso específico.

## 📄 Contribuição
Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, siga os passos abaixo:

1. Faça um **fork** do repositório.
2. Crie uma nova **branch** (git checkout -b feature/nome-da-sua-feature).
3. Faça suas alterações e realize o **commit** (git commit -m 'Adicionando nova feature').
4. Envie para o repositório remoto (git push origin feature/nome-da-sua-feature).
5. Abra um **Pull Request** para revisão e possível merge.

## 📞 Contato
Para dúvidas, sugestões ou contribuições, entre em contato através do e-mail: **wesneipaiva@gmail.com**
