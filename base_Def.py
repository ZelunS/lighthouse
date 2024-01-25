import json
import os
import yaml
import jmespath
import jsonpath
import datetime

class getInfo:

    def read_summary(self):
        with open(os.getcwd() + "/report/lighthouse/summary.json",encoding='utf-8',errors='ignore') as summary:
            report = json.load(summary)
            return report

    def write_baseUrl(self):
        with open(os.getcwd() + "/LT_url.txt",  mode='a',encoding='utf-8', errors='ignore') as txt:
            txt.write('https://www.litime.com/''\n' 
                      'https://ca.litime.com/''\n'
                      'https://www.litime.de/''\n'
                      'https://uk.litime.com/''\n'
                      'https://jp.litime.com/''\n'
                      'https://au.litime.com/')

    def write_lighthouse_LTurl(self,data):
        with open(os.getcwd() + "/LT_url.txt",  mode='a',encoding='utf-8', errors='ignore') as txt:
            txt.write('\n' + data)

    def clear_lighthouse_LTurl(self):
        with open(os.getcwd() + "/LT_url.txt",  mode='w', encoding='utf-8') as txt:
            txt.truncate()

    def write_LT_yaml(self, data):
        with open(os.getcwd() + "/random_LT.yml", mode='a', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    def read_LT_yaml(self, key):
        with open(os.getcwd() + "/random_LT.yml", mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]

    def clear_LT_yaml(self):
        with open(os.getcwd() + "/random_LT.yml", mode='w', encoding='utf-8') as f:
            f.truncate()

class product_strip:

    def strip_US(self,product):
        product_name = product.strip("\n Sale New")
        return product_name

    def strip_CA(self,product):
        product_name = product.strip("\r\n ")
        return product_name

    def strip_DE(self,product):
        product_name = product.strip("\r\n ")
        return product_name

    def strip_UK(self,product):
        product_name = product.strip("\r\n Sale")
        return product_name

    def strip_JP(self,product):
        product_name = product.strip("\r\n ホット 新規 セール")
        return product_name

    def strip_AU(self,product):
        product_name = product.strip("\r\n Sale New")
        return product_name

    def strip_En(self,product):
        product_name = product.strip("\r\n Sale New")
        return product_name

def time_number(n):
    return n * 100

def list_join(list):
    num = "".join([str(x) for x in list])
    return num

def switch(list):
    num = time_number(float(list_join(list)))
    return num

def score_search(country):
    report = getInfo().read_summary()
    num = jmespath.search("[?url=='"+country+"'].score",report)
    return num

def num_search(country,target):
    report = getInfo().read_summary()
    num = jmespath.search("[?url=='"+country+"'].detail."+target+"",report)
    return num

def practices_search(country):
    report = getInfo().read_summary()
    num = switch(jsonpath.jsonpath(report,'$..[?(@.url=="'+country+'")]..best-practices'))
    print(num)
    return num

def data_time():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now)
    return now

def product_lk(base_url,product_url):
    p_links = None
    if base_url not in product_url:
        p_links = base_url + product_url
    elif base_url in product_url:
        p_links = product_url
    return p_links

def product_search(name,target):
    info = ""
    if name == "LT_US":
        if target == "product_name":
            info = getInfo().read_LT_yaml('LTUS随机商品名称')
        elif target == "product_link":
            info = getInfo().read_LT_yaml('LTUS随机商品链接')
    elif name == "LT_CA":
        if target == "product_name":
            info = getInfo().read_LT_yaml('LTCA随机商品名称')
        elif target == "product_link":
            info = getInfo().read_LT_yaml('LTCA随机商品链接')
    elif name == "LT_DE":
        if target == "product_name":
            info = getInfo().read_LT_yaml('LTDE随机商品名称')
        elif target == "product_link":
            info = getInfo().read_LT_yaml('LTDE随机商品链接')
    elif name == "LT_UK":
        if target == "product_name":
            info = getInfo().read_LT_yaml('LTUK随机商品名称')
        elif target == "product_link":
            info = getInfo().read_LT_yaml('LTUK随机商品链接')
    elif name == "LT_JP":
        if target == "product_name":
            info = getInfo().read_LT_yaml('LTJP随机商品名称')
        elif target == "product_link":
            info = getInfo().read_LT_yaml('LTJP随机商品链接')
    elif name == "LT_AU":
        if target == "product_name":
            info = getInfo().read_LT_yaml('LTAU随机商品名称')
        elif target == "product_link":
            info = getInfo().read_LT_yaml('LTAU随机商品链接')
    return info

def productScore_search(counrty):
    report = getInfo().read_summary()
    product_score = ""
    if counrty == "LT_US":
        product_link = getInfo().read_LT_yaml('LTUS随机商品链接')
        product_score = jmespath.search("[?url=='"+product_link+"'].score",report)
    elif counrty == "LT_CA":
        product_link = getInfo().read_LT_yaml('LTCA随机商品链接')
        product_score = jmespath.search("[?url=='"+product_link+"'].score",report)
    elif counrty == "LT_DE":
        product_link = getInfo().read_LT_yaml('LTDE随机商品链接')
        product_score = jmespath.search("[?url=='"+product_link+"'].score",report)
    elif counrty == "LT_UK":
        product_link = getInfo().read_LT_yaml('LTUK随机商品链接')
        product_score = jmespath.search("[?url=='"+product_link+"'].score",report)
    elif counrty == "LT_JP":
        product_link = getInfo().read_LT_yaml('LTJP随机商品链接')
        product_score = jmespath.search("[?url=='"+product_link+"'].score",report)
    elif counrty == "LT_AU":
        product_link = getInfo().read_LT_yaml('LTAU随机商品链接')
        product_score = jmespath.search("[?url=='"+product_link+"'].score",report)
    return product_score
