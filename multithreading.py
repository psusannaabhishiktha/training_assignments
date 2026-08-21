# A service calls many independent APIs and is slow. How would you use multithreading to improve the total response time?​

# urls = [​
# "https://api.example.com/users/1",​
# "https://api.example.com/users/2",​
# "https://api.example.com/users/3",​
# ]​

#--------------------------------------

# import required libraries
# create list of API URLs
# define function to call API and return response
# use ThreadPoolExecutor to call APIs concurrently
# collect and print results

import requests
from concurrent.futures import ThreadPoolExecutor
urls = [
    "https://api.example.com/users/1",
    "https://api.example.com/users/2",
    "https://api.example.com/users/3"
]

def call_api(url):
    response = requests.get(url)
    return response.json()

with ThreadPoolExecutor() as executor:
    results = executor.map(call_api, urls)

for result in results:
    print(result)