import pandas
df = pandas.read_csv("input/main.csv")
df1 = df[df['COUNTRY'].str.contains("USA")]
#print(df1)
df1 = pandas.DataFrame(df1)
print(df1)
df1.to_csv('output/filteredCountry.csv')
