import requests

target_urls = [
    "http://example.com/redirect?url=http://evil.com",
    "http://example.com/redirect?url=https://good.com",
    # ...
]

for target_url in target_urls:
    response = requests.get(target_url)
    if response.url.startswith("http://evil.com"):
        print(f"{target_url} is vulnerable to Open Redirect.")
    else:
        print(f"{target_url} is not vulnerable to Open Redirect.")
