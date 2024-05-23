import pandas as pd


def calculate_potential_students(birth_data_path, output_file_path):
    # Read sheet
    birth_data = pd.read_excel(birth_data_path)

    # Only want years between 2001 and 2022 for my analysis
    years_of_study = range(2001, 2023)

    potential_students = []
    for year in years_of_study:
        # to get the relevant years of birth - use range of 18, 19 and 20 years old
        relevant_birth_years = range(year - 20, year - 17)
        relevant_births = birth_data[birth_data['Rok'].isin(relevant_birth_years)]

        # Calculate the average number and round it
        avg_births = round(relevant_births['Počet narozených'].mean() if not relevant_births.empty else None)
        potential_students.append({'Rok': year, 'Potenciální studenti': avg_births})

    # Create data frame
    potential_students_df = pd.DataFrame(potential_students)

    # Save data
    potential_students_df.to_excel(output_file_path, index=False)
    print(f"Data about potential students from 2001 to 2022 have been successfully saved to {output_file_path}")


# Paths to the files
birth_data_path = 'narozeni.xlsx'
output_file_path = 'mozni_studenti.xlsx'

# Process the data
calculate_potential_students(birth_data_path, output_file_path)
