import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Gsheets:
    def __init__(self, secret_path):
        self.client = self._connect(secret_path)

    def _connect(self, secret_path):
        scope = ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(secret_path, scope)
        client = gspread.authorize(creds)
        return client

    def uploadtosheet(self, sheet_name, form_data):
        sheet = self.client.open(sheet_name).sheet1
        sheet.insert_row(form_data)
        
