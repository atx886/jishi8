import json
import re
import time

import requests
from openpyxl import load_workbook
import urllib
import urllib.parse
import urllib.request

file = '3.xlsx'
max_a = load_workbook(file).active.max_row


def writeexcle(t):
    wb = load_workbook(file)
    sheet = wb.active
    max_row = sheet.max_row - t

    row_max = 'a' + str(max_row)
    print(sheet)

    if max_row > 0:
        a = sheet[row_max].value
        print(a)
        return a
    else:
        print("空了")
        return None


def getck(phone):
    url = 'https://www.chaojijishi.com/api/v3/thirdPartyCheckRedirect'

    header1 = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; M2006J10C Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36'
    }

    data = {
        "mobile": str(phone),
        "password": "123456",
        "type": "zl_jiudou"
    }

    r = requests.post(url=url, headers=header1, data=data)

    k = r.text
    print(k)
    rs = re.findall('user_id\":(.+?),', k)
    print(rs[0])

    # 登录ck
    time.sleep(2)
    url1 = 'https://v1.kykykb.cn/third_login?partner_id=xiaomi&platform_code=xiaomi&third_username=' + str(
        phone) + '&third_user_id=' + str(rs[
                                             0]) + '&device_token=E65EDB645421EA65F709E6975338483AF55F2F76&device_type=xiaomi&version=1.2.2&platform=android&third_type=jiudou&timestamp=' + str(
        int(round(time.time() * 1000)))

    header2 = {
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/3.14.9'
    }

    r = requests.post(url=url1, headers=header2)
    x = r.text
    print(x)
    s = re.findall('token\":\"(.+?)\"', x)
    print(s[0])
    return s[0]


def rw(phone):
    tk = getck(phone)
    ti = int(round(time.time() * 1000))
    url = 'https://v1.kykykb.cn/task/list?partner_id=xiaomi&platform_code=xiaomi&version=1.2.2&platform=android&timestamp=' + str(
        ti)
    # tk = 'bPfmSWNULUfPf4FAL7tYRwtn2KkKEIz5NBxfRqnOF3aExrELAqbpNrIpEAOc4NTSy6GJFsPpW73zcenDexXnMoMj+cwprtk5FNQC5CAoSC8='
    header = {
        'Host': 'v1.kykykb.cn',
        'token': tk.replace('\\', ''),
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/3.14.9'

    }

    r = requests.get(url=url, headers=header)
    res = r.content.decode('utf-8')
    res = json.loads(res)
    # print(r.content)
    print(res)

    url1 = 'https://v1.kykykb.cn/task/sign_list'
    r = requests.get(url=url1, headers=header)
    res = r.content.decode('utf-8')
    res = json.loads(res)
    print(res)
    # 签到
    url2 = 'https://v1.kykykb.cn/task/sign_in'
    r = requests.get(url=url2, headers=header)
    res = r.content.decode('utf-8')
    res = json.loads(res)
    print(res)

    # 获取点赞列表
    url4 = 'https://v1.kykykb.cn/forum/section/hot?partner_id=xiaomi&platform_code=xiaomi&page=1&version=1.2.2&platform=android&timestamp=' + str(
        int(round(time.time() * 1000)))
    r = requests.post(url=url4, headers=header)
    li = r.text
    lis = re.findall('id\":(\d+\.?\d),\"title', li)
    if len(lis) < 4:
        r = requests.post(url=url4, headers=header)
        li = r.text
        lis = re.findall('id\":(\d+\.?\d),\"title', li)
    # 点赞
    m = 0
    for l in lis:
        time.sleep(0.7)
        url3 = 'https://v1.kykykb.cn/forum/topic/agree?topic_id=' + l
        r = requests.post(url=url3, headers=header)
        res = r.content.decode('utf-8')
        res = json.loads(res)
        print(res)
        m += 1
        if m >= 5:
            break
    url6 = 'https://v1.kykykb.cn/task/receive?partner_id=xiaomi&platform_code=xiaomi&id=3&version=1.2.2&platform=android&timestamp=' + str(
        int(round(time.time() * 1000)))
    r = requests.get(url=url6, headers=header)
    res = r.content.decode('utf-8')
    res = json.loads(res)
    print(res)

    # 发表
    url5 = 'https://v1.kykykb.cn/forum/topic/edit?partner_id=xiaomi&platform_code=xiaomi&category_id=687&resources=%5B%7B%22type%22%3A%22text%22%2C%22content%22%3A%222%22%7D%5D&title=1&version=1.2.2&platform=android&timestamp=1653127568442'
    # url5 = 'https://v1.kykykb.cn/forum/topic/edit?partner_id=xiaomi&platform_code=xiaomi&category_id=687&resources=%5B%7B%22type%22%3A%22text%22%2C%22content%22%3A%22%F0%9F%98%84%22%7D%5D&title=%E5%BF%AB%E4%B9%90&version=1.2.2&platform=android&timestamp=1653127472119'
    tk = 'NvZ0hWVXpQBe/t/pNoqIimu+tMNgweb3'
    h = {
        'X-User-Token': tk
    }
    r = requests.get('https://v2.jinrishici.com/sentence', headers=h)
    # res = r.content.decode('utf-8')
    # res = json.loads(res)
    res = r.text
    title = re.findall('title\":\"(.+?)\"', res)
    content = re.findall('content\":\"(.+?)\"', res)
    # print(res)
    print(title[0])
    print(content[0])
    text = f'[{{"type":"text","content":"{content[0][1]}"}}]&title={title[0][1]}'
    # print(text)
    qt = urllib.parse.quote(text)
    print(qt)
    # url5 = 'https://v1.kykykb.cn/forum/topic/edit?partner_id=xiaomi&platform_code=xiaomi&category_id=687&resources=' + qt + '&version=1.2.2&platform=android&timestamp=' + str(
    #     int(round(time.time() * 1000)))
    # print(url5)
    r = requests.post(url=url5, headers=header)
    res = r.content.decode('utf-8')
    res = json.loads(res)
    print(res)
    url7 = 'https://v1.kykykb.cn/task/receive?partner_id=xiaomi&platform_code=xiaomi&id=7&version=1.2.2&platform=android&timestamp=' + str(
        int(round(time.time() * 1000)))
    r = requests.get(url=url7, headers=header)
    res = r.content.decode('utf-8')
    res = json.loads(res)
    print(res)



# rw(17000655027)

a = max_a
c = 0
chengong = 0
while a > 0:
    try:
        time.sleep(2)
        phone = writeexcle(c)
        rw(phone)
        chengong += 1
        c += 1
        a -= 1
    except Exception as e:
        print('失败')
        a -= 1
        c += 1

print(chengong)
