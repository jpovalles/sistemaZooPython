import views.viewsZoo as tiendaView
import streamlit as st


if __name__ == '__main__':
    st.set_page_config(
        page_title="CRUD de una tienda",
        layout="wide"
    )
    tienda = tiendaView.sistema()
    tienda.mostrarMenu()