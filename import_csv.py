import mandatory_libraries as ml

csv_path = ml.Path('Resources/avg_wages.csv')
avg_wages_file = ml.pd.read_csv(csv_path, header=0, parse_dates=True).dropna(how='all', axis=1)