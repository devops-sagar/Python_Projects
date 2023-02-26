import requests

'''3 various URLs for testing purpose'''
# x = requests.get("https://devops-sagar.github.io/portfolio/")
# x = requests.get("https://cc.csusm.edu/", timeout=0.3)                               # timeout will close the request withing define value and gives error if elapsed time is more then the parameter value - Check (x.elapsed) in line-16 which is the actual time took to serve the request
x = requests.get("https://csusm.instructure.com/")

print(f"Response URL is: {x.url}")                                                     # returns the URL of the response
print(f"Status code object will be: {x}")                                              # returns status code object
print(f"Status code will be: {x.status_code}")                                         # returns status code
print(f"Status code says: {x.reason}")                                                 # returns a text corresponding to the status code
print(f"which request object requested this reponse?: {x.request}")                    # returns the request object that requested this response
# print(f"Content of the response will be: {x.text}")                                  # returns the content of the response, in unicode
print(f"Apparent Encoding will be: {x.apparent_encoding}")                             # returns apparent Encoding
# print(f"Web site content in bytes will be: {x.content}")                             # returns the content of the response in bytes
print(f"Cookies sent back from the website is: {x.cookies}")                           # returns cookies sent back from the server
print(f"Time taken to process this request will be: {x.elapsed}")                      # returns time spent from requesting and arriving of a server request
print(f"To decode the content, this will be the encoding type: {x.encoding}")          # returns the encoding used to decode request text
print(f"Dictionary of response header contains: {x.headers}")                          # returns dictionary of response headers
print(f"History of request in the format of response object: {x.history}")             # returns a list of response objects holding the history of request
print(f"Is this permanent redirect URL: {x.is_permanent_redirect}")                    # returns True if the response is the permanent redirected url, otherwise False
print(f"Is the response redirected: {x.is_redirect}")                                  # returns True if the response was redirected, otherwise False
print(f"Iterating Content: {x.iter_content()}")                                        # iterate over the response and getting in form of bytes
# for i in x.iter_content():                                                           # Iterate over the response and getting elements
#     print(i)
print(f"Iterating Content lines: {x.iter_lines()}")                                    # iterates over the lines of the response
# for i in x.iter_lines():                                                             # Iterate over the response line by line
#     print(i)
# print(f"Results in format of json obejct: {x.json()}")                               # returns Returns a JSON object of the result (if the result was written in JSON format, if not it raises an error)
print(f"Header links will be: {x.links}")                                              # returns header links
print(f"If Error occured this is the statement: {x.raise_for_status}")                 # if an error occur, this method returns a HTTPError object
x.close()                                                                              # closes the connection to the server

'''
From here there is a POST request demo to demonstrarte the data posting
'''

url = 'https://jsonplaceholder.typicode.com/posts'

data = {
    "id": 5,
    "title": 'Software Engineer',
    "body": 'TCS',
    "userId": 1818688,
}

response = requests.post(url, json=data)
print(response.text)
