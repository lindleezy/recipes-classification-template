import logging
import os
import pandas as pd


_logger = logging.getLogger(__name__)


def load_file_as_dataframe(location: str, *args, **kwargs) -> pd.DataFrame:
    """
    Load content from the specified dataset file as a Pandas DataFrame.

    This method is used to load dataset types that are not natively  managed by MLflow Recipes
    (datasets that are not in Parquet, Delta Table, or Spark SQL Table format). This method is
    called once for each file in the dataset, and MLflow Recipes automatically combines the
    resulting DataFrames together.

    :param location: The path to the dataset file.
    :return: A Pandas DataFrame representing the content of the specified file.
    """
    _, file_extension = os.path.splitext(location)
    if file_extension == '.csv':
        return pd.read_csv(location, *args, **kwargs)
    elif file_extension in ['.xls', '.xlsx', '.xlsm', '.xlsb', '.odf', '.ods', '.odt']:
        return pd.read_excel(location, *args, **kwargs)
    else:
        raise NotImplementedError(f'Unsupported file format: {file_extension}')