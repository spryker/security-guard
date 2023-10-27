#!/bin/bash

curl -X GET -k "https://10.111.11.10/api/exception_lists/items/_find?list_id=6426f7c3-fc86-4a78-bbd5-4c8b3147aeee&per_page=90" \
-u <user_name>:<password> \
-H 'kbn-xsrf: true' \
-H "Content-Type: application/json" \
| jq > report.json
