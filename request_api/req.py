import requests

response = requests.get("https://devops-sagar.github.io/portfolio/")
print(response)         # returns status code
print(response.text)    # returns source code
