import streamlit as st

from autometrics.services.ingestion import load_google_sheets
from autometrics.services.metrics import calculate_metrics

st.title("AutoMetrics Dashboard")

# Input: Sheet ID
sheet_id = st.text_input("Ingrese el Google Sheet ID", value="TU_DEFAULT_ID")

if sheet_id:
    # Paso 1: Ingestión de datos
    try:
        data = load_google_sheets(sheet_id)
        st.write("Datos brutos:", data.head())
    except Exception as e:
        st.error(f"No se pudo cargar los datos: {e}")
        st.stop()

    # Paso 2: Cálculo de métricas
    try:
        metrics = calculate_metrics(data)
        st.subheader("Métricas calculadas")
        for key, value in metrics.items():
            st.metric(label=key, value=value)
    except Exception as e:
        st.error(f"No se pudieron calcular las métricas: {e}")
        st.stop()

    # Paso 3: Visualización
    if "sales" in data.columns:
        st.subheader("Gráfico de ventas")
        st.bar_chart(data["sales"])
    else:
        st.warning("No hay columna 'sales' para graficar")
