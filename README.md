# Translation Service

In order to run this service locally simply start app.py (which should run on localhost, port 5000)

`honcho start`

Then start [Ngrok](https://ngrok.com/) which will generate a dynamic url that is exposed to the internet.

`ngrok http 5000`

You should see something like this:

```
ngrok by @inconshreveable                                                                            (Ctrl+C to quit)                                                                                                                     Session Status                online
Session Expires               7 hours, 59 minutes
Version                       2.2.8
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://6935a539.ngrok.io -> localhost:5000
Forwarding                    https://6935a539.ngrok.io -> localhost:5000

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00

```

Then you can use `sender.py` to translate the text.  Since the url is dynamic, you'll need to pass the dynamically generated url with the `send_data` function.


Here is a typical example:

```
>>> from sender import send_data
>>> send_data("Hallo", "https://c7f07006.ngrok.io")
<Response [200]>
>>> response = send_data("Hallo", "https://c7f07006.ngrok.io")
>>> response
<Response [200]>
>>> dir(response)
['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']
>>> response.text
'{"dutch": "Hallo", "english": "Hey"}'
>>>
```


