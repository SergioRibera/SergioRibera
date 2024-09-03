import requests
import json

def fetch_api_data(limit = 10):
    # Replace this URL with your actual API endpoint
    api_url = "https://api.github.com/search/repositories?q=owner%3ASergioRibera+sort%3Astars+archived%3Afalse&type=repositories&s=stars&o=desc"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        
        data = response.json()
        
        # Process the data and create the desired structure

        return list(islice(({
                "name": item["name"],
                "description": item["description"]
            } for item in data['items']
            if item['description'] and item['description'] != ''), 
        limit))
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    result = fetch_api_data()
    
    if result:
        with open("data/projects.json", "w") as f:
            json.dump(result, f, indent=2)
        print("Data saved successfully")
    else:
        print("Failed to fetch or process data")
