import requests
import urllib.request
import json

def proxy_req(method,url,data,headers,**kwargs):
    proxy = "127.0.0.1:4780"
    proxies = {
        "http": proxy,
        "https": proxy
    }
    if method == "post":
        rep = requests.post(url=url,json=data, headers=headers,proxies=proxies,**kwargs)
        return rep
    elif method == "get":
        rep = requests.get(url=url,params=data,headers=headers,proxies=proxies,**kwargs)
        return rep

class proxyRequests:

    Session = requests.session()

    def proxy_Requests(self,method, url, data, headers, **kwargs):
        method = str(method).lower()
        proxy = "127.0.0.1:4780"
        proxies = {
            "http": proxy,
            "https": proxy
        }
        rep = None
        if method == "post":
            data=json.dumps(data)
            rep = proxyRequests.Session.request(method,url=url, json=data, headers=headers, proxies=proxies, **kwargs)
        elif method == "get":
            rep = proxyRequests.Session.request(method,url=url, params=data, headers=headers, proxies=proxies, **kwargs)
        return rep