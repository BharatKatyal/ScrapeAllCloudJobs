import requests
import csv

def fetch_jobs_and_save_to_csv(endpoint_url, csv_filename):
    # Make a GET request to the endpoint
    response = requests.get(endpoint_url)
    response.raise_for_status()  # This will raise an error if the request failed
    
    # Parse the JSON response
    jobs_data = response.json()['items'][0]['requisitionList']
    
    # Open a CSV file for writing
    with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write the header row
        headers = ['Id', 'Title', 'PostedDate', 'PrimaryLocation', 'PrimaryLocationCountry', 'ShortDescriptionStr']
        writer.writerow(headers)
        
        # Write job data rows
        for job in jobs_data:
            row = [job['Id'], job['Title'], job['PostedDate'], job['PrimaryLocation'], job['PrimaryLocationCountry'], job['ShortDescriptionStr']]
            writer.writerow(row)

# Example usage
endpoint_url = 'https://eeho.fa.us2.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitions?onlyData=true&expand=requisitionList.secondaryLocations,flexFieldsFacet.values&finder=findReqs;siteNumber=CX_45001,facetsList=LOCATIONS%3BWORK_LOCATIONS%3BWORKPLACE_TYPES%3BTITLES%3BCATEGORIES%3BORGANIZATIONS%3BPOSTING_DATES%3BFLEX_FIELDS,limit=100,lastSelectedFacet=AttributeChar6,locationId=300000000149325,selectedFlexFieldsFacets=%22AttributeChar6%7C0%20to%202%2B%20years%22,sortBy=POSTING_DATES_DESC'
csv_filename = 'oracle_jobs_data.csv'
fetch_jobs_and_save_to_csv(endpoint_url, csv_filename)
