import subprocess
import json

# in progress - is not read yet

# Read the input file line by line
# TODO: replace absolute path to the relative path
with open("/home/itsec/sp/diesec/security-guard/python/stafflist.txt", "r") as file:
    for line in file:
        # Split the line into parts using ',' as the delimiter
        parts = line.strip().split(',')

        # Check if there are at least four parts
        if len(parts) >= 4:
            email = parts[0]
            isp = parts[1]
            country = parts[2]
            city = parts[3]

            # Now you can use these variables as needed
            print()
            print("Email:", email)
            print("Company:", isp)
            print("Country:", country)
            print("City:", city)
            username = email.split('@')[0]
            print("Username:", username)
            print()

            # Create a JSON dictionary with placeholders for variables
            json_data = {
                "description": "Exception list item",
                "entries": [
                    {
                        "field": "resource.accessKeyDetails.principalId",
                        "operator": "included",
                        "type": "match",
                        "value": f"*:{email}"
                    },
                    {
                        "field": "service.action.awsApiCallAction.remoteIpDetails.organization.isp",
                        "operator": "included",
                        "type": "match",
                        "value": isp
                    },
                    {
                        "field": "service.action.awsApiCallAction.remoteIpDetails.country.countryName",
                        "operator": "included",
                        "type": "match",
                        "value": country
                    },
                    {
                        "field": "service.action.awsApiCallAction.remoteIpDetails.city.cityName",
                        "operator": "included",
                        "type": "match",
                        "value": city
                    }
                ],
                "expire_time": "2024-11-11T09:56:42.919Z",
                "list_id": "6426f7c3-fc86-4a78-bbd5-4c8b3147aeee",
                "name": f"{username}/{city}",
                "namespace_type": "single",
                "type": "simple"
            }

            # Convert the JSON dictionary to a JSON string
            json_str = json.dumps(json_data)

            # Execute the curl command using subprocess
            # TODO: replace creds with variables
            curl_command = [
                "curl",
                "-X", "POST",
                "-k", "https://10.111.11.10/api/exception_lists/items",
                "-u", "username:userpassword",
                "-H", "kbn-xsrf: true",
                "-H", "Content-Type: application/json",
                "-d", json_str
            ]

            # Run the curl command and capture the output
            # TODO: replace absolute path to the relative path
            result = subprocess.run(curl_command, stdout=subprocess.PIPE, text=True)
            with open("/home/itsec/sp/diesec/security-guard/python/curl-results.json", "a") as result_file:
                result_file.write(result.stdout)

        else:
            print("Invalid line:", line.strip())

# End of the script
