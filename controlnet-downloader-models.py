#******************************************************************************#
#                                                                              #
#                   controlnet-downloader-models.py                            #
#                                                                              #
#   Date: 2021/09/27                                                           #
#   This script downloads the .pth files of the ControlNet models from the     #
#   HuggingFace repository.                                                    #
#   version: 0.0.1                                                             #
#   Author: Carlos Rocha - Dez/2023, Brazil                                    #
#   repository: https://github.com/carlosrocha-dev/controlnet-downloader.git   #
#                                                                              #
#******************************************************************************#

from bs4 import BeautifulSoup
import requests
import os
from tqdm import tqdm

# URL of the page to scrape
url = 'https://huggingface.co/lllyasviel/ControlNet-v1-1/tree/main'

# Base URL for downloading files
base_download_url = 'https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/'

# Folder to save the .pth files
destination_folder = './'

# Create the destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Function to check if the content of a file is HTML
def is_html_file(file_path):
    with open(file_path, 'rb') as file:
        # Read the first 1024 bytes to check for HTML tags
        content = file.read(1024)
        return b'<!DOCTYPE html>' in content or b'<html' in content

# Function to download .pth files
def download_pth_files(url, destination_folder):
    try:
        # Send a request to the webpage
        response = requests.get(url)
        response.raise_for_status()

        # Parse the webpage content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all SVG elements that match the download icon
        svg_icons = soup.find_all('svg', {'aria-hidden': 'true', 'focusable': 'false', 'role': 'img'})

        # Extract the parent <a> tags which contain the download links
        pth_links = [svg.find_parent('a')['href'] for svg in svg_icons if svg.find_parent('a') and svg.find_parent('a')['href'].endswith('.pth')]

        # Download each .pth file
        for link in pth_links:
            # Extract the filename
            file_name = link.split('/')[-1]

            # Construct the complete file URL
            file_url = base_download_url + file_name + '?download=true'

            # Full path to save the file
            file_path = os.path.join(destination_folder, file_name)

            # Get the file size
            response = requests.get(file_url, stream=True)
            total_size_in_bytes = int(response.headers.get('content-length', 0))

            # Download and save the file
            with requests.get(file_url, stream=True) as file_response:
                with open(file_path, 'wb') as f, tqdm(
                    desc=file_name,
                    total=total_size_in_bytes,
                    unit='iB',
                    unit_scale=True,
                    unit_divisor=1024,
                ) as bar:
                    for chunk in file_response.iter_content(chunk_size=8192):
                        size = f.write(chunk)
                        bar.update(size)

            # Check if the downloaded file is an HTML file
            if is_html_file(file_path):
                os.remove(file_path)
                print(f"Deleted HTML file: {file_name}")

        return "Download completed successfully."
    except Exception as e:
        return f"An error occurred: {e}"

# Execute the function
download_pth_files(url, destination_folder)
