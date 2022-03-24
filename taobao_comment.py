import requests

# headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
#         'cookie': 'enc=K9w7lt0ACBfpcACk6ecuukxEkb1wNETI1lm3hKkz7NajxjsuF0PAGnF5N7JRRx5HCpSMCVO1qRy3Rapjl1genVBK2xHvD7IRt4/CXyb2F4s=; thw=cn; hng=CN|zh-CN|CNY|156; UM_distinctid=17eee6250f9159-01a9f45a7cc1c2-5b161d53-1ee2a3-17eee6250fa71d; t=6d3c2a8bbeb6d033449b4a59f392574b; sgcookie=E1002IuC8xy1zZ2reo60tyVIZBD7D0t/au5YFlQ5aSbvMmIbSx0XrKUt+GVknQwGtBrH/N44BX1DaCBhBuceKZqA71oF03usJd1svg4LwVzS3We4hZf3Cx3WTQ7RI6JaSdK9; tracknick=; cna=LAUHF+dphiwCAbenJmGtGvDq; cookie2=13b1550abd36d47f035e2b9de478bfc4; _tb_token_=1e678541d5b7; mt=ci=-1_1; xlly_s=1; _samesite_flag_=true; _m_h5_tk=8d63662a6825d1659a446efa7320c453_1646920743192; _m_h5_tk_enc=5d58d3d667dc14bc7147468d25047a21; x5sec=7b22726174656d616e616765723b32223a223133643037343836663830376133396562373938383363313964373530393539434f334f70354547454a3364775a37367634364b5a4367434d4a6e47756b453d227d; tfstk=cL6dBgGVDP4nfttO06FGPUas4DpRaQ3WrAYqelxgi2xTHuM-FsfdntUPYPxvueEO.; l=eBQsx5LlgaeZHqOaBO5Zourza77tNIRb81PzaNbMiInca6QFGFzz8NCnfB8vPdtjgtfvietrAS_2aRHv-VaLRFTjGO0qOC0eQD99-; isg=BOjoS9m5HqI5GDEo4PAW9OR4udb6EUwbfhmBKqIZkWNR_YlnSiBzq6Fz9ZUNSgTz'}
# url="https://rate.taobao.com/feedRateList.htm?auctionNumId=584618259981&userNumId=2710998898&currentPageNum=1&pageSize=20&rateType=&orderType=sort_weight&attribute=&sku=&hasSku=false&folded=0&ua=098#E1hvxQvUvbpvUQCkvvvvvjiWR2dy1j3vR2FyQj3mPmPvQjDCRLMyljr2RFcW6jlHPLsw29hvCvvvvvvUvpCWvfP6YC0nKd4AnsBSD76fdug7EcqOaXgBRbwZJbVYRfVth7QEfwoOdiTAVAllKbygndp6jUkUDC4AdcOdYE7reEkKf3Ax0fUtKfEIpf9Cvm9vvhCvvvvvvvvvpKGvvvHsvvCHwQvv9fQvvhxsvvmCi9vvBcWvvUVeuvhvmvvvpLqn05SZkvhvC9hvpyPygvvCvvOv9hCvvvvgvpvhvvCvp8OCvvpvvhHh&_ksTS=1646913845172_1241&callback=jsonp_tbcrate_reviews_list"
# r=requests.get(url,headers=headers)
# print(r.status_code)
# print(r.text)

import requests
import time
import json

t_param = time.time()
t_list = str(t_param).split('.')
_ksTS = t_list[0]+'_'+t_list[1][:3]
callback = str(int(t_list[1][:3])+ 1)

# ajax url
# url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=576746298719&sellerId=2328901391'
url = 'https://rate.tmall.com/list_detail_rate.htm?'

headers = {
    # cookie 值
    'cookie': 'enc=K9w7lt0ACBfpcACk6ecuukxEkb1wNETI1lm3hKkz7NajxjsuF0PAGnF5N7JRRx5HCpSMCVO1qRy3Rapjl1genVBK2xHvD7IRt4/CXyb2F4s=; thw=cn; hng=CN|zh-CN|CNY|156; UM_distinctid=17eee6250f9159-01a9f45a7cc1c2-5b161d53-1ee2a3-17eee6250fa71d; t=6d3c2a8bbeb6d033449b4a59f392574b; sgcookie=E1002IuC8xy1zZ2reo60tyVIZBD7D0t/au5YFlQ5aSbvMmIbSx0XrKUt+GVknQwGtBrH/N44BX1DaCBhBuceKZqA71oF03usJd1svg4LwVzS3We4hZf3Cx3WTQ7RI6JaSdK9; tracknick=; cna=LAUHF+dphiwCAbenJmGtGvDq; cookie2=13b1550abd36d47f035e2b9de478bfc4; _tb_token_=1e678541d5b7; mt=ci=-1_1; xlly_s=1; _samesite_flag_=true; _m_h5_tk=8d63662a6825d1659a446efa7320c453_1646920743192; _m_h5_tk_enc=5d58d3d667dc14bc7147468d25047a21; x5sec=7b22726174656d616e616765723b32223a223133643037343836663830376133396562373938383363313964373530393539434f334f70354547454a3364775a37367634364b5a4367434d4a6e47756b453d227d; tfstk=c5-1By2lP5V1DW04bdMEb1JoW5SGZMDRKXfeCEkDnYUYGip1iHrPNW955WsVH91..; l=eBQsx5LlgaeZHYW3BOfwhurza77thIRfguPzaNbMiOCP9I1y7rlcW6m6g7L2CnGVnsIWR3oQGZRzBkTUAy4ehEGfIqlBs2JZndLh.; isg=BP__iVrJoR-2oaYNMwV5eQdFjtOJ5FOGPVT2z5HM_a7zoB4imbVx13a24nBe-Cv-',
    # 返回
    "referer":"https://detail.tmall.com/item.htm?id=576746298719&rn=e82112c285c196431b1c91c448ccc1c8&abbucket=11&on_comment=1",
    # 模拟浏览器
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
}
# 请求参数
params = {
    # 商品ID
    "itemId": 576746298719,
    # 卖家ID
    "sellerId": 2328901391,
    # 评论页
    "currentPage":"1",
    # 时间戳
    "_ksTS":_ksTS,
    # json 回调
    "callback":callback,
}

res = requests.get(url,params=params,headers=headers)
print(res)
print("===="*100)
print(res.text)