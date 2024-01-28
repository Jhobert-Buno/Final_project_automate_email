from datetime import date
import pandas as pd 
from final_project_try import send_email

#use the google sheets url
SHEET_ID = "1Aw-sAHaWse4pELT8KA5mvsL1HGElHnSJj9p8Xv0cnog"
SHEET_NAME = "Sheet1"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

def load_df(url):
    parse_dates = ["due_date", "reminder_date"]
    df = pd.read_csv(url, parse_dates=parse_dates)
    return df


print(load_df(URL))