import streamlit as st
import time
from ..controllers import dataController as dc
dataC = dc.dataController

mainContent = st.container
def main():
    mainContent.title("Data Visualization")
    mainContent.markdown("""
    ## Data Visualization
    """)
    Historic_Data = dataC.getAtributtesFromTable
    with mainContent:
        st.markdown("""
                    
                    
                    Aquí Probando la visualización de streamlit según lo que encuentre en la base de datos.
                    """)
        with st.spinner('Cargando...'):
            st.altair_chart(Historic_Data)


if __name__ == '__main__':
    main()