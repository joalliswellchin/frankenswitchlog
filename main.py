import pandas as pd
import os

def get_csv():
    filename = os.getenv('CSV_FILENAME', 'switch_data')
    filedir = './' + filename + '.csv'
    print('file dir:',filedir)
    return pd.read_csv(filedir)

def main():
    print("Getting csv...")
    df = get_csv()
    print(df)

# in case we need to import from elsewhere
if __name__ == "__main__":
    main()