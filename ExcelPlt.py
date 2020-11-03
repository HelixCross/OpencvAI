import pandas as pd
import plotly.express as px

# Creation of the variables to read the EXCEL files.
# Note that you will have to install the xlrd module in order to read the xlsx files.
# You may use the csv format as well in order to avoid the xlrd installation.
excel_book_1_letative_path = '/Users/Hetze/Downloads/Purchases - Home A.xlsx'
excel_book_prices = '/Users/Hetze/Downloads/PriceBook.xlsx'

# Creation variables for the file read.
df_prices = pd.read_excel(excel_book_prices)
df_home_1 = pd.read_excel(excel_book_1_letative_path)


# print(df_prices, df_home_1)

# Merging two columns into the ID one.
df_total = df_home_1.merge(df_prices, on="ID")

# Calling the row total price and the purchased amounts from the csv file.
# You may call the same way any row you wish to automate.
df_total["Total Price"] = df_total["PURCHASED AMOUNT"] * df_total["Price"]

# Print the called rows.
print(df_total)

# Create and show the graph.
# Matpyplot may be used here as well.
fig = px.pie(df_total[["MATERIAL", "Total Price"]], values="Total Price", names="MATERIAL")
fig.show()
