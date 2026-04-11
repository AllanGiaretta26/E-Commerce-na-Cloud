# 🛒 E-CommerceCloud

Aplicação completa de cadastro e visualização de produtos para e-commerce, desenvolvida com **Streamlit** no frontend, **SQL Server** para persistência de dados e **Azure Blob Storage** para armazenamento de imagens.

![Tela do app](assets/screenshot.png)

---

## ✨ Funcionalidades

- ✅ Cadastro de produtos com nome, preço, descrição e imagem
- ☁️ Upload automático de imagens para Azure Blob Storage
- 💾 Persistência de dados em SQL Server
- 📋 Listagem visual de produtos cadastrados
- 🔒 Configuração segura via variáveis de ambiente

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|------------|-----------|
| **Python 3.9+** | Linguagem principal |
| **Streamlit** | Framework para interface web interativa |
| **Azure Blob Storage** | Armazenamento de imagens na nuvem |
| **SQL Server** | Banco de dados relacional |
| **python-dotenv** | Gerenciamento de variáveis de ambiente |

**Bibliotecas principais:**
- `streamlit` - Interface web
- `azure-storage-blob` - SDK do Azure Blob Storage
- `pymssql` - Driver para SQL Server
- `python-dotenv` - Carregamento de `.env`

---

## 📋 Pré-requisitos

- Python 3.9 ou superior
- SQL Server instalado e acessível
- Conta Azure Storage com container Blob configurado
- Credenciais de acesso ao banco e storage

---

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd E-CommerceCloud
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuração

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
# Azure Blob Storage
BLOB_ACCOUNT_NAME=seu_blob_account
BLOB_CONTAINER_NAME=seu_container
# Pode ser a connection string completa OU somente a account key
BLOB_CONNECTION_STRING=sua_connection_string_ou_account_key

# SQL Server
SQL_SERVER=seu_servidor
SQL_DATABASE=seu_banco
SQL_USER=seu_usuario
SQL_PASSWORD=sua_senha
```

> ⚠️ **Importante:** Nunca adicione o arquivo `.env` ao versionamento (já incluído no `.gitignore`).

---

## 🗄️ Configuração do Banco de Dados

Execute o script SQL abaixo para criar a tabela de produtos:

```sql
CREATE TABLE Produtos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome NVARCHAR(255),
    descricao NVARCHAR(MAX),
    preco DECIMAL(18,2),
    imagem_url NVARCHAR(2083)
);
```

---

## ▶️ Como Executar

Inicie a aplicação com o comando:

```bash
streamlit run main.py
```

A aplicação abrirá automaticamente no seu navegador padrão (geralmente em `http://localhost:8501`).

---

## 📖 Uso

1. **Cadastrar Produto:**
   - Preencha os campos: nome, preço e descrição
   - Selecione uma imagem para o produto
   - Clique em `Cadastrar Produto`

2. **Visualizar Produtos:**
   - Clique em `Visualizar Produtos` na sidebar
   - Veja todos os produtos cadastrados com suas imagens

---

## 🏗️ Estrutura do Projeto

```
E-CommerceCloud/
├── assets/
│   └── screenshot.png      # Captura de tela da aplicação
├── main.py                 # Código principal da aplicação
├── requirements.txt        # Dependências Python
├── .env                    # Variáveis de ambiente (não versionado)
├── .gitignore              # Arquivos ignorados pelo Git
└── README.md               # Este arquivo
```

---

## ⚠️ Solução de Problemas

| Problema | Solução |
|----------|---------|
| **Erro de conexão com Blob Storage** | Verifique se `BLOB_ACCOUNT_NAME`, `BLOB_CONTAINER_NAME` e `BLOB_CONNECTION_STRING` estão corretos |
| **Erro de conexão com SQL Server** | Confirme se o servidor está acessível e as credenciais no `.env` estão corretas |
| **Imagem não aparece na listagem** | Verifique se o container Blob está público ou com SAS token configurado |
| **Módulo não encontrado** | Execute `pip install -r requirements.txt` novamente com o venv ativo |

---

## 🔒 Boas Práticas de Segurança

- ✅ Mantenha o arquivo `.env` fora do versionamento
- ✅ Use contas de storage com acesso restrito
- ✅ Configure regras de firewall no SQL Server
- ✅ Rotação periódica de chaves e senhas
- ✅ Use variáveis de ambiente em produção ao invés de `.env`

---

## 📝 Licença

Este projeto é open-source. Sinta-se livre para usar e modificar.

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para sugerir melhorias ou reportar bugs:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 👤 Autor
Desenvolvido por Allan Giaretta
