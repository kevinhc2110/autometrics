from typing import Dict

import pandas as pd


def calculate_metrics(df: pd.DataFrame) -> Dict[str, float]:
    """
    Calcula métricas de ventas a partir de un DataFrame de pandas.

    Args:
        df (pd.DataFrame): DataFrame que contiene al menos la columna 'sales'.

    Returns:
        dict[str, float]: Diccionario con las métricas calculadas:
            - 'total_sales': Suma total de ventas.
            - 'average_sales': Promedio de ventas.

    Raises:
        ValueError: Si el DataFrame no contiene la columna 'sales'.
    """
    if 'sales' not in df.columns:
        raise ValueError("El DataFrame no contiene la columna 'sales'")

    total_sales = df['sales'].sum(skipna=True)
    average_sales = df['sales'].mean(skipna=True)

    return {
        'total_sales': total_sales,
        'average_sales': average_sales
    }
