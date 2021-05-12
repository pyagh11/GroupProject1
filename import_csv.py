import mandatory_libraries as ml

csv_path = ml.Path('Resources/avg_wages.csv')
avg_wages_file = ml.pd.read_csv(csv_path, header=0, parse_dates=True).dropna(how='all', axis=1)

csv_path = ml.Path('Resources/countries_codes_and_coordinates.csv')
countries_abbr_file = ml.pd.read_csv(csv_path, header=0).dropna(how='all', axis=1)

csv_path = ml.Path('Resources/cost of living index cos.csv')
cost_of_living_file = ml.pd.read_csv(csv_path, header=0, parse_dates=True).dropna(how='all', axis=1)