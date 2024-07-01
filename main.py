import pandas as pd
import glob
from loguru import logger

def read_file(model):

    logger.info('Reading files.')

    file_pattern = f'Files/{model}*.csv'

    files = sorted(glob.glob(file_pattern))

    if not files:
        logger.error(f"No files found for pattern {file_pattern}")
    else:
        records_list = [pd.read_csv(file, delimiter='|') for file in files]
        combined_records = pd.concat(records_list, ignore_index=True)
        save_csv(combined_records, model)

def save_csv(combined_records, model):

    logger.info('Generating CSV files.')

    output = f'Output/{model}.csv'

    combined_records.to_csv(output, index=False, sep = '|')

def main():

    model = input('Enter model to generate: ')
 
    read_file(model)

if __name__ == '__main__':
    main()  