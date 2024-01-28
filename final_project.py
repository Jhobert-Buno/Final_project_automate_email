from datetime import date
import pandas as pd 
from final_project_try import send_email

#use the google sheets url
SHEET_ID = "1Aw-sAHaWse4pELT8KA5mvsL1HGElHnSJj9p8Xv0cnog"
SHEET_NAME = "Sheet1"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"
