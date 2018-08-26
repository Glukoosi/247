import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from app import app

class Gsheets:
    def __init__(self, secret_path):
        client = self._connect(secret_path)

    def _connect(self, secret_path):
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name(secret_path, scope)
        client = gspread.authorize(creds)
        return client

    def uploadtosheet(self, sheet_name):
        print("updloading ayyy")
        return None
        
