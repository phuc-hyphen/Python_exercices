import pandas as pd
import xlsxwriter

# Create a Pandas Excel writer using XlsxWriter as the engine.
# writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
# df5 = pd.read_excel('sample.xlsx')
df = pd.read_csv('datas.csv')
print(df)


# df_sheet_index = pd.read_excel('sample.xlsx', sheet_name=1)

# # Convert the dataframe to an XlsxWriter Excel object.
# df.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False, index=False)

# # Convert the dataframe to an XlsxWriter Excel object.
# df.to_excel(writer, sheet_name='Sheet1')  # Default position, cell A1.
# df.to_excel(writer, sheet_name='Sheet1',
#              startrow=7, startcol=4, header=False, index=False)
# df.to_excel(writer, sheet_name='Sheet1', startcol=3)
# df.to_excel(writer, sheet_name='Sheet1', startrow=6)

# # get information about the sheet
# df.index #returns the list of the index, in our case, it’s just integers 0, 1, 2, 3.

# df.columns # gives the list of the column (header) names.

# df.shape # shows the dimension of the dataframe, in this case it’s 4 rows by 5 columns.
# # get a column
# df5.country # get column country
# print(df5["column name"])
# df[['User Name', 'Age', 'Gender']]
# #get a row
# df5.loc[0]
# df5.loc[begin:end]
# # create new column
# df5["new column name"] = df5["column name"].replace(" ", "_")
# # get max values of column
# df5["new column name"].max()
# #view the data
# val = df5['City'][1]
# val = df5['col_name'].values[0]
# df.loc[2,'Country'] # get the country name for Harry Porter, who’s on row 3.
# print(df5.tail(20))#last 20 rows
# print(df5.head(20))#firts 20 rows

# # get mini table of values
# df[['User Name', 'Age', 'Gender']].loc[[1,3]]
# df.loc[[1,3],['User Name', 'Age', 'Gender']]

# #mapping
# df = pd.DataFrame({'col2': {0: 'a', 1: 2, 2: np.nan}, 'col1': {0: 'w', 1: 1, 2: 2}})
# di = {1: "A", 2: "B"}
# df.replace({"col1": di}) #replace
# df['col1'].map(di)       # note: if the dictionary does not exhaustively map all
#                          # entries then non-matched entries are changed to NaNs
# df['col1'].map(di).fillna(df['col1']) # Non-Exhaustive mapping


# # Get the xlsxwriter objects from the dataframe writer object.
# workbook = writer.book
# worksheet = writer.sheets['Sheet1']

# # using XlsxWriter
# workbook = xlsxwriter.Workbook('filename.xlsx')
# worksheet = workbook.add_worksheet()

# # Close the Pandas Excel writer and output the Excel file.
# writer.save()

# # ADD chart
# # Create a chart object.
# chart = workbook.add_chart({'type': 'column'})

# # Get the dimensions of the dataframe.
# (max_row, max_col) = df.shape

# # Configure the series of the chart from the dataframe data.
# chart.add_series({'values': ['Sheet1', 1, 1, max_row, 1]})

# # Insert the chart into the worksheet.
# worksheet.insert_chart(1, 3, chart)

# # Apply a conditional format to the required cell range.
# worksheet.conditional_format(1, max_col, max_row, max_col,
#                              {'type': '3_color_scale'})
# # sett datetime format
# writer = pd.ExcelWriter("pandas_datetime.xlsx",
#                         engine='xlsxwriter',
#                         datetime_format='mmm d yyyy hh:mm:ss',
#                         date_format='mmmm dd yyyy')

# # Add some cell formats.
# format1 = workbook.add_format({'num_format': '#,##0.00'})
# format2 = workbook.add_format({'num_format': '0%'})

# # Set the column width and format.
# worksheet.set_column(1, 1, 18, format1)

# # Set the format but not the column width.
# worksheet.set_column(2, 2, None, format2)

# # Add a header format.
# header_format = workbook.add_format({
#     'bold': True,
#     'text_wrap': True,
#     'valign': 'top',
#     'fg_color': '#D7E4BC',
#     'border': 1})

# # Write the column headers with the defined format.
# for col_num, value in enumerate(df.columns.values):
#     worksheet.write(0, col_num + 1, value, header_format)
