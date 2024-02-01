import requests
import hashlib
import base64
import hmac
from datetime import datetime
from base_Def import switch,score_search,data_time
from proxy import proxy_req

def gen_sign(timestamp, secret):
    # 拼接timestamp和secret
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    hmac_code = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()
    # 对结果进行base64处理
    sign = base64.b64encode(hmac_code).decode('utf-8')
    return sign

def time10():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    ts10 = str(timestamp).split('.')[0]
    return ts10

def send_success_msg(name,key,score,performance,accessibility,practices,seo,product_name,product_link,product_score):
    url = "https://open.feishu.cn/open-apis/bot/v2/hook/d8a6f124-7be7-48fe-b24c-d1eb08242833"
    data = {
        "timestamp": str(time10()),
        "sign": gen_sign(time10(), "4DtxiISKlOH1c5LSMBMXrb"),
        "msg_type": "interactive",
        "card": {
            "elements": [
                {
                    "extra": {
                        "tag": "button",
                        "text": {
                            "content": "查看官网",
                            "tag": "lark_md"
                        },
                        "type": "primary",
                        "multi_url": {
                            "url": key,
                            "android_url": "",
                            "ios_url": "",
                            "pc_url": ""
                        }
                    },
                    "tag": "div",
                    "text": {
                        "content": "**本次巡检的网站：" + name + "**\n**总分：" + str(score) + "**\n  -性能：" + str(
                            performance) + "\n  -无障碍：" + str(
                            accessibility) + "\n  -最佳做法：" + str(practices) + "\n  -SEO：" + str(
                            seo) + "\n时间：" + data_time() + "\n",
                        "tag": "lark_md"
                    }
                },
                {
                    "tag": "hr"
                },
                {
                    "extra": {
                        "tag": "button",
                        "text": {
                            "content": "查看商品",
                            "tag": "lark_md"
                        },
                        "type": "primary",
                        "multi_url": {
                            "url": product_link,
                            "android_url": "",
                            "ios_url": "",
                            "pc_url": ""
                        }
                    },
                    "tag": "div",
                    "text": {
                        "content": "**本次抽取的商品：" + product_name + "**\n总分：" + str(product_score),
                        "tag": "lark_md"
                    }
                }
            ],
            "header": {
                "template": "orange",
                "title": {
                    "content": "网站健康巡检",
                    "tag": "plain_text"
                }
            }
        }
    }
    headers = {"Content-Type": "application/json"}
    # rep = requests.post(url, json=data, headers=headers)
    rep = proxy_req("post",url,data,headers)
    print(rep.json())
    print(data)

def send_fail_msg(name,key):
    url = "https://open.feishu.cn/open-apis/bot/v2/hook/d8a6f124-7be7-48fe-b24c-d1eb08242833"
    data = {
        "timestamp": str(time10()),
        "sign": gen_sign(time10(), "4DtxiISKlOH1c5LSMBMXrb"),
        "msg_type": "interactive",
        "card": {
            "elements": [
                {
                    "extra": {
                        "tag": "button",
                        "text": {
                            "content": "查看官网",
                            "tag": "lark_md"
                        },
                        "type": "primary",
                        "multi_url": {
                            "url": key,
                            "android_url": "",
                            "ios_url": "",
                            "pc_url": ""
                        }
                    },
                    "tag": "div",
                    "text": {
                        "content": "**本次巡检的网站："+name+"**\n**总分：0**\n**备注：本次巡检执行失败，可能是网络原因导致，请自行查看官网**\n时间："+data_time()+"\n",
                        "tag": "lark_md"
                    }
                }
            ],
            "header": {
                "template": "red",
                "title": {
                    "content": "网站健康巡检",+
                    "tag": "plain_text"
                }
            }
        }
    }
    headers = {"Content-Type": "application/json"}
    # rep = requests.post(url, json=data, headers=headers)
    rep = proxy_req("post",url,data,headers)
    print(rep.json())
    print(data)
