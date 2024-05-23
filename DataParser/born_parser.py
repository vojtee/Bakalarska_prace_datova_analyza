import pandas as pd


def extract_data(file_path, output_file_path):
    # Skip the first lines
    data = pd.read_excel(file_path, skiprows=8)

    # Need column A and D (0, 4)
    column_a = data.iloc[:, 0]
    born = pd.to_numeric(data.iloc[:, 4], errors='coerce')  # Converts to numeric and replaces errors with NaN

    # New DataFrame
    result_df = pd.DataFrame({
        'Rok': column_a,
        'Počet narozených': born
    })

    # Save the data
    result_df.to_excel(output_file_path, index=False)
    print(f"Data were successfully saved to {output_file_path}")


# Paths to the files
file_path = 'pohyb_obyvatel.xlsx'
output_file_path = 'narozeni.xlsx'

# Process data
extract_data(file_path, output_file_path)
