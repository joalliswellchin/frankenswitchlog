import pandas as pd
import os

def get_csv():
    filename = os.getenv('CSV_FILENAME', 'switch_data')
    filedir = './' + filename + '.csv'
    print('file dir:',filedir)
    return pd.read_csv(filedir)

def generate_md(df, dir):
    f = open(dir + "/README.md", "w")
    # TODO: set title in file
    df = df.fillna('')
    title = list(df.columns)
    temp = [" ---- " for _ in title if True]
    f.write('|' + '|'.join(title) + '|\n')
    f.write('|' + '|'.join(temp) + '|\n')
    for _, row in df.iterrows():
        f.write('|' + row.str.cat(sep='|')+ '|\n')
    f.close()
    return

def main():
    # TODO: get excel maybe?
    print('Getting csv...')
    df = get_csv()

    # split df to multiple readme, and save them in respective folders
    # TODO: spawning of multiprocessing for the below info
    # get all top housing info
    tophousing_df = df[['name of switch', 'producer', 'top housing']].copy()
    generate_md(tophousing_df, 'switches/tophousing')
    # get all btm housing info
    btmhousing_df = df[['name of switch', 'producer', 'bottom housing']].copy()
    generate_md(btmhousing_df, 'switches/btmhousing')
    # get all stem info
    stem_df = df[['name of switch', 'producer', 'stem']].copy()
    generate_md(stem_df, 'switches/stem')
    # get all spring info
    spring_df = df[['name of switch', 'producer', 'spring']].copy()
    generate_md(spring_df, 'switches/spring')

# in case we need to import from elsewhere
if __name__ == '__main__':
    main()