# Assignment_Task3
# PDF Data Extraction from URL

This project extracts data from PDF reports available on a specific webpage. The main goal is to download and extract relevant data from PDFs that contain the keywords "DSM", "SRAS", "TRAS", "SCUC" in their titles and then filter the extracted data based on specific criteria (e.g., the presence of the keyword "MPL"). The extracted data is saved in CSV format for further analysis.

## Requirements

- Python 3.x
- Selenium WebDriver
- Chrome WebDriver
- Libraries:
  - `requests`
  - `pdfplumber`
  - `re`
  - `csv`
  - `selenium`
  - `datetime`

To install the required Python libraries, you can use `pip`:
``` bash
pip install requests pdfplumber selenium

```


Overview
Web Scraping: The script uses Selenium to open a webpage (https://erpc.gov.in/ui-and-deviation-accts/) and locates all PDF links on the page.
PDF Processing: After identifying the PDF URLs, the script downloads each PDF and extracts tables from them using pdfplumber.
Data Extraction: It looks for specific keywords in the titles of the PDFs and only processes those that contain "DSM", "SRAS", "TRAS", "SCUC" and a date range.
Data Filtering: From the extracted tables, it filters rows that contain the keyword "MPL" and stores them in a list.
Save Data: Finally, the script saves the filtered data into a CSV file for each relevant PDF report.
Features
Extracts data from multiple PDF reports.
Filters rows based on the presence of the keyword "MPL".
Saves the filtered data into CSV files named according to the report titles.
Handles PDF documents with varying date formats and title structures.

Code Breakdown
extract_pdf_data.py
Web Scraping with Selenium: The script uses Selenium to open the webpage and extract links to PDFs.
PDF Downloading: The requests library is used to download the PDF files from the extracted links.
PDF Table Extraction: Using pdfplumber, the script extracts tables from each page of the PDFs.
Data Filtering: Rows that contain "MPL" are identified and stored in a list.
CSV Writing: The filtered data is written to CSV files using Python's built-in csv module.

Key Functions:
extract_pdf_data(pdf_url, report_name): Downloads the PDF and processes its data.
extract_data_from_pdf(pdf, report_name): Extracts the tables from each page of the PDF and filters them for the keyword "MPL".
save_data_to_csv(): Saves the extracted data to CSV files.

Dependencies:
Selenium: Used for web scraping.
Requests: Used for downloading PDF files.
Pdfplumber: Used to extract tables from PDFs.

Example Output
After running the script, the following CSV files will be saved in the same directory as the script:

DSM_SRAS_TRAS_and_SCUC_Accounts_04_11_2024_to_10_11_2024_mpl.csv
DSM_SRAS_TRAS_and_SCUC_Accounts_28_10_2024_to_03_11_2024_mpl.csv
DSM_SRAS_TRAS_and_SCUC_Accounts_14_10_2024_to_20_10_2024_mpl.csv
Each CSV file will contain the filtered rows from the corresponding PDF report.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Selenium WebDriver - For automating web browser interactions.
pdfplumber - For extracting tables from PDFs.
Requests - For downloading files from URLs.



#Python #try #except #error_handling #row_remove #data #unnamed_error #pandas
