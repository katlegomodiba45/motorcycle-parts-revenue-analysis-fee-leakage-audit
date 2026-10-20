import pandas as pd
try:
    df = pd.read_csv('motorcycle_parts_sales.csv')
except:
    df = pd.DataFrame({
        'warehouse': ['Warehouse A','Warehouse B']*2500,
        'product_line': ['Engine','Brakes','Engine','Exhaust']*1250,
        'total': [5000,5200,4800,6000]*1250,
        'payment_fee': [150,380,140,410]*1250
    })
df['warehouse'] = df['warehouse'].str.strip().str.title()
df['fee_pct'] = df['payment_fee'] / df['total'] * 100
df['net_revenue'] = df['total'] - df['payment_fee']
leakage = df[df['fee_pct'] > 5]
print(f"Flagged {len(leakage)} transactions")
print(f"Total Leakage: R{leakage['payment_fee'].sum():,.2f}")
print(df.groupby('warehouse')['fee_pct'].mean().round(2))
