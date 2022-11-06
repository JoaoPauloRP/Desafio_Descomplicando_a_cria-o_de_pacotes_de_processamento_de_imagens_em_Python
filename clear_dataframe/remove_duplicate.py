def remove_duplicate(dataframe):
  duplicados = dataframe[dataframe.duplicated(keep='first')]
  if len(duplicados) > 0:
      print(duplicados)
      dataframe = dataframe.drop_duplicates(keep='first', inplace=True)
      print(" \n \n Valores duplicados foram removidos")
  else:
          print("Não há valores duplicados")