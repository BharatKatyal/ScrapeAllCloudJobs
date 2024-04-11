import csv
import requests
import time

def fetch_job_details_and_save_to_csv(input_csv_filename, output_csv_filename, url_template):
    first_job_processed = False

    # Read the job IDs from the input CSV file
    with open(input_csv_filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            job_id = row['Id']

            # Construct the URL for the GET request using the job ID
            url = url_template.format(job_id=job_id)

            # Make the GET request
            response = requests.get(url)
            if response.status_code == 200:
                job_details = response.json()['items'][0]  # Assuming the first item contains the job details

                # If this is the first job being processed, determine the fieldnames and write the header
                if not first_job_processed:
                    fieldnames = list(job_details.keys())  # Dynamically determine fieldnames from the first job details
                    with open(output_csv_filename, 'w', newline='', encoding='utf-8') as file:
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerow(job_details)  # Write the first job's details
                    first_job_processed = True
                else:
                    # For subsequent jobs, just open the file in append mode and write the job details
                    with open(output_csv_filename, 'a', newline='', encoding='utf-8') as file:
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writerow(job_details)

                # Add a delay to avoid hitting the endpoint too much
                time.sleep(2)

# Example usage
input_csv_filename = 'oracle_jobs_data.csv'
output_csv_filename = 'oracle_jobs_data_job_details_incremental.csv'
url_template = 'https://eeho.fa.us2.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitionDetails?expand=all&onlyData=true&finder=ById;Id="{job_id}",siteNumber=CX_45001'  # Base URL for fetching data; replace with the actual URL and format
fetch_job_details_and_save_to_csv(input_csv_filename, output_csv_filename, url_template)

