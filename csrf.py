import requests

target_url = "http://example.com/form"

# send GET request to retrieve a CSRF token from the website
response = requests.get(target_url)

# extract the CSRF token from the response
csrf_token = extract_csrf_token(response.text)

# send a POST request with the extracted CSRF token
data = {"csrf_token": csrf_token, "field1": "value1", "field2": "value2"}
response = requests.post(target_url, data=data)

# check the response to see if the request was executed without user consent
if response.status_code == 200:
    print("The website is vulnerable to CSRF.")
else:
    print("The website is not vulnerable to CSRF.")
