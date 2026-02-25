import streamlit as st
from azure.storage.blob import BlobServiceClient
import os
import pymssql
import uuid
from dotenv import load_dotenv

# Carrega variaveis do arquivo .env para o ambiente
load_dotenv()


def normalize_env(name):
    # Remove espacos e aspas extras para evitar erros de configuracao
    value = os.getenv(name)
    if value is None:
        return None
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
        value = value[1:-1]
    return value.strip()


# Configuracoes de Blob e SQL vindas do .env
blob_account_name = normalize_env("BLOB_ACCOUNT_NAME")
blob_container_name = normalize_env("BLOB_CONTAINER_NAME")
blob_connection_value = normalize_env("BLOB_CONNECTION_STRING")

SQLServer = normalize_env("SQL_SERVER")
SQLDatabase = normalize_env("SQL_DATABASE")
SQLUser = normalize_env("SQL_USER")
SQLPassword = normalize_env("SQL_PASSWORD")


def build_blob_connection_string():
    # Aceita tanto a connection string completa quanto apenas a account key
    if not blob_connection_value:
        return None
    lowered = blob_connection_value.lower()
    if "accountname=" in lowered and "accountkey=" in lowered:
        return blob_connection_value
    if not blob_account_name:
        return None
    return (
        "DefaultEndpointsProtocol=https;"
        f"AccountName={blob_account_name};"
        f"AccountKey={blob_connection_value};"
        "EndpointSuffix=core.windows.net"
    )


def get_sql_connection():
    # Garante que as credenciais estejam presentes antes de conectar
    missing = []
    if not SQLServer:
        missing.append("SQL_SERVER")
    if not SQLDatabase:
        missing.append("SQL_DATABASE")
    if not SQLUser:
        missing.append("SQL_USER")
    if not SQLPassword:
        missing.append("SQL_PASSWORD")
    if missing:
        raise ValueError(f"Variaveis ausentes no .env: {', '.join(missing)}")
    return pymssql.connect(server=SQLServer, user=SQLUser, password=SQLPassword, database=SQLDatabase)


def cadastrar_produto(product_name, product_price, product_description, product_image):
    # Valida formulario e executa upload + insert no banco
    if not product_name or not product_description or not product_image or product_price <= 0:
        st.warning("Por favor, preencha todos os campos e faca upload da imagem do produto.")
        return

    blob_connection_string = build_blob_connection_string()
    if not blob_connection_string or not blob_container_name or not blob_account_name:
        st.error("Configuracao do Blob Storage incompleta no .env.")
        return

    try:
        # Upload da imagem para o Blob Storage
        blob_service_client = BlobServiceClient.from_connection_string(blob_connection_string)
        blob_client = blob_service_client.get_blob_client(
            container=blob_container_name,
            blob=f"{uuid.uuid4()}_{product_image.name}",
        )
        blob_client.upload_blob(product_image, overwrite=True)
        image_url = (
            f"https://{blob_account_name}.blob.core.windows.net/"
            f"{blob_container_name}/{blob_client.blob_name}"
        )

        # Insert do produto no SQL Server
        conn = get_sql_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Produtos (nome, descricao, preco, imagem_url) VALUES (%s, %s, %s, %s)",
            (product_name, product_description, product_price, image_url),
        )
        conn.commit()
        cursor.close()
        conn.close()

        st.success("Produto cadastrado com sucesso!")
    except Exception as e:
        st.error(f"Erro ao cadastrar o produto: {e}")


def visualizar_produtos():
    # Le produtos do banco e renderiza na tela
    try:
        conn = get_sql_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT nome, descricao, preco, imagem_url FROM Produtos")
        products = cursor.fetchall()
        cursor.close()
        conn.close()

        if not products:
            st.info("Nenhum produto cadastrado.")
            return

        for product in products:
            st.subheader(product[0])
            st.write(f"Preco: R${product[2]:.2f}")
            st.write(product[1])
            st.image(product[3], width=200)
    except Exception as e:
        st.error(f"Erro ao carregar os produtos: {e}")


# Interface principal
st.title("Cadastro do Produtos")

product_name = st.text_input("Digite o nome do produto:")
product_price = st.number_input("Digite o preco do produto", min_value=0.0, step=0.01)
product_description = st.text_area("Digite a descricao do produto:")
product_image = st.file_uploader("Faca upload da imagem do produto:", type=["jpg", "jpeg", "png"])

if st.button("Cadastrar Produto"):
    cadastrar_produto(product_name, product_price, product_description, product_image)

st.header("Produtos Cadastrados")

if st.button("Visualizar Produtos"):
    visualizar_produtos()
