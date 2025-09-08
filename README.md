# proyecto_sprint7
# proyecto_sprint7: es una visualizacion de datos de Vehiculos.
Este proyecto es una aplicación web interactiva creada con **Streamlit** que permite explorar el conjunto de datos `vehicles_us.csv`.  
La aplicación ofrece dos visualizaciones principales que ayudan a comprender mejor los anuncios de venta de vehículos:
**Histograma**: muestra la distribución de los valores del odómetro (kilometraje de los vehículos).  
**Diagrama de dispersión**: permite observar la relación entre el precio y el kilometraje de los vehículos.
## Funcionalidad
La aplicación utiliza casillas de verificación (`st.checkbox`) para que el usuario seleccione las gráficas que desea visualizar.  
Las funcionalidades principales son:

- Seleccionar y mostrar un **histograma** del kilometraje.  
- Seleccionar y mostrar un **diagrama de dispersión** (precio vs. odómetro).  
- Posibilidad de visualizar ambos gráficos al mismo tiempo o ninguno (en cuyo caso se muestra un mensaje informativo).  

## Tecnologías utilizadas
- Python 3  
- [Streamlit](https://streamlit.io/)  
- [Plotly Express](https://plotly.com/python/plotly-express/)  
- Pandas  