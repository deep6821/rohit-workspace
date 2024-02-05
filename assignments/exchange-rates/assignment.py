import pandas as pd

# Read the CSV files
customers_df = pd.read_csv('customer.csv')
exchange_rate_df = pd.read_csv('exchange_rate.csv')
transactions_df = pd.read_csv('transaction.csv')

# Convert transaction_date column to datetime type
transactions_df['transaction_date'] = pd.to_datetime(transactions_df['transaction_date'], dayfirst=True)

# Merge customers_df and transactions_df on customer_id
merged_df = pd.merge(customers_df, transactions_df, on='customer_id')

# Merge merged_df and exchange_rate_df on currency
merged_df = pd.merge(merged_df, exchange_rate_df, left_on='currency', right_on='from_currency')

# Calculate the total amount in EUR
merged_df['amount_eur'] = merged_df['amount'] * merged_df['rate']

# Create a new column for month and year
merged_df['month_year'] = merged_df['transaction_date'].dt.to_period('M')

# Group by month, country, and calculate total amount, number of transactions, and number of unique users
summary_df = merged_df.groupby(['month_year', 'country']).agg({'amount_eur': 'sum', 'transaction_id': 'count', 'customer_id': 'nunique'})
summary_df = summary_df.rename(columns={'amount_eur': 'total_amount_eur', 'transaction_id': 'num_transactions', 'customer_id': 'num_unique_users'})

print("Summary View:")
print(summary_df)

# Calculate the evolution of exchange rates for each currency (based on GBP) in percentage for the next 15 days
date_to_check = pd.to_datetime('02-01-2020', dayfirst=True)

currency_list = merged_df['to_currency'].unique()
rate_evolution_df = pd.DataFrame(columns=['currency', 'date', 'rate_evolution'])

for currency in currency_list:
    currency_df = exchange_rate_df.loc[(exchange_rate_df['from_currency'] == 'GBP') & (exchange_rate_df['to_currency'] == currency)]
    start_rate = currency_df.loc[currency_df['effective_date'] == date_to_check, 'rate'].values[0]
    next_15_days = pd.date_range(start=date_to_check, periods=15, freq='D')
    rates = currency_df.loc[currency_df['effective_date'].isin(next_15_days), 'rate']
    evolution = (rates / start_rate - 1) * 100
    currency_evolution_df = pd.DataFrame({'currency': [currency]*len(evolution), 'date': next_15_days, 'rate_evolution': evolution})
    rate_evolution_df = pd.concat([rate_evolution_df, currency_evolution_df])

print("\nExchange Rate Evolution:")
print(rate_evolution_df)




print