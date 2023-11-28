import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    combined_table = pd.merge(person, address, on='personId', how='left')
    return combined_table[['firstName', 'lastName', 'city', 'state']]
