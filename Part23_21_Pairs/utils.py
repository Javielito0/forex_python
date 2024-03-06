def get_his_data_filename(pair, granularity):
    return f"/Users/javier/Documents/visual_studio/forex_python/Part23_21_Pairs/his_data/{pair}_{granularity}.pkl"

def get_instruments_data_filename():
    return "instruments.pkl"

if __name__ == "__main__":
    print(get_his_data_filename("EUR_USD", "H1"))
    print(get_instruments_data_filename())