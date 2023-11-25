import requests
import os
import time
from dotenv import load_dotenv
import pandas as pd
import json

load_dotenv()
API_KEY = os.environ.get('BING_API_KEY') 
ENDPOINT = 'https://api.bing.microsoft.com/v7.0/images/search'

def search_images(query,count=50):
    headers = {'Ocp-Apim-Subscription-Key': API_KEY}
    params = {'q': query, 'count': count}  # Adjust count as needed
    response = requests.get(ENDPOINT, headers=headers, params=params)
    
    response.raise_for_status()
    return response.json() , response

def download_images(image_urls, folder_name):
    os.makedirs(folder_name, exist_ok=True)
    for i, url in enumerate(image_urls):
        try:
            img_data = requests.get(url).content
            with open(os.path.join(folder_name, f'{i}.jpg'), 'wb') as file:
                file.write(img_data)
            
        except Exception as e:
            print(f"Error downloading {url}: {e}")

def main(celebrities):
    
    for i , celeb in enumerate(celebrities):
        folder_name = f'Arab_Celebs_Data/{i}_{celeb}'
        print(f"Searching images for {celeb}")
        response , good= search_images(f"{celeb} arab celebrity clear image")
        print(good)
        os.makedirs(folder_name, exist_ok=True)
        with open(os.path.join(folder_name, f'{i}_{celeb}.json'), 'w') as file:
            json.dump(response, file)
        image_urls = [img['thumbnailUrl'] for img in response['value']]
        download_images(image_urls, f'Arab_Celebs_Data/{i}_{celeb}')
        time.sleep(1)  # Rate limiting



# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('celebrities.csv')

# Get the list of celebrities
celebrities = df['Name'].tolist()

main(celebrities)


