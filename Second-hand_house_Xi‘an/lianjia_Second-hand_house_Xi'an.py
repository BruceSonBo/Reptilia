import requests
import parsel
import csv

# per = 101 # changan
# per =  22 # 高新六路
# per =  11 # 高新3小
# per =  12 # 高新4路
per =  10 # 高新3小

for page in range(1,per):
    print(f'\n======正在抓取第{page}页数据======')
    # 长安所有
    # url = f'https://xa.lianjia.com/ershoufang/changan7/pg{page}/'
    # 长安3室
    # url = f'https://xa.lianjia.com/ershoufang/changan7/pg{page}l3/'
    # 高新6路 3室
    # url = f'https://xa.lianjia.com/ershoufang/gaoxinliulu/pg{page}l3/'
    # 高新3小
    # url = f'https://xa.lianjia.com/ershoufang/gaoxinsanxiao/pg{page}l3/'

    # url = f'https://xa.lianjia.com/ershoufang/gaoxinsilu/pg{page}l3/'

    url = f'https://xa.lianjia.com/ershoufang/gaoxinyizhong/pg{page}l3/'




    # 确认url地址
    # url = 'https://xa.lianjia.com/ershoufang/changan7/l3'
    # url = 'https://xa.lianjia.com/ershoufang/changan7'

    # url = 'https://xa.lianjia.com/ershoufang'

    # 长安
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

    # 2、发送指定url地址的请求（html\js\css）
    response=requests.get(url=url, headers=headers)
    html_data = response.text     # 转换为文本
    # print(html_data)
    selector = parsel.Selector(html_data)
    lis = selector.css('.clear.LOGCLICKDATA')

    for li in lis:  # 二次提取  
        title = li.css('.title a::text').get()  # :: 属性选择器  # 房子标题
        address = li.css('.positionInfo a::text').getall() # 房子地址
        address = '_'.join(address)

        introduce = li.css('.houseInfo::text').get()  #介绍
        star = li.css('followInfo::text').get()       #关注度

        tags = li.css('tag span::text').getall()      # 标签（vr看房、房本年限。。）
        tags = ','.join(tags)

        totalPrice = li.css('.priceInfo .totalPrice span::text').get() + '万'  # 总价
        unitPrice = li.css('.unitPrice span::text').get()                      # 单价

        print(title, address, introduce, star, tags, totalPrice, unitPrice, sep='__')  # sep 分割打印

        with open ('链家-高新1中2手3室.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow([title, address, introduce, star, tags, totalPrice, unitPrice])