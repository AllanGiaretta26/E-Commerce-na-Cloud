# 🛒 E-CommerceCloud

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-Blob%20Storage-0078D4?logo=microsoftazure&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL%20Server-CC2927?logo=microsoftsqlserver&logoColor=white)
![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![Licença](https://img.shields.io/badge/licença-MIT-green)

> Aplicação de cadastro e visualização de produtos para e-commerce, com upload de imagens em nuvem e persistência em banco relacional.

![Tela do app](assets/screenshot.png)

---

## Descrição

O **E-CommerceCloud** é uma aplicação fullstack que permite cadastrar produtos com imagem, descrição e preço, armazenando os dados em **SQL Server** e as imagens no **Azure Blob Storage**. A interface é construída com **Streamlit**, oferecendo uma experiência simples tanto para o cadastro quanto para a visualização dos produtos.

O projeto demonstra a integração entre Python, banco de dados relacional e serviços de armazenamento em nuvem, sendo útil como base para protótipos de e-commerce ou estudo de aplicações com Azure.

---

## Status do Projeto

![Status](https://img.shields.io/badge/status-concluído-brightgreen)

Projeto concluído, com as funcionalidades de cadastro e listagem de produtos totalmente operacionais.

---

## Funcionalidades

- Cadastro de produtos com nome, preço, descrição e imagem
- Upload automático de imagens para Azure Blob Storage
- Persistência de dados em SQL Server
- Listagem visual dos produtos cadastrados
- Configuração via variáveis de ambiente

---

## Tecnologias

- **Python 3.9+** — linguagem principal
- **Streamlit** — interface web interativa
- **Azure Blob Storage** — armazenamento de imagens em nuvem
- **SQL Server** — banco de dados relacional
- **pymssql** — driver de conexão com o SQL Server
- **python-dotenv** — carregamento de variáveis de ambiente

---

## Pré-requisitos

- Python 3.9 ou superior
- SQL Server instalado e acessível
- Conta Azure Storage com um container Blob configurado
- Credenciais de acesso ao banco e ao storage

---

## Como Instalar e Rodar

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd E-CommerceCloud
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Linux/Mac
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

Execute o script abaixo para criar a tabela `Produtos`:

```sql
CREATE TABLE Produtos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome NVARCHAR(255),
    descricao NVARCHAR(MAX),
    preco DECIMAL(18,2),
    imagem_url NVARCHAR(2083)
);
```

### 5. Execute a aplicação

```bash
streamlit run main.py
```

A aplicação abrirá automaticamente no navegador (geralmente em `http://localhost:8501`).

---

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as variáveis abaixo:

```env
# Azure Blob Storage
BLOB_ACCOUNT_NAME=
BLOB_CONTAINER_NAME=
BLOB_CONNECTION_STRING=

# SQL Server
SQL_SERVER=
SQL_DATABASE=
SQL_USER=
SQL_PASSWORD=
```

> O campo `BLOB_CONNECTION_STRING` aceita tanto a connection string completa quanto apenas a account key. Nunca versione o `.env`.

---

## Como Usar

1. **Cadastrar produto** — preencha nome, preço, descrição, faça upload de uma imagem e clique em `Cadastrar Produto`.
2. **Visualizar produtos** — clique em `Visualizar Produtos` para listar os itens cadastrados com suas imagens.

---

## Estrutura do Projeto

```
E-CommerceCloud/
├── assets/
│   └── screenshot.png      # Captura de tela da aplicação
├── main.py                 # Código principal da aplicação
├── requirements.txt        # Dependências Python
├── .env                    # Variáveis de ambiente (não versionado)
├── .gitignore              # Arquivos ignorados pelo Git
└── README.md
```

---

## Solução de Problemas

| Problema | Solução |
|----------|---------|
| Erro de conexão com Blob Storage | Verifique se `BLOB_ACCOUNT_NAME`, `BLOB_CONTAINER_NAME` e `BLOB_CONNECTION_STRING` estão corretos |
| Erro de conexão com SQL Server | Confirme se o servidor está acessível e as credenciais no `.env` estão corretas |
| Imagem não aparece na listagem | Verifique se o container Blob está público ou com SAS token configurado |
| Módulo não encontrado | Execute `pip install -r requirements.txt` novamente com o `venv` ativo |

---

## Licença

Distribuído sob a licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.

---

## Autor

Desenvolvido por **[Allan Giaretta](https://github.com/AllanGiaretta26)**.
