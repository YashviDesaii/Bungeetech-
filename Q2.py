import pandas
df = pandas.read_csv("output/filteredCountry.csv")
df = df.drop(['DESCRIPTION', 'YEAR','CAPACITY','URL','SELLER_INFORMATION','OFFER_DESCRIPTION','COUNTRY'], axis=1)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
print(df.columns)
df['PRICE'] = df['PRICE'].map(lambda x: x.lstrip('$').rstrip('?'))
df['PRICE'] = df['PRICE'].str.replace(',','')
df['PRICE'] = df['PRICE'].astype(float)
SKU = df.groupby(['SKU'])
df1 = df.groupby('SKU').PRICE.nsmallest(1).reset_index().drop('level_1',1)
df2 = df.groupby('SKU').PRICE.nsmallest(2).reset_index().drop('level_1',1) \
.drop_duplicates(subset=['SKU'], keep='last')
df2 = df2.reset_index()

#print(df1)
#print(df2)
sku = df1['SKU'].tolist()
price1 = df1['PRICE'].tolist()
price2 = df2['PRICE'].tolist()

finaldf = pandas.DataFrame({'SKU':sku,'FIRST_MINIMUM_PRICE':price1, 'SECOND_MINIMUM_PRICE':price2})
print(finaldf)
finaldf.to_csv('output/lowestPrice.csv')