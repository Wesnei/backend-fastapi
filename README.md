
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
- **Docker** - Utilizado para containerizar a aplicação e o banco de dados.
- **Jinja2** - Utilizado para criar templates na interface da API.


## 📦 Como Executar

### Pré-requisitos
Antes de rodar a API, é necessário garantir que você tenha os seguintes pré-requisitos instalados em sua máquina:

- **Docker** (para rodar os containers da aplicação e do banco de dados)
- **Docker Compose** (para orquestrar os containers)

Se preferir rodar localmente, você pode seguir as instruções para criar o ambiente Python manualmente.

### 1. Criar e Ativar um Ambiente Virtual (venv)
Se você for rodar a aplicação **sem Docker**, crie um ambiente virtual:

```bash
python -m venv venv
```

- **No Windows**:
```bash
.\venv\Scripts\activate
```

- **No macOS/Linux**:
```bash
source venv/bin/activate
```

### 2. Instalar as Dependências
Com o ambiente virtual ativado, instale as dependências necessárias para o projeto:

```bash
pip install -r requirements.txt
```

### 3. Configurar o Banco de Dados PostgreSQL
Se você não estiver usando Docker para o banco de dados, certifique-se de ter o **PostgreSQL** instalado e funcionando. Crie um banco de dados e usuário com as permissões necessárias.

---

### 🐳 **Rodando o Projeto com Docker**

Se você deseja rodar a aplicação com **Docker**, siga as instruções abaixo.

### Passo 1: Criar Arquivos Docker

#### **Dockerfile**

```Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### **docker-compose.yml**

```yaml
version: "3.9"
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: fastapi-app
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/fastAPI
    depends_on:
      - db
    volumes:
      - .:/app

  db:
    image: postgres:17
    container_name: postgres-db
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
      POSTGRES_DB: fastAPI
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### Passo 2: Rodar o Projeto

1. **Construir e Rodar os Containers**: Utilize o comando abaixo para construir as imagens e rodar os containers.

```bash
docker-compose up --build
```

2. **Acessar a API**: Após os containers estarem rodando, a aplicação estará disponível em [http://localhost:8000](http://localhost:8000).

---

## 🚀 Como Testar as Rotas com Postman

Use o **Postman** ou qualquer outra ferramenta de API para testar as rotas da aplicação. Aqui estão as principais rotas disponíveis na API:

### **Rotas de Cursos**  
- **GET /cursos** – Listar todos os cursos cadastrados.
- **POST /cursos** – Adicionar um novo curso.
- **PUT /cursos/{id}** – Atualizar um curso existente.
- **DELETE /cursos/{id}** – Deletar um curso específico.

---

## 📄 Contribuição
Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, siga os passos abaixo:

1. Faça um **fork** do repositório.
2. Crie uma nova **branch** (git checkout -b feature/nome-da-sua-feature).
3. Faça suas alterações e realize o **commit** (git commit -m 'Adicionando nova feature').
4. Envie para o repositório remoto (git push origin feature/nome-da-sua-feature).
5. Abra um **Pull Request** para revisão e possível merge.

---

## 📞 Contato
Para dúvidas, sugestões ou contribuições, entre em contato através do e-mail: **wesneipaiva@gmail.com**
