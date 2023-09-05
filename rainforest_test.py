import requests

base_url = 'https://www.letsrevolutionizetesting.com/challenge.json'

def send(url):
    print(f"Following: {url}")
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = response.json()
        
        if 'follow' in json_data:
            follow_id = json_data['follow'].split("=")[1]
            new_url = f"{base_url}?id={follow_id}"
            send(new_url)
        else:
            print(f"End reached: {json_data['message']}")
    else:
        print(f"Failed to fetch data from {url}, status code: {response.status_code}")

# Usage:
send(base_url)
