#!/bin/bash

# Read the input file line by line
while IFS= read -r line
do
  # Split the line into parts using ',' as the delimiter
  IFS=',' read -ra parts <<< "$line"

  # Check if there are at least four parts
  if [ ${#parts[@]} -ge 4 ]; then
    email="${parts[0]}"
    isp="${parts[1]}"
    country="${parts[2]}"
    city="${parts[3]}"
    echo
    echo 
    # Now you can use these variables as needed
    echo "Email: $email"
    echo "Company: $isp"
    echo "Country: $country"
    echo "City: $city"
    username=$(echo "$email" | cut -d "@" -f 1)
    echo "username: $username"
    echo

    # Create a JSON template with placeholders for variables
json_template='{
  "description": "Exception list item",
  "entries": [
    {
      "field": "resource.accessKeyDetails.principalId",
      "operator": "included",
      "type": "match",
      "value": "*:%s"
    },
    {
      "field": "service.action.awsApiCallAction.remoteIpDetails.organization.isp",
      "operator": "included",
      "type": "match",
      "value": "%s"
    },
    {
      "field": "service.action.awsApiCallAction.remoteIpDetails.country.countryName",
      "operator": "included",
      "type": "match",
      "value": "%s"
    },
    {
      "field": "service.action.awsApiCallAction.remoteIpDetails.city.cityName",
      "operator": "included",
      "type": "match",
      "value": "%s"
    }
  ],
  "expire_time": "2024-11-11T09:56:42.919Z",
  "list_id": "6426f7c3-fc86-4a78-bbd5-4c8b3147aeee",
  "name": "%s/%s",
  "namespace_type": "single",
  "type": "simple"
}'

# Use printf to insert the external variables into the JSON template
json_data=$(printf "$json_template" "$email" "$isp" "$country" "$city" "$username" "$country")

curl -X POST -k "https://10.111.11.10/api/exception_lists/items" \
-u <user_name>:<password> \
-H 'kbn-xsrf: true' \
-H "Content-Type: application/json" \
-d "$json_data" >> curl-results.json && less /home/itsec/sp/diesec/curl-results.json | jq
  else
    echo "Invalid line: $line"
  fi

done < stafflist.txt

exit
