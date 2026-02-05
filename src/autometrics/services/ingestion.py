from pathlib import Path

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


def load_google_sheets(sheet_id: str) -> pd.DataFrame:
    """
    Carga los datos de un documento de Google Sheets en un DataFrame de pandas.

    Args:
        sheet_id (str): El ID del documento de Google Sheets.

    Returns:
        pd.DataFrame: Contiene los datos del documento de Google Sheets.

    Raises:
        ValueError: Si el sheet_id no existe.
        RuntimeError: Si ocurre un error al conectarse a Google Sheets.
    """
    scope: list[str] = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds_file = Path("credentials.json")
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
    client = gspread.authorize(creds)

    try:
        sheet = client.open_by_key(sheet_id).sheet1
        data = sheet.get_all_records()
    except gspread.SpreadsheetNotFound:
        raise ValueError(f"Google Sheet con ID {sheet_id} no encontrado")
    except Exception as e:
        raise RuntimeError(f"No se pudo cargar la hoja de Google Sheets: {e}")

    df = pd.DataFrame(data)
    return df
