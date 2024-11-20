import pandas as pd
from pathlib import Path

def read_excel_sheet(excel_file_path, sheet_name, header=1):
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name, header=header)
    print(df.to_json())
    

if __name__ == "__main__":
    read_excel_sheet(excel_file_path=(Path(__file__).parents[2]/"assets/data_links.xlsx"), sheet_name="sheet_data_link")
    # print(Path(__file__).parents[1], type(Path(__file__)))
    
    