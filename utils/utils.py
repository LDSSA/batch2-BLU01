import pandas as pd

def get_stores_data():
    return pd.read_csv('data/stores.csv', \
                         usecols=['Date', 'Store', 'Sales', 
                                  'Customers', 'Open', 'Promo'])

def get_store_data():
    stores = get_stores_data()
    store = stores.loc[stores.Store==1].drop('Store', axis=1)    
    store.Date = pd.to_datetime(store.Date).dt.strftime('%d/%m/%Y')
    store = store.sample(frac=1, random_state=9999)
    return store
