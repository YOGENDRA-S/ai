import requests

urls = ['http://example.com/page1', 'http://example.com/page2', 'http://example.com/page3']
payloads = ['/?admin=1', '/?user=2']

for url in urls:
    for payload in payloads:
        test_url = url + payload
        try:
            response = requests.get(test_url)
            if response.status_code == 200:
                if "Unauthorized" not in response.text:
                    print(f'Possible Broken Access Control vulnerability found in {test_url}')
        except requests.exceptions.RequestException as e:
            print(e)
  
  import requests

def scan_url_for_sql_injection(url):
    payloads = ['\'', '\"', ' OR 1=1 --']
    for payload in payloads:
        response = requests.get(url + payload)
        if "error" in response.text.lower():
            print(f"Possible SQL Injection vulnerability detected in {url}")
            break

url_list = [
    "http://example.com/search?q=",
    "http://example.com/login?username=",
    "http://example.com/products?id="
]

for url in url_list:
    scan_url_for_sql_injection(url)
