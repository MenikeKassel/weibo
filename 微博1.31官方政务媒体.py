# -*- coding: utf-8 -*-
# @Time : 2022/1/31 14:51
# @Author : menike
# @File : 微博1.31官方政务媒体.py
# @Software: PyCharm

import time
import requests
import json
import urllib3
import csv

urllib3.disable_warnings()


def get_uid(custom):
    '''
    获取官方媒体的uid
    '''
    url = f"https://weibo.com/ajax/profile/info?custom={custom}"
    headers = {
        'accept': 'application/json,text/plain,*/*',
        'cookie': 'SINAGLOBAL=4410093549687.555.1633845372069;UOR=,,login.sina.com.cn;ALF=1674820413;SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWFXpX3EM7.P0REsQ7Uh6TY5JpX5K-hUgL.FoMp1K201hB7SKz2dJLoIp-LxKML1h-L12eLxK-LB-qL1h-ceK.t;SCF=Av1gbWwFv1LduqTrF6XN7cUpIIlstIA_sgGytKXLXj-FUbO0b9jscMgOCeJMsey-tFzFegn2ovE9EwoYyZN15dI.;SUB=_2A25M88NDDeRhGeFP4lMS-CrMzj6IHXVviLOLrDV8PUJbmtCOLWv9kW9NQOuIwZtRvDL_QtdN2VHHPNo1O1zXB6LY;SSOLoginState=1643623187;XSRF-TOKEN=hLpFg_QZSXuSOpkYXR3Zz1f3;_s_tentry=weibo.com;Apache=7649664796407.238.1643623195061;ULV=1643623195161:19:10:2:7649664796407.238.1643623195061:1643613600327;WBPSESS=_X_Um1n8CY35FhNEaqmYqLXPcYqAf2-mHZhMYxSHB9Xtk8qt9JG9ZHqOxsXz8TMZwhmZPg20Ii2XF7wZtqiC6ZHhEbsJgLFDU-TG5QU26igISjJr2BAMvSGWn3OyARcmehtx-i28k34JtR38gMfiOA==',
        'referer': f'https://weibo.com/{custom}',
        'user-agent': 'Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/97.0.4692.71Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    try:
        resp = requests.get(url, headers=headers, verify=False)
        # print(r.text)
    except requests.HTTPError as e:
        print(e)
        print("HTTPError")
    except requests.RequestException as e:
        print(e)
    except:
        print("Unknown Error !")
    html = json.loads(resp.text)
    try:
        description = html['data']["user"]["description"]  # 官方描述
        followers_count = html['data']["user"]["followers_count"]  # 粉丝数量
        id = html['data']["user"]["id"]  # 粉丝数量
        print("官方描述:" + description)
        print("粉丝数量:" + str(followers_count))
        print("id:" + str(id))
    except:
        print("未获取到媒体信息")
    return uid


def get_news_id(uid, page):
    '''
    获取当前新闻集合页面的所有新闻id
    :param uid:新闻的uid
    :param page:新闻集合页面
    :return:
    '''
    ids = []

    url = f"https://weibo.com/ajax/statuses/mymblog?uid={uid}&page={page}&feature=0"
    headers = {
        'accept': 'application/json,text/plain,*/*',
        'cookie': 'SINAGLOBAL=4410093549687.555.1633845372069;UOR=,,login.sina.com.cn;ALF=1674820413;SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWFXpX3EM7.P0REsQ7Uh6TY5JpX5K-hUgL.FoMp1K201hB7SKz2dJLoIp-LxKML1h-L12eLxK-LB-qL1h-ceK.t;SCF=Av1gbWwFv1LduqTrF6XN7cUpIIlstIA_sgGytKXLXj-FUbO0b9jscMgOCeJMsey-tFzFegn2ovE9EwoYyZN15dI.;SUB=_2A25M88NDDeRhGeFP4lMS-CrMzj6IHXVviLOLrDV8PUJbmtCOLWv9kW9NQOuIwZtRvDL_QtdN2VHHPNo1O1zXB6LY;SSOLoginState=1643623187;XSRF-TOKEN=hLpFg_QZSXuSOpkYXR3Zz1f3;_s_tentry=weibo.com;Apache=7649664796407.238.1643623195061;ULV=1643623195161:19:10:2:7649664796407.238.1643623195061:1643613600327;WBPSESS=_X_Um1n8CY35FhNEaqmYqLXPcYqAf2-mHZhMYxSHB9Xtk8qt9JG9ZHqOxsXz8TMZwhmZPg20Ii2XF7wZtqiC6ZHhEbsJgLFDU-TG5QU26igISjJr2BAMvSGWn3OyARcmehtx-i28k34JtR38gMfiOA==',
        'referer': f'https://weibo.com/{custom}',
        'user-agent': 'Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/97.0.4692.71Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    try:
        resp = requests.get(url, headers=headers, verify=False)
        # print(r.text)
    except requests.HTTPError as e:
        print(e)
        print("HTTPError")
    except requests.RequestException as e:
        print(e)
    except:
        print("Unknown Error !")
    html = json.loads(resp.text)
    for i in range(20):
        try:
            created_at = html['data']["list"][i]['created_at']  # 官方描述
            id = html['data']["list"][i]['id']  # 粉丝数量
            ids.append(id)
            text_raw = html['data']["list"][i]['text_raw']  # 粉丝数量
            attitudes_count = html['data']["list"][i]['attitudes_count']  # 博客点赞数
            comments_count = html['data']["list"][i]['comments_count']  # 博客评论数
            reposts_count = html['data']["list"][i]['reposts_count']  # 博客转发数
            print("发博时间:" + created_at)
            print("新闻id:" + str(id))
            print("微博内容:" + str(text_raw))
            print("博客点赞数:" + str(attitudes_count))
            print("博客评论数:" + str(comments_count))
            print("博客转发数:" + str(reposts_count))
            dit = {
                '发博时间': created_at,
                '新闻id': id,
                '微博内容': text_raw,
                '博客点赞数': attitudes_count,
                '博客评论数': comments_count,
                '博客转发数': reposts_count
            }
            # 把拆分的数据整合进一个新的字典
            csv__.writerow(dit)
        except:
            print("未获取到媒体信息")
    f.close()
    return ids


def get_comment(url):
    '''
    获取评论信息
    '''
    headers = {
        'accept': 'application/json,text/plain,*/*',
        'cookie': 'SINAGLOBAL=4410093549687.555.1633845372069;UOR=,,login.sina.com.cn;ALF=1674820413;SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWFXpX3EM7.P0REsQ7Uh6TY5JpX5K-hUgL.FoMp1K201hB7SKz2dJLoIp-LxKML1h-L12eLxK-LB-qL1h-ceK.t;SCF=Av1gbWwFv1LduqTrF6XN7cUpIIlstIA_sgGytKXLXj-FUbO0b9jscMgOCeJMsey-tFzFegn2ovE9EwoYyZN15dI.;SUB=_2A25M88NDDeRhGeFP4lMS-CrMzj6IHXVviLOLrDV8PUJbmtCOLWv9kW9NQOuIwZtRvDL_QtdN2VHHPNo1O1zXB6LY;SSOLoginState=1643623187;XSRF-TOKEN=hLpFg_QZSXuSOpkYXR3Zz1f3;_s_tentry=weibo.com;Apache=7649664796407.238.1643623195061;ULV=1643623195161:19:10:2:7649664796407.238.1643623195061:1643613600327;WBPSESS=_X_Um1n8CY35FhNEaqmYqLXPcYqAf2-mHZhMYxSHB9Xtk8qt9JG9ZHqOxsXz8TMZwhmZPg20Ii2XF7wZtqiC6ZHhEbsJgLFDU-TG5QU26igISjJr2BAMvSGWn3OyARcmehtx-i28k34JtR38gMfiOA==',
        'user-agent': 'Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/97.0.4692.71Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    try:
        resp = requests.get(url, headers=headers, verify=False)
        # print(r.text)
    except requests.HTTPError as e:
        print(e)
        print("HTTPError")
    except requests.RequestException as e:
        print(e)
    except:
        print("Unknown Error !")
    html = json.loads(resp.text)
    try:
        max_id = html["max_id"]
    except:
        print("未定位到max_id")
    try:
        for i in range(19):
            created_at = html['data'][i]["created_at"]  # 评论发表时间
            comment_content = html['data'][i]["text_raw"]  # 评论文本内容
            comment_like = html['data'][i]["like_counts"]  # 点赞数
            comment_reply = html['data'][i]["total_number"]  # 回复数
            if comment_content != []:
                print(comment_content)
            dit = {
                '评论发表时间': created_at,
                '评论内容': comment_content,
                '点赞数': comment_like,
                '回复数': comment_reply
            }
            # 把拆分的数据整合进一个新的字典
            csv__.writerow(dit)
    except:
        print('新闻id' + str(id) + "获取失败")
    return max_id


if __name__ == '__main__':
    custom = "rmrb"  # 官方政务媒体名称
    uid = get_uid(custom)
    f = open(
        f'./data/{custom}.csv',
        mode='a',
        encoding='utf-8-sig',
        newline='')
    # 创建一个csv文件，mode=a表示对文件只能写入，encoding是内容文字，newline避免有换行字符等产生
    csv__ = csv.DictWriter(
        f,
        fieldnames=(
            '发博时间',
            '新闻id',
            '微博内容',
            '博客点赞数',
            '博客评论数',
            '博客转发数'
        )
    )
    # f是创建的csv文件，fieldnames表示列名
    csv__.writeheader()
    for page in range(1, 2):
        time.sleep(10)
        ids = get_news_id(uid, page)
        # print(len(ids))
        for id in ids:  # 当前页面每个新闻id
            url = f"https://weibo.com/ajax/statuses/buildComments?is_reload=1&id={id}&is_show_bulletin=2&is_mix=0&count=10&uid={uid}"
            f2 = open(
                f'./data/{id}.csv',
                mode='a',
                encoding='utf-8-sig',
                newline='')
            # 创建一个csv文件，mode=a表示对文件只能写入，encoding是内容文字，newline避免有换行字符等产生
            csv__ = csv.DictWriter(
                f2,
                fieldnames=(
                    '评论发表时间',
                    '评论内容',
                    '点赞数',
                    '回复数'
                )
            )
            # f是创建的csv文件，fieldnames表示列名
            csv__.writeheader()
            for i in range(10):
                time.sleep(10)
                max_id = get_comment(url)
                # print(max_id)
                url = f"https://weibo.com/ajax/statuses/buildComments?flow=0&is_reload=1&id={id}&is_show_bulletin=2&is_mix=0&max_id={max_id}&count=20&uid={uid}"
