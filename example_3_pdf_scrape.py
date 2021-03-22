import pdfplumber
import pandas as pd


# Load the PDF file
path = r'pdf\salary-information-for-the-executive-branch.pdf'

# Identify the agency salary table
with pdfplumber.open(path) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                if 'AGENCY' in row:
                    agency_table = table

cleaned_table = []



# Save the table data to csv
headers = cleaned_table.pop(0)

df = pd.DataFrame(cleaned_table, columns=headers)

df.to_csv(r'pdf\salary_info.csv', index=False)
