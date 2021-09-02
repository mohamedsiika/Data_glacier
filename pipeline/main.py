import yaml
import logging
import pandas as pd
def config_file(filepath):
    with open(filepath, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logging.error(exc)

def validation(table_config,df):
    expected_col=list(map(lambda x:x.lower(),list(table_config['columns'])))
    expected_col.sort()
    df.columns=list(map(lambda x:x.lower(),list(df.columns)))
    df = df.reindex(sorted(df.columns), axis=1)
    print(expected_col)
    print(df.columns)
    if len(df.columns) == len(expected_col) and list(expected_col) == list(df.columns):
        print("column name and column length validation passed")
        return 1
    else:

        print("column name and column length validation failed")
        mismatched_columns_file = list(set(df.columns).difference(expected_col))
        print("Following File columns are not in the YAML file", mismatched_columns_file)
        missing_YAML_file = list(set(expected_col).difference(df.columns))
        print("Following YAML columns are not in the file uploaded", missing_YAML_file)
        logging.info(f'df columns: {df.columns}')
        logging.info(f'expected columns: {expected_col}')
        return 0

table_config=config_file('file.Yaml')
df=pd.read_csv('yellow_tripdata.csv')
validation(table_config,df)
