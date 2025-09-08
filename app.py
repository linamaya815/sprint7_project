import pandas as pd
import plotly.express as px
import streamlit as st

# leer los datos
car_data = pd.read_csv('vehicles_us.csv')

st.title("Exploración de vehicles_us")

# casillas de verificación
show_hist = st.checkbox('Mostrar histograma')
show_scatter = st.checkbox('Mostrar diagrama de dispersión')

# histograma
if show_hist:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# diagrama de dispersión
if show_scatter:
    st.write('Creación de un gráfico de dispersión: precio vs. odómetro')
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Relación entre kilometraje y precio",
        labels={"odometer": "Kilometraje", "price": "Precio"}
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# mensaje si no se selecciona nada
if not show_hist and not show_scatter:
    st.write("Selecciona al menos una casilla para visualizar un gráfico.")
