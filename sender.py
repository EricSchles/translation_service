import requests
import json

def send_data(text, url):
    """
    This function sends data to the google translate service.
    The default for this function is to translate dutch to english.
    
    Parameters:
    @text - the dutch text to be translated
    @url - the unique url to pass to send the request
    
    Testing on localhost:
    ```
    send_data('halo', 'http://localhost:5000/')
    ```

    Notice that we need not specify an end point, this is because the
    service only has the one translation endpoint.
    
    For translation over the web, we must use tunneling to create a dynamic
    web address.  For this we use a Python3 Fork of PageKite, found here:
    https://www.github.com/EricSchles/PyPageKite && 
    https://www.github.com/EricSchles/PySocksipyChain

    OR 
    ngrok found here:

    To make ngrok work with the Windows Linux Subsystem you'll need to run the following command:
    
    `ngrok http 3000 --log stderr`
    
    Using these two packages we are able to tunnel to the internet, without having
    to deploy anything!  Then this function can be called from the dynamically generated
    web address by PyPageKite.  This allows you to use it as a true service on the internet.
    """
    dutch_text = {}
    dutch_text["text"] = text
    return requests.post(url, json=json.dumps(dutch_text))
