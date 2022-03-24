from datetime import date
import re
import json
import requests
def taobao(keyword,pages,select_type,date_):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        'cookie': 'enc=K9w7lt0ACBfpcACk6ecuukxEkb1wNETI1lm3hKkz7NajxjsuF0PAGnF5N7JRRx5HCpSMCVO1qRy3Rapjl1genVBK2xHvD7IRt4/CXyb2F4s=; thw=cn; hng=CN|zh-CN|CNY|156; UM_distinctid=17eee6250f9159-01a9f45a7cc1c2-5b161d53-1ee2a3-17eee6250fa71d; t=6d3c2a8bbeb6d033449b4a59f392574b; sgcookie=E1002IuC8xy1zZ2reo60tyVIZBD7D0t/au5YFlQ5aSbvMmIbSx0XrKUt+GVknQwGtBrH/N44BX1DaCBhBuceKZqA71oF03usJd1svg4LwVzS3We4hZf3Cx3WTQ7RI6JaSdK9; tracknick=; cna=LAUHF+dphiwCAbenJmGtGvDq; _m_h5_tk=9d8f0e554753127f3390ee16f518b2da_1646666499950; _m_h5_tk_enc=da89eab35a5af403377519bdcf904297; xlly_s=1; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; CNZZDATA1272960300=271800581-1644672166-https%3A%2F%2Fwww.taobao.com%2F|1646650248; cookie2=13b1550abd36d47f035e2b9de478bfc4; _tb_token_=1e678541d5b7; JSESSIONID=04F2CF65F15C8624A4609FC22CDB54DC; isg=BLm5VBTx_44M9qAb-WdXNy2HyCWTxq14x9ZwudvuNeBfYtn0Ixa9SCew5GaUQUWw; l=eBQsx5LlgaeZH6nEBOfanurza77OSIRYYuPzaNbMiOCPO55B5BghW6mrAxT6C3GVh6X2R3oQGZRyBeYBqQAonxv92j-la_kmn; tfstk=cJ_fBwcHAxDf0JZZusNzuRbaaBYOw_He1fpVGGypGhTWEp10-2JIF6gqCFR9N'}
    url = 'https://s.taobao.com/search?q={}&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id={}&ie=utf8&sort={}'.format(keyword, date_, selections[select_type])
    titles=[];item_ids=[];prices=[];locations=[];sales=[];seller_ids=[];store_names=[]
    for i in range(pages):
        r = requests.get(url+'&s={}'.format(str(i*44)),headers=headers,)
        print(r.status_code)

        print(r.text)
        print('*'*100)
        data = re.search(r'g_page_config = (.+);',r.text)#捕捉json字符串

        print(data)

        data = json.loads(data.group(1))#json转dict
        for auction in data['mods']['itemlist']['data']['auctions']:
            titles.append(auction['raw_title'])#商品名
            item_ids.append(auction['nid'])#商品id
            prices.append(auction['view_price'])#价格
            locations.append(auction['item_loc'])#货源
            sales.append(auction['view_sales'])#卖出数量
            seller_ids.append(auction['user_id']) #商家id
            store_names.append(auction['nick'])#店铺名

        #正则实现
        '''titles.extend(re.findall(r'"raw_title":"(.+?)"',r.text,re.I)) 
        item_ids.extend( re.findall(r'"nid":"(.+?)"',r.text,re.I))
        prices.extend(re.findall(r'"view_price":"([^"]+)"',r.text,re.I)) 
        locations.extend(re.findall(r'"item_loc":"([^"]+)"',r.text,re.I))
        sales.extend(re.findall(r'"view_sales":"([^"]+)"',r.text,re.I)) 
        seller_ids.extend(re.findall(r'"user_id":"([^"]+)"',r.text,re.I)) 
        store_names.extend(re.findall(r'"nick":"([^"]+)"',r.text,re.I)) '''
    #单纯打印出来看
    print (len(titles),len(item_ids),len(prices),len(locations),len(sales),len(seller_ids),len(store_names))
    print(titles)
    print(item_ids)
    print(prices)
    print(locations)
    print(sales)
    print(seller_ids)
    print(store_names)


selections = {'0':'default',
              '1':'renqi-desc',
              '2':'sale-desc'}
keyword = input('输入商品名\n')
pages = int(input('爬多少页\n'))
date_ =  'staobaoz_' + str(date.today()).replace('-','')
if input('yes/no  for 改排序方式,默认综合')=='yes':
    select_type = input('输入1按人气，输入2按销量')
else:
    select_type = '0'
taobao(keyword,pages,select_type,date_)