import pandas as pd


def process_data(excel_file_path, start_row, output_file_name):
    # Table setup
    columns = ['Celkem', 'Celkem P', 'Bakalářské P', 'Magisterské P', 'Navazující magisterské P', 'Doktorské P',
               'Celkem K', 'Bakalářské K', 'Magisterské K', 'Navazující magisterské K', 'Doktorské K']

    # Read data from each list for each row
    dfs = pd.read_excel(excel_file_path, sheet_name=None, header=None, skiprows=start_row-1, usecols='G:Q')

    # For each list get only the needed line and add the year
    for sheet_name, df in dfs.items():
        df = df.iloc[0, :].to_frame().T
        df.columns = columns
        df['Rok'] = sheet_name
        dfs[sheet_name] = df

    # Concatenate all lists into one DataFrame
    final_df = pd.concat(dfs.values(), ignore_index=True)

    # Save the DataFrame to an Excel file
    output_file = f'{output_file_name}.xlsx'
    final_df.to_excel(output_file, sheet_name=output_file_name, index=False)


# Define the rows and output file names
rows_and_outputs = [(10, 'poprve_zapsani'), (12, 'celkem_studenti'), (19, 'celkem_studenti_cr'),
                    (26, 'celkem_studenti_ciz'), (33, 'celkem_studenti_verejne'), (40, 'celkem_studenti_soukrome')]

# Process the data
for start_row, output_name in rows_and_outputs:
    process_data('f11.xlsx', start_row, output_name)
    print(f"Data saved successfully for {output_name}.")
