import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

def fetch_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    file_links = set()
    folder_links = set()

    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('/kreemkhaled112/ahmed/blob'):
            file_links.add(href)
        elif href and href.startswith('/kreemkhaled112/ahmed/tree'):
            folder_links.add(href)

    return file_links, folder_links

def process_folders(base_url, folders, file_links):
    new_folders = set()
    for folder in folders:
        full_url = f"{base_url}{folder}"
        flinks, flolders = fetch_links(full_url)
        file_links.update(flinks)
        new_folders.update(flolders)

    return new_folders

def recursive_folder_process(base_url, folders, file_links):
    while folders:
        folders = process_folders(base_url, folders, file_links)

def download_files(base_url, file_links):
    for link in file_links:
        download_url = f"{base_url}{link.replace('/blob', '/raw')}"
        path = link.replace('/kreemkhaled112/ahmed/blob/master/', '')
        path = unquote(path)  # Decode URL encoded characters.
        
        # Create directory structure if it doesn't exist.
        os.makedirs(os.path.dirname(path), exist_ok=True)
        
        # Download and save the file.
        response = requests.get(download_url)
        if response.status_code == 200:
            with open(path, 'wb') as file:
                file.write(response.content)
        else:
            print(f"Failed to download {path}")

base_url = "https://github.com"
initial_url = f"{base_url}/kreemkhaled112/ahmed"
files, folders = fetch_links(initial_url)

recursive_folder_process(base_url, folders, files)
download_files(base_url, files)
