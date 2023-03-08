import streamlit as st
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

#here i specify the secrets from streamlit which i need to connect to the database
db_user = st.secrets.MySQLcredentials.user
db_pw = st.secrets.MySQLcredentials.password
db_host = st.secrets.MySQLcredentials.host
db_port = st.secrets.MySQLcredentials.port
db_name_users = st.secrets.MySQLcredentials.users_dbname
db_name_data = st.secrets.MySQLcredentials.data_dbname

#connection string for users database with sqlalchemy
conn_string_users = f"mysql+mysqlconnector://{db_user}:{db_pw}@{db_host}:{db_port}/{db_name_users}"
engine_users = create_engine(conn_string_users)

#and here i make the string for the data from the sawmill's cameras
conn_string_data = f"mysql+mysqlconnector://{db_user}:{db_pw}@{db_host}:{db_port}/{db_name_data}"
engine_data = create_engine(conn_string_data)

#creates sqlalchemy session to manage database transactions
Session_users = sessionmaker(bind=engine_users)
session_users = Session_users()

#creates sqlalchemy instance to reflect data from unknown tables from provided database
metadata = MetaData()
metadata.reflect(bind=engine_data)

