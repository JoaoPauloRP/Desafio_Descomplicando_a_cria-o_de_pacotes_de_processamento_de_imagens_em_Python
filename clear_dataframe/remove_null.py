def remove_null(dataframe):
  dataframe.dropna(how="all", inplace=True)