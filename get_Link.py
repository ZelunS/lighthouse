import requests
import os
import collections
from bs4 import BeautifulSoup
from proxy import proxy_req,proxyRequests
import json
from base_Def import getInfo,product_strip,product_lk
import random

def catch_LTUSproduct():
    url = 'https://www.litime.com'
    response = proxyRequests().proxy_Requests("get",url,None,None)
    soup = BeautifulSoup(response.content, 'html.parser')
    menu_column = soup.find('div', class_='menu-dropdown__column column-4 column-full')
    links = menu_column.find_all('a')
    product_links = {}
    for link in links:
        product_name = product_strip().strip_En(link.text)
        product_link = product_lk(url,link.get('href'))
        print("LT-US的商品名称： "+product_name)
        if "Go to" not in product_name and product_link != None:
            product_links[product_name] = product_link
        else:
            pass
    items = list(product_links.items())
    random_items = random.choice(items)
    print(random_items)
    # getInfo().clear_LT_yaml()
    getInfo().write_LT_yaml({'LTUS随机商品名称': random_items[0]})
    getInfo().write_LT_yaml({'LTUS随机商品链接': random_items[1]})

def catch_LTCAproduct():
    url = 'https://ca.litime.com'
    response = proxyRequests().proxy_Requests("get",url,None,None)
    soup = BeautifulSoup(response.content, 'html.parser')
    menu_column = soup.find('div', class_='menu-dropdown__wrapper')
    links = menu_column.find_all('a')
    product_links = {}
    for link in links:
        product_name = product_strip().strip_En(link.text)
        product_link = product_lk(url,link.get('href'))
        print("LT-CA的商品名称： "+product_name)
        if "Go to" not in product_name and product_link != None:
            product_links[product_name] = product_link
        else:
            pass
    items = list(product_links.items())
    random_items = random.choice(items)
    print(random_items)
    # getInfo().clear_LT_yaml()
    getInfo().write_LT_yaml({'LTCA随机商品名称': random_items[0]})
    getInfo().write_LT_yaml({'LTCA随机商品链接': random_items[1]})

def catch_LTDEproduct():
    url = 'https://www.litime.de'
    response = proxyRequests().proxy_Requests("get",url,None,None)
    soup = BeautifulSoup(response.content, 'html.parser')
    menu_column = soup.find('div', class_='menu-dropdown custom-scrollbar megamenu_style_2')
    links = menu_column.find_all('a')
    product_links = {}
    for link in links:
        product_name = product_strip().strip_En(link.text)
        product_link = product_lk(url,link.get('href'))
        print("LT-DE的商品名称： "+product_name)
        if "Gehe zu" not in product_name and product_link != None:
            product_links[product_name] = product_link
        else:
            pass
    items = list(product_links.items())
    random_items = random.choice(items)
    print(random_items)
    # getInfo().clear_LT_yaml()
    getInfo().write_LT_yaml({'LTDE随机商品名称': random_items[0]})
    getInfo().write_LT_yaml({'LTDE随机商品链接': random_items[1]})

def catch_LTUKproduct():
    url = 'https://uk.litime.com'
    response = proxyRequests().proxy_Requests("get", url, None, None)
    soup = BeautifulSoup(response.content, 'html.parser')
    menu_column = soup.find('div', class_='menu-dropdown__wrapper')
    links = menu_column.find_all('a')
    product_links = {}
    for link in links:
        product_name = product_strip().strip_En(link.text)
        product_link = product_lk(url, link.get('href'))
        print("LT-UK的商品名称： "+product_name)
        if "Go to" not in product_name and product_name != '' and product_link != None:
            product_links[product_name] = product_link
        else:
            pass
    items = list(product_links.items())
    random_items = random.choice(items)
    print(random_items)
    # getInfo().clear_LT_yaml()
    getInfo().write_LT_yaml({'LTUK随机商品名称': random_items[0]})
    getInfo().write_LT_yaml({'LTUK随机商品链接': random_items[1]})

def catch_LTJPproduct():
    url = 'https://jp.litime.com'
    response = proxyRequests().proxy_Requests("get", url, None, None)
    soup = BeautifulSoup(response.content, 'html.parser')
    menu_column = soup.find('div', class_='menu-dropdown__wrapper')
    links = menu_column.find_all('a')
    product_links = {}
    for link in links:
        product_name = product_strip().strip_JP(link.text)
        product_link = product_lk(url, link.get('href'))
        print("LT-JP的商品名称： "+product_name)
        if "に進む" not in product_name and product_name != '' and product_link != None:
            product_links[product_name] = product_link
        else:
            pass
    items = list(product_links.items())
    random_items = random.choice(items)
    print(random_items)
    # getInfo().clear_LT_yaml()
    getInfo().write_LT_yaml({'LTJP随机商品名称': random_items[0]})
    getInfo().write_LT_yaml({'LTJP随机商品链接': random_items[1]})

def catch_LTAUproduct():
    url = 'https://au.litime.com'
    response = proxyRequests().proxy_Requests("get", url, None, None)
    soup = BeautifulSoup(response.content, 'html.parser')
    menu_column = soup.find('ul', class_='header__submenu list-menu list-menu--disclosure list-menu--disclosure-1 caption-large motion-reduce')
    links = menu_column.find_all('a')
    product_links = {}
    for link in links:
        product_name = product_strip().strip_En(link.text)
        product_link = product_lk(url, link.get('href'))
        print("LT-AU的商品名称： "+product_name)
        if "Go to" not in product_name and product_name != '' and product_link != None:
            product_links[product_name] = product_link
        else:
            pass
    items = list(product_links.items())
    random_items = random.choice(items)
    print(random_items)
    # getInfo().clear_LT_yaml()
    getInfo().write_LT_yaml({'LTAU随机商品名称': random_items[0]})
    getInfo().write_LT_yaml({'LTAU随机商品链接': random_items[1]})

def catch_LT_Allproduct():
    getInfo().clear_LT_yaml()
    url = {'https://www.litime.com','https://ca.litime.com','https://www.litime.de','https://uk.litime.com','https://jp.litime.com','https://au.litime.com'}
    for a in url:
        response = proxyRequests().proxy_Requests("get",a,None,None)
        soup = BeautifulSoup(response.content, 'html.parser')

        if a == 'https://www.litime.com':
            menu_column = soup.find('div', class_='menu-dropdown__column column-4 column-full')
            links = menu_column.find_all('a')
            product_links = {}
            for link in links:
                product_name = product_strip().strip_En(link.text)
                product_link = product_lk(a, link.get('href'))
                if "Go to" not in product_name and product_name != '' and product_link != None:
                    product_links[product_name] = product_link
                else:
                    pass
            items = list(product_links.items())
            random_items = random.choice(items)
            print(random_items)
            getInfo().write_LT_yaml({'LTUS随机商品名称': random_items[0]})
            getInfo().write_LT_yaml({'LTUS随机商品链接': random_items[1]})
            getInfo().write_lighthouse_LTurl(random_items[1])

        elif a == 'https://ca.litime.com':
            menu_column = soup.find('div', class_='menu-dropdown__wrapper')
            links = menu_column.find_all('a')
            product_links = {}
            for link in links:
                product_name = product_strip().strip_En(link.text)
                product_link = product_lk(a, link.get('href'))
                if "Go to" not in product_name and product_name != '' and product_link != None:
                    product_links[product_name] = product_link
                else:
                    pass
            items = list(product_links.items())
            random_items = random.choice(items)
            print(random_items)
            getInfo().write_LT_yaml({'LTCA随机商品名称': random_items[0]})
            getInfo().write_LT_yaml({'LTCA随机商品链接': random_items[1]})
            getInfo().write_lighthouse_LTurl(random_items[1])

        elif a == 'https://www.litime.de':
            menu_column = soup.find('div', class_='menu-dropdown custom-scrollbar megamenu_style_2')
            links = menu_column.find_all('a')
            product_links = {}
            for link in links:
                product_name = product_strip().strip_En(link.text)
                product_link = product_lk(a, link.get('href'))
                if "Gehe zu" not in product_name and product_name != '' and product_link != None:
                    product_links[product_name] = product_link
                else:
                    pass
            items = list(product_links.items())
            random_items = random.choice(items)
            print(random_items)
            getInfo().write_LT_yaml({'LTDE随机商品名称': random_items[0]})
            getInfo().write_LT_yaml({'LTDE随机商品链接': random_items[1]})
            getInfo().write_lighthouse_LTurl(random_items[1])

        elif a == 'https://uk.litime.com':
            menu_column = soup.find('div', class_='menu-dropdown__wrapper')
            links = menu_column.find_all('a')
            product_links = {}
            for link in links:
                product_name = product_strip().strip_En(link.text)
                product_link = product_lk(a, link.get('href'))
                if "Go to" not in product_name and product_name != '' and product_link != None:
                    product_links[product_name] = product_link
                else:
                    pass
            items = list(product_links.items())
            random_items = random.choice(items)
            print(random_items)
            getInfo().write_LT_yaml({'LTUK随机商品名称': random_items[0]})
            getInfo().write_LT_yaml({'LTUK随机商品链接': random_items[1]})
            getInfo().write_lighthouse_LTurl(random_items[1])

        elif a == 'https://jp.litime.com':
            menu_column = soup.find('div', class_='menu-dropdown__wrapper')
            links = menu_column.find_all('a')
            product_links = {}
            for link in links:
                product_name = product_strip().strip_JP(link.text)
                product_link = product_lk(a, link.get('href'))
                if "に進む" not in product_name and product_name != '' and product_link != None:
                    product_links[product_name] = product_link
                else:
                    pass
            items = list(product_links.items())
            random_items = random.choice(items)
            print(random_items)
            getInfo().write_LT_yaml({'LTJP随机商品名称': random_items[0]})
            getInfo().write_LT_yaml({'LTJP随机商品链接': random_items[1]})
            getInfo().write_lighthouse_LTurl(random_items[1])

        elif a == 'https://au.litime.com':
            menu_column = soup.find('ul',class_='header__submenu list-menu list-menu--disclosure list-menu--disclosure-1 caption-large motion-reduce')
            links = menu_column.find_all('a')
            product_links = {}
            for link in links:
                product_name = product_strip().strip_En(link.text)
                product_link = product_lk(a, link.get('href'))
                if "Go to" not in product_name and product_name != '' and product_link != None:
                    product_links[product_name] = product_link
                else:
                    pass
            items = list(product_links.items())
            random_items = random.choice(items)
            print(random_items)
            getInfo().write_LT_yaml({'LTAU随机商品名称': random_items[0]})
            getInfo().write_LT_yaml({'LTAU随机商品链接': random_items[1]})
            getInfo().write_lighthouse_LTurl(random_items[1])

if __name__ == '__main__':
    getInfo().clear_lighthouse_LTurl()
    getInfo().write_baseUrl()
    # catch_LTUSproduct()
    # catch_LTCAproduct()
    # catch_LTDEproduct()
    # catch_LTUKproduct()
    # catch_LTJPproduct()
    # catch_LTAUproduct()
    catch_LT_Allproduct()
