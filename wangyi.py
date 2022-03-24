import json
import re
import requests

#构造基本headers
headers = {
    # # cookie 值
    # 'cookie': 'enc=K9w7lt0ACBfpcACk6ecuukxEkb1wNETI1lm3hKkz7NajxjsuF0PAGnF5N7JRRx5HCpSMCVO1qRy3Rapjl1genVBK2xHvD7IRt4/CXyb2F4s=; thw=cn; hng=CN|zh-CN|CNY|156; UM_distinctid=17eee6250f9159-01a9f45a7cc1c2-5b161d53-1ee2a3-17eee6250fa71d; t=6d3c2a8bbeb6d033449b4a59f392574b; sgcookie=E1002IuC8xy1zZ2reo60tyVIZBD7D0t/au5YFlQ5aSbvMmIbSx0XrKUt+GVknQwGtBrH/N44BX1DaCBhBuceKZqA71oF03usJd1svg4LwVzS3We4hZf3Cx3WTQ7RI6JaSdK9; tracknick=; cna=LAUHF+dphiwCAbenJmGtGvDq; cookie2=13b1550abd36d47f035e2b9de478bfc4; _tb_token_=1e678541d5b7; mt=ci=-1_1; xlly_s=1; _samesite_flag_=true; _m_h5_tk=8d63662a6825d1659a446efa7320c453_1646920743192; _m_h5_tk_enc=5d58d3d667dc14bc7147468d25047a21; x5sec=7b22726174656d616e616765723b32223a223133643037343836663830376133396562373938383363313964373530393539434f334f70354547454a3364775a37367634364b5a4367434d4a6e47756b453d227d; tfstk=c5-1By2lP5V1DW04bdMEb1JoW5SGZMDRKXfeCEkDnYUYGip1iHrPNW955WsVH91..; l=eBQsx5LlgaeZHYW3BOfwhurza77thIRfguPzaNbMiOCP9I1y7rlcW6m6g7L2CnGVnsIWR3oQGZRzBkTUAy4ehEGfIqlBs2JZndLh.; isg=BP__iVrJoR-2oaYNMwV5eQdFjtOJ5FOGPVT2z5HM_a7zoB4imbVx13a24nBe-Cv-',
    # # 返回
    "referer": "https://detail.tmall.com/item.htm?id=576746298719&rn=e82112c285c196431b1c91c448ccc1c8&abbucket=11&on_comment=1",
    # 模拟浏览器
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
}

def get_playlists(pages,order,cat):
    """
    获取当前页面歌单id
    :param pages:
    :param order:
    :param cat:
    :return:
    """
    playlist_ids=[]

    for page in range(pages):
        url='http://music.163.com/discover/playlist/?order={}&cat={}&limit=35&offset={}'.format(order,cat,str(page*35))
        print(url)
        r=requests.get(url,headers=headers)
        print("*"*100)
        # print(r.text)
        playlist_ids.extend(re.findall(r'playlist\?id=(\d+?)" class="msk"',r.text))

    return playlist_ids

def get_songs(playlist_id='778462085'):
    """
    获取歌单内歌曲id,名称等信息
    :param playlist_id:
    :return:
    """
    r = requests.get('http://music.163.com/playlist?id={}'.format(playlist_id),headers=headers)
    song_ids = re.findall(r'song\?id=(\d+?)".+?</a>',r.text)#歌id列表
    song_titles = re.findall(r'song\?id=\d+?">(.+?)</a>',r.text)#歌名列表
    list_title = re.search(r'>(.+?) - 歌单 - 网易云音乐',r.text).group(1)#歌单名
    list_url = 'http://music.163.com/playlist?id='+playlist_id #歌单链接
    return [song_ids, song_titles, list_title, list_url]#一次性返回这些信息给评论爬取器

# list=get_playlists(4,"hot","韩语")
# print(list)
# print(get_songs())
# id='721243'
# r = requests.get('http://music.163.com/song?id={}'.format(id),headers=headers)
# print(r.text)
data={
    "params": "Lm33pTra8neX5LF9XEMx2VaoILLcrSQUtyppKE1EgSxtwJdyeEyLAPPP4yNFXso17esHYoJ9T9Yx/kNqT9hyg8xJMIQh8MpFU7kjsRlcR+PbbnTFQ1bpqlk8mpGbU1qQuLskIRmQY4l4JQGMlPOY6jSFQVsP8rfI7nfRkZbdb5LDMU4gyAVrBUsZDQ/u2mGZxTQrKCnezb3Csc9Y5abgQeYYYFUrXxPg2N6gNeKHiuzf3J3QXJH2tYykxgjaySdRYuj2gTaSsBMDdIK5YWCEXygb1qqj+CN4IdUr/D+ffvE=",
    "encSecKey": "51e2f7445bacb87c58835301d0552ee85ac94cc185058d87f8581a01e50187f22d319ebd6d656dcf2466519e128906d8d3c29200014c34c23c0c62ecf5c5083cf4a61b358960a39c1cfb953cfbc2e257e197e83567331b753870d79dd862ffd71fede6d053f42027d5f7bc67ee78b69db45c7793aa24d80d6016450c2dfe7439"
}
url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

r=requests.post(url,data=data, headers=headers)
# print(r.text)
# dirs=json.loads(r.text)
print("*"*1000)
# list=re.findall(r"\"content\":\"(.+?)\",",r.text)
# print(list)
comments_json=json.loads(r.text)
comments=comments_json['data']['comments']
with open('comments1.txt',"w",encoding='utf-8') as f:
    for each in comments:
        f.write(each['user']['nickname']+':\n\n')
        f.write(each['content']+'\n')
        f.write("------------------------\n")
# print(dirs)
