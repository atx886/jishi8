import json
import re
import time

import requests
import random

from openpyxl import load_workbook

ta = []
tb = []
tc = []

file = '3.xlsx'
max_a = load_workbook(file).active.max_row
for a in range(0, max_a + 1):
    ta.append(0)
    tb.append(0)
    tc.append(0)


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


def rt():
    t = random.randint(1, 6)
    print('随即停止', t)
    time.sleep(t)


def gettk(phone):
    rt()
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
    # print(k)
    rs = re.findall('user_id\":(.+?),', k)
    # print(rs[0])
    rt()

    # 登录ck
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
    # print(x)
    s = re.findall('token\":\"(.+?)\"', x)
    # print(s[0])
    return s[0]


def qd(header):
    rt()
    url2 = 'https://v1.kykykb.cn/task/sign_in'
    r = requests.get(url=url2, headers=header)
    res = r.content.decode('utf-8')
    res = json.loads(res)
    print(res)


def dz(header):
    rt()
    url4 = 'https://v1.kykykb.cn/forum/section/hot?partner_id=xiaomi&platform_code=xiaomi&page=1&version=1.2.2&platform=android&timestamp=' + str(
        int(round(time.time() * 1000)))
    r = requests.post(url=url4, headers=header)
    li = r.text
    lis = re.findall('id\":(\d+\.?\d),\"title', li)
    print("当前长度")
    print(len(lis))
    m = 0
    for l in lis:
        rt()
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


def gettask(header):
    rt()
    ti = int(round(time.time() * 1000))
    url = 'https://v1.kykykb.cn/task/list?partner_id=xiaomi&platform_code=xiaomi&version=1.2.2&platform=android&timestamp=' + str(
        ti)
    r = requests.get(url=url, headers=header)
    res = r.content.decode('utf-8')
    res = json.loads(res)
    # print(r.content)
    # print(res)

    a = str(res)
    s = re.findall('state_desc\': \'(.+?)\'', a)
    a3 = s[0]
    a4 = s[2]
    a5 = s[4]
    # print(s)
    print(a3, a4, a5)
    return a3, a4, a5


def fb(header):
    rt()
    tim = str(int(round(time.time() * 1000)))
    url5 = 'https://v1.kykykb.cn/forum/topic/edit?partner_id=xiaomi&platform_code=xiaomi&category_id=687&resources=%5B%7B%22type%22%3A%22text%22%2C%22content%22%3A%222%22%7D%5D&title=1&version=1.2.2&platform=android&timestamp=' + tim
    url6 = 'https://v1.kykykb.cn/forum/topic/edit?partner_id=xiaomi&platform_code=xiaomi&category_id=3188&resources=%5B%7B%22type%22%3A%22text%22%2C%22content%22%3A%22%E6%9D%A5%E4%BA%86%22%7D%5D&title=&version=1.2.2&platform=android&timestamp=' + tim
    url7 = 'https://v1.kykykb.cn/forum/topic/edit?partner_id=xiaomi&platform_code=xiaomi&category_id=689&resources=%5B%7B%22type%22%3A%22text%22%2C%22content%22%3A%22%E5%BF%AB%E4%B9%90%22%7D%5D&title=&version=1.2.2&platform=android&timestamp=' + tim
    url8 = 'https://v1.kykykb.cn/forum/topic/edit?partner_id=xiaomi&platform_code=xiaomi&category_id=6735&resources=%5B%7B%22type%22%3A%22text%22%2C%22content%22%3A%22%E7%BE%8E%E5%A5%BD%22%7D%5D&title=&version=1.2.2&platform=android&timestamp=1' + tim
    ks = random.randint(5, 8)
    if ks == 5:
        requests.post(url=url5, headers=header)
    if ks == 6:
        requests.post(url=url6, headers=header)
    if ks == 7:
        requests.post(url=url7, headers=header)
    if ks == 8:
        requests.post(url=url8, headers=header)

    # res = r.content.decode('utf-8')
    # res = json.loads(res)
    # print(res)
    url7 = 'https://v1.kykykb.cn/task/receive?partner_id=xiaomi&platform_code=xiaomi&id=7&version=1.2.2&platform=android&timestamp=' + str(
        int(round(time.time() * 1000)))
    r = requests.get(url=url7, headers=header)
    # res = r.content.decode('utf-8')
    # res = json.loads(res)
    # print(res)


def lg(header, t):
    x = 0
    t = max_a - t
    a = gettask(header)
    if a[0] != "完成":
        qd(header)
    else:
        x += 1
        ta[t] = 1
    if a[1] != "完成":
        dz(header)
    else:
        x += 1
        tb[t] = 1
    if a[2] != "完成":
        fb(header)
    else:
        x += 1
        tc[t] = 1
    return x


def setheader(tk):
    header = {
        'Host': 'v1.kykykb.cn',
        'token': tk.replace('\\', ''),
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/3.14.9'

    }
    return header


def ww(k):
    b = 0
    for iq in k:
        if iq == 0:
            print(max_a - b)
        b += 1


errs = 0
errph = []
t = 0
while t < max_a:
    phone = writeexcle(t)
    max_b = lg(setheader(gettk(phone)), t)
    err = 0
    while max_b != 3:
        max_b = lg(setheader(gettk(phone)), t)
        err += 1
        if err > 3:
            print("失败一个")
            errph.append(phone)
            max_b = 3
    t += 1

print('失败数：')
for ers in errph:
    print(ers)

print("任务一完成")
a1 = 0
for i in ta:
    a1 += i
print(a1)
print("任务二完成")
a2 = 0
for i in tb:
    a2 += i
print(a2)
print("任务三完成")
a3 = 0
for i in tc:
    a3 += i
print(a3)

print("各任务失败序号")
print("任务一")
ww(ta)
print("任务二")
ww(tb)
print("任务三")
ww(tc)
