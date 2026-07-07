import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Dashboard Morosidad Bancaria", layout="wide")

st.title("📊 Dashboard Analítico - Riesgo de Morosidad Bancaria")

# Cargar datos
df = pd.read_csv("dataset_personal.csv")

# KPI
porcentaje_morosos = df["Moroso"].mean() * 100

st.metric(
    label="Porcentaje de Clientes Morosos",
    value=f"{porcentaje_morosos:.2f}%"
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Clientes Morosos")

    fig, ax = plt.subplots()

    conteo = df["Moroso"].value_counts()

    ax.bar(["No Moroso", "Moroso"], conteo)

    st.pyplot(fig)

with col2:
    st.subheader("Distribución del Ingreso Mensual")

    fig, ax = plt.subplots()

    ax.hist(df["Ingreso_Mensual"], bins=30)

    st.pyplot(fig)

st.subheader("Ingreso Mensual vs Deuda Total")

fig, ax = plt.subplots()

ax.scatter(
    df["Ingreso_Mensual"],
    df["Deuda_Total"],
    alpha=0.5
)

ax.set_xlabel("Ingreso Mensual")
ax.set_ylabel("Deuda Total")

st.pyplot(fig)

st.subheader("Hallazgos")

st.write("""
- El porcentaje de clientes morosos permite identificar el nivel de riesgo de la cartera.
- Existe una relación entre el ingreso mensual y la deuda total.
- El Árbol de Decisión obtuvo el mejor desempeño predictivo.
""")

st.subheader("Recomendaciones")

st.write("""
- Evaluar el riesgo antes de aprobar nuevos créditos.
- Dar seguimiento a clientes con alta relación deuda/ingreso.
- Actualizar periódicamente el modelo con nuevos datos.
""")
