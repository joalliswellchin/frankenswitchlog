import pandas as pd
import os

def get_csv():
    filename = os.getenv('CSV_FILENAME', 'switch_data')
    filedir = './' + filename + '.csv'
    print('file dir:',filedir)
    return pd.read_csv(filedir)

def main():
    #TODO: get excel maybe?
    print("Getting csv...")
    df = get_csv()
    print(df)
    #TODO: Convert csv to multiple readme, and save them in respective folders

# in case we need to import from elsewhere
if __name__ == "__main__":
    main()