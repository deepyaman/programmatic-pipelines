"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.6
"""
import pandas as pd


def process(data_right: pd.DataFrame) -> pd.DataFrame:
    combine_all = pd.DataFrame()

    for partition_id, partition_load_func in data_right.items():
        partition_data = partition_load_func()
        combine_all = pd.concat(
            [combine_all, partition_data], ignore_index=True, sort=True
        )

    return combine_all
