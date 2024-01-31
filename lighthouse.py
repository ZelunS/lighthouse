import os
from base_Def import getInfo,switch,score_search,num_search,practices_search,productScore_search,product_search
import jmespath
from send_Msg import send_success_msg,send_fail_msg
from get_Link import catch_LT_Allproduct
import subprocess

# def lightHouse():
#     os.system(f'npx lighthouse-batch -f LT_url.txt --html -p "--locale zh --preset=desktop"')
def lightHouse():
    command = f'npx lighthouse-batch -f LT_url.txt --html'
    subprocess.run(command, shell=True, check=True)

def check_all():
    report = getInfo().read_summary()
    url =  jmespath.search("[*].url",report)
    for key in url:

        if key == 'https://www.litime.com/':
            name = "LT_US"
            url = key
            score = switch(score_search("https://www.litime.com/"))
            if score != 0:
                performance = switch(num_search(key,"performance"))
                accessibility = switch(num_search(key,"accessibility"))
                practices = practices_search(key)
                seo = switch(num_search(key,"seo"))
                random_productName = product_search(name,"product_name")
                random_productLink = product_search(name,"product_link")
                random_productScore = switch(productScore_search(name))
                send_success_msg(name,url,score,performance,accessibility,practices,seo,random_productName,random_productLink,random_productScore)
            elif score == 0:
                send_fail_msg(name,url)

        elif key == 'https://ca.litime.com/':
            name = "LT_CA"
            url = key
            score = switch(score_search("https://ca.litime.com/"))
            if score != 0:
                performance = switch(num_search(key,"performance"))
                accessibility = switch(num_search(key,"accessibility"))
                practices = practices_search(key)
                seo = switch(num_search(key,"seo"))
                random_productName = product_search(name,"product_name")
                random_productLink = product_search(name,"product_link")
                random_productScore = switch(productScore_search(name))
                send_success_msg(name,url,score,performance,accessibility,practices,seo,random_productName,random_productLink,random_productScore)
            elif score == 0:
                send_fail_msg(name, url)

        elif key == 'https://www.litime.de/':
            name = "LT_DE"
            url = key
            score = switch(score_search("https://www.litime.de/"))
            if score != 0:
                performance = switch(num_search(key,"performance"))
                accessibility = switch(num_search(key,"accessibility"))
                practices = practices_search(key)
                seo = switch(num_search(key,"seo"))
                random_productName = product_search(name,"product_name")
                random_productLink = product_search(name,"product_link")
                random_productScore = switch(productScore_search(name))
                send_success_msg(name,url,score,performance,accessibility,practices,seo,random_productName,random_productLink,random_productScore)
            elif score == 0:
                send_fail_msg(name, url)

        elif key == 'https://uk.litime.com/':
            name = "LT_UK"
            url = key
            score = switch(score_search("https://uk.litime.com/"))
            if score != 0:
                performance = switch(num_search(key,"performance"))
                accessibility = switch(num_search(key,"accessibility"))
                practices = practices_search(key)
                seo = switch(num_search(key,"seo"))
                random_productName = product_search(name,"product_name")
                random_productLink = product_search(name,"product_link")
                random_productScore = switch(productScore_search(name))
                send_success_msg(name,url,score,performance,accessibility,practices,seo,random_productName,random_productLink,random_productScore)
            elif score == 0:
                send_fail_msg(name, url)

        elif key == 'https://jp.litime.com/':
            name = "LT_JP"
            url = key
            score = switch(score_search("https://jp.litime.com/"))
            if score != 0:
                performance = switch(num_search(key,"performance"))
                accessibility = switch(num_search(key,"accessibility"))
                practices = practices_search(key)
                seo = switch(num_search(key,"seo"))
                random_productName = product_search(name,"product_name")
                random_productLink = product_search(name,"product_link")
                random_productScore = switch(productScore_search(name))
                send_success_msg(name,url,score,performance,accessibility,practices,seo,random_productName,random_productLink,random_productScore)
            elif score == 0:
                send_fail_msg(name, url)

        elif key == 'https://au.litime.com/':
            name = "LT_AU"
            url = key
            score = switch(score_search("https://au.litime.com/"))
            if score != 0:
                performance = switch(num_search(key,"performance"))
                accessibility = switch(num_search(key,"accessibility"))
                practices = practices_search(key)
                seo = switch(num_search(key,"seo"))
                random_productName = product_search(name,"product_name")
                random_productLink = product_search(name,"product_link")
                random_productScore = switch(productScore_search(name))
                send_success_msg(name,url,score,performance,accessibility,practices,seo,random_productName,random_productLink,random_productScore)
            elif score == 0:
                send_fail_msg(name, url)

if __name__ == '__main__':
    # getInfo().clear_lighthouse_LTurl()
    # getInfo().write_baseUrl()
    # catch_LT_Allproduct()
    lightHouse()
    # check_all()