import zipfile
import os
import requests

def download_and_extract(url, extract_to='arhiva'):
    # Descărcarea arhivei
    response = requests.get(url)
    with open("arhiva.zip", "wb") as f:
        f.write(response.content)

    # Extrage fișierele din arhivă
    with zipfile.ZipFile("arhiva.zip", "r") as zip_ref:
        zip_ref.extractall(extract_to)

    # Verifică fișierele extrase
    for root, dirs, files in os.walk(extract_to):
        for file in files:
            print(file)

if __name__ == "__main__":
    url = "https://drive.google.com/uc?id=1CEx_TnzAlTMEGqqq5O2QXKoz8fPOUjW8"
    download_and_extract(url)
