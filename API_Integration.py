import mandatory_libraries as ml
import import_csv as csv_files

ml.load_dotenv('.env')
def get_CryptoCompare_content():
    crypto_currency_list = 'fsyms=BTC,ETH,DOGE,LTC,BCH,XRP,ADA,XLM,LINK,ALGO,WBTC,YFI,COMP,DASH,ETC,SOL,UNI,DOT,CAKE,WAVES,ATOM,BCD,QTUM,CEL,MANA,STX,FTM,LUNA,AAVE,GRT,SUSHI,BNB,USDT,VET,THETA,FIL,TRX,EOS,XMR,NEO,BSV,MIOTA,XTZ,BTT,MKR,HT,DAI'
    # local_currency_list = 'tsyms=EUR,USD,GBP,JPY,AUD,CAD,CHF,NZD,CNY,SEK,MXN,SGD,HKD,NOK,KRW,TRY,INR,RUB,BRL'
    local_currency_list = 'tsyms=USD'
    crypto_compare_apy_key = ml.os.getenv("CRYPTO_COMPARE_API_KEY")

    crypto_compare_URL = 'https://min-api.cryptocompare.com/data/pricemulti?'+crypto_currency_list+'&'+local_currency_list
    response_data = ml.requests.get(crypto_compare_URL)
    crypto_compare_content = ml.json.loads(ml.json.dumps(response_data.json(), indent=4))
    return crypto_compare_content

def cryptoCompareContend_toDataFrame():
    records=[]
    crypto_compare_content = get_CryptoCompare_content()
    for crypto_currency in crypto_compare_content.keys():
        for currency_code in crypto_compare_content[crypto_currency].keys():
            records.append([
                crypto_currency,
                currency_code,
                crypto_compare_content[crypto_currency][currency_code]
            ])
    result_df = ml.pd.DataFrame(records, columns=['crypto_currency','currency_code','crypto_value'])
    result_df.to_csv('crypto_compare_df.csv', index=False)
    return result_df

def set_final_df():
    crypto_df = cryptoCompareContend_toDataFrame()
    avg_wages = csv_files.avg_wages_file
    country_abbr = csv_files.countries_abbr_file
    final_df = ml.pd.merge(crypto_df,avg_wages,on='currency_code',how='left')
    final_df['avg_wage_crypto_value'] = final_df['avg_wage_value']/final_df['crypto_value']
    final_df = ml.pd.merge(final_df,country_abbr, on='country_code',how='left')
    final_df = final_df[final_df['year'] > 2015]

    final_df['full_date'] = ml.pd.to_datetime(final_df['year'], format='%Y')
    final_df.to_csv('final_df.csv', index=False)
    return final_df
