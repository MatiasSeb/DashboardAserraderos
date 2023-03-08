import streamlit as st
from controllers import usersController as users
from controllers import dataController as data

backOfficeCont = st.container()
backOfficeSidebar = st.sidebar.container()

#here i create the backoffice view in streamlit, this can only be shown if the user is an admin
def backOffice():
    if st.session_state['admin'] == True & st.session_state['role'] == 1 & st.session_state['logged'] == True:
        with backOfficeSidebar+st.spinner("Cargando..."):
            st.header("Administración")
            st.header("Menú")
            st. ([["Usuarios", "Visualización resumida"]])   
            st.markdown("Selecciona una opción para administrar en la plataforma.")
            option = st.selectbox("Opciones:", ["Usuarios"], ["Visualización resumida"])
            if option == "Usuarios":
                with backOfficeCont:
                    st.header("Usuarios")
                    st.markdown("Aquí puedes administrar los usuarios de la aplicación.")
                    st.markdown("Para añadir un nuevo usuario, selecciona la opción 'Añadir nuevo usuario' en el menú")
                    option = st.selectbox("Opciones:", ["Añadir nuevo usuario", "Modificar usuario", "Eliminar usuario"])
                    if option == "Añadir nuevo usuario":
                        st.header("Añadir nuevo usuario")
                        st.markdown("Aquí puedes añadir un nuevo usuario a la aplicación.")
                        st.markdown("Para ello, introduce los datos del usuario en los campos de texto y pulsa 'Añadir'.")
                        userMail = st.text_input("Email", "")
                        name = st.text_input("Nombre", "")
                        password = st.text_input("Contraseña", "")
                        repeat_password = st.text_input("Repite la contraseña", "")
                        if(st.button("Añadir")):
                            if (len(userMail) and len(name) and len(password) > 0):
                                if(password == repeat_password):
                                    users.registerUser(userMail, name, password)
                    elif option == "Modificar usuario":
                        st.header("Modificar usuario")
                        st.markdown("Aquí puedes modificar los datos de un usuario de la aplicación.")
                        st.markdown("Para ello, introduce los datos del usuario en los campos de texto y pulsa 'Modificar'.")
                        userMail = st.text_input("Email", "")
                        name = st.text_input("Nombre", "")
                        role = st.selectbox("Rol", ["Administrador", "Operario"])
                        if(st.button("Modificar")):
                            if (len(userMail) and len(name) > 0):
                                if(role == "Administrador" or role == "Operario"):
                                    users.registerUser(userMail, name, role)
                    elif option == "Eliminar usuario":
                        st.header("Eliminar usuario")
                        st.markdown("Aquí puedes eliminar un usuario de la aplicación.")
                        st.markdown("Para ello, introduce el email del usuario en el campo de texto y pulsa 'Eliminar'.")
                        userMail = st.text_input("Email", "")
                        if(st.button("Eliminar")):
                            users.deleteUsers(userMail)
            if option == "Visualización resumida":
                with backOfficeCont:
                    st.header("Visualización resumida")
                    st.markdown("Aquí puedes configurar la visualización resumida de los datos de la aplicación.")
                    st.markdown("Para ello, selecciona los datos que quieres mostrar en la visualización resumida y pulsa 'Guardar'.")
                    with st.container():
                        table_name = st.selectbox("Selecciona una tabla:", list(data.get_table_data().keys()))
                        with st.spinner('Cargando datos...'):
                            table_data = data.get_table_data()[table_name]
                            st.write("Columnas:", table_data['columns'])
                            st.write("Datos:")
                            for row in table_data['data']:
                                st.write(row)
                            st.success('Datos cargados exitosamente!')