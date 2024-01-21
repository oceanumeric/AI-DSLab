import requests
from loguru import logger



def download_data(url, filename):
    """
    Download data from url and save it to filename
    """
    # send the request
    response = requests.get(url)
    # check if the request was successful
    if response.status_code != 200:
        logger.error(f"Request failed with status code {response.status_code}")
        return None
    
    # save the data to file
    with open(filename, "w") as f:
        f.write(response.text)
    
    logger.info(f"Data saved to {filename}")
    


if __name__ == "__main__":
    url = "https://api.inc.com/rest/i5list/2023"
    filename = "data/inc5000_2023.json"
    download_data(url, filename)
