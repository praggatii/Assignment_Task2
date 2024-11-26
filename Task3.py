import re
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from io import BytesIO
import pdfplumber
import csv
 
# Store pdf data in list
pdf_data_list = []
 
required_keywords = ["DSM", "SRAS", "TRAS", "SCUC"]
 
# Download and extract data from pdf
def extract_pdf_data(pdf_url, report_name):
    print(f"Downloading PDF from: {pdf_url}")
    pdf_response = requests.get(pdf_url)
    pdf_response.raise_for_status()
 
    with pdfplumber.open(BytesIO(pdf_response.content)) as pdf:
        extract_data_from_pdf(pdf, report_name)
 
# Extract data from PDF and filter 'MPL'
def extract_data_from_pdf(pdf, report_name):
    extracted_data = []
 
    total_pages = len(pdf.pages)
    print(f"Total pages in PDF: {total_pages}")
 
    for page_num, page in enumerate(pdf.pages):
        print(f"Processing page {page_num + 1}...")
        # Extract tables from the page
        tables = page.extract_tables()
 
        print(f"Found {len(tables)} tables on page {page_num + 1}")
 
        # Iterate through all tables and filter rows containing "MPL"
        for table_index, table in enumerate(tables):
            headers = table[0] if table else []
 
            # Filter rows with "MPL"
            mpl_rows = [row for row in table[1:] if any("MPL" in (str(cell) if cell else "") for cell in row)]
            print(f"Rows with 'MPL' in Table {table_index + 1} on page {page_num + 1}: {mpl_rows}")
 
            if mpl_rows:
                extracted_data.append({
                    'headers': headers,
                    'rows': mpl_rows
                })
 
    if extracted_data:
        pdf_data_list.append({
            'report_name': report_name,
            'data': extracted_data
        })
 
def save_data_to_csv():
    for pdf_data in pdf_data_list:
        csv_file_path = f"{pdf_data['report_name']}_mpl.csv"
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
 
            for data in pdf_data['data']:
                writer.writerow(data['headers'])
                writer.writerows(data['rows'])
 
        print(f"Data containing 'MPL' has been saved to {csv_file_path}")
 
# Selenium webdriver setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
 
driver = webdriver.Chrome(options=chrome_options)
 
url = 'https://erpc.gov.in/ui-and-deviation-accts/'
print(f"Opening URL: {url}")
driver.get(url)
time.sleep(5)
current_year = datetime.now().year
 
title_regex = re.compile(rf"{current_year}")
 
pdf_links = driver.find_elements(By.CSS_SELECTOR, 'a[href*=".pdf"]')
print("Found PDF links on the page:")
for link in pdf_links:
    title = link.get_attribute('title')
    pdf_url = link.get_attribute('href')
    print(f"Title: {title}, URL: {pdf_url}")
 
# Check for PDFs matching required criteria
for link in pdf_links:
    title = link.get_attribute('title')
    pdf_url = link.get_attribute('href')
 
    if all(keyword in title for keyword in required_keywords):
        print(f"Found PDF with all required keywords: {title}")
        report_name = re.sub(r'[^\w\s]', '_', title)
        extract_pdf_data(pdf_url, report_name)
 
# Close the driver
driver.quit()
 
# Save all accumulated data to CSV files
save_data_to_csv() 


