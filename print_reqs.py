import requests

print(requests.__version__)

requests.get('http://google.com')

print(requests.get(
    'https://raw.githubusercontent.com/asvpglory/404Lab1/main/print_reqs.py').content)
