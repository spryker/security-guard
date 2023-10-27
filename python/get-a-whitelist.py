import requests
import json

url = "https://10.111.11.10/api/exception_lists/items/_find?list_id=6426f7c3-fc86-4a78-bbd5-4c8b3147aeee&per_page=90"
headers = {
    "kbn-xsrf": "true",
    "Content-Type": "application/json"
}
user = "AddSprykerUserToWhitelist"
password = "a*4tB8PVrHaTV6heJ9v7HGh%6wzc#b*m"

try:
    response = requests.get(url, headers=headers, auth=(user, password), verify=False)
    response.raise_for_status()  # Raise an exception for 4xx or 5xx HTTP status codes

    data = response.json()
    with open("report.json", "w") as report_file:
        json.dump(data, report_file, indent=4)

    with open("report.json", "r") as report_file:
        print(report_file.read())
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
