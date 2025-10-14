import pandas as pd

class AnimeDataLoader:
    def __init__(self, original_csv:str, processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_process(self):
        data = pd.read_csv(self.original_csv , encoding='utf-8' , on_bad_lines='skip').dropna()
        required_cols = {'Name', 'Genres', 'Sypnopsis'}
        missing_cols = required_cols - set(data.columns)

        if missing_cols:
            raise ValueError("Missing Column in CSV File")
        
        data['Info'] = (
            "Title: " + data["Name"] + " Overview: " + data["Sypnopsis"] + " Genres: " + data["Genres"]
        )

        data[['Info']].to_csv(self.processed_csv , index=False, encoding='utf-8')

        return self.processed_csv