# Source: "Implementing a Twitter feed in Python" by Matt Griffiths
# www.informaticscentre.co.cuk/news/view/26

import oauth2 as oauth
 
def Request(url, key, secret, http_method = 'GET', post_body = '', http_headers = ''):
    consumer = oauth.Consumer(key,secret) 
    token = oauth.Token(key, secret)
    client = oauth.Client(consumer, token)
  
    request = client.request(
        url,
        method = http_method,
        body = post_body,
        headers = http_headers)
    
    return request
    
