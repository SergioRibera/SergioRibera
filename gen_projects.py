import requests
import json

def fetch_api_data():
    # Replace this URL with your actual API endpoint
    api_url = "https://api.github.com/search/repositories?q=owner%3ASergioRibera+sort%3Astars+archived%3Afalse&type=repositories&s=stars&o=desc"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        
        data = response.json()
        
        # Process the data and create the desired structure
        processed_data = []
        for i in range(10):
            item = data['items'][i]
            if not item['description'] or len(item['description']) == 0:
                continue
            processed_item = {
                "name": item["name"],
                "description": item["description"]
            }
            processed_data.append(processed_item)
        
        return processed_data
    
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
