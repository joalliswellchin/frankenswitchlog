import pandas as pd
import os

def get_csv():
    filename = os.getenv('CSV_FILENAME', 'switch_data')
    filedir = './' + filename + '.csv'
    print('file dir:',filedir)
    return pd.read_csv(filedir)

def generate_md():
    #TODO: Convert csv to multiple readme, and save them in respective folders
    return

def main():
    #TODO: get excel maybe?
    print("Getting csv...")
    df = get_csv()
    print(df)
    generate_md()

# in case we need to import from elsewhere
if __name__ == "__main__":
    main()