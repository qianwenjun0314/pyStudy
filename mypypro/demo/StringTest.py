from urllib import parse
from urllib import request

url1 = 'https://activity.m.duiba.com.cn/crecord/record'
url2 = 'http://activity.m.duiba.com.cn/customShare/share?id=1288&redirect='


url3 = 'http://home.m.duiba.com.cn/test/generateSign?appKey=jlg88lyxz7siqtmr&uid=1&credits=1000000&redirect=http://activity.m.duiba.com.cn/hdtool/index?id=2956561'

url4_data = 'http://activity.m.duiba.com.cn/autoLogin/autologin?redirect=http%3A%2F%2Factivity.m.duiba.com.cn%2Fhdtool%2Findex%3Fid%3D2956561&uid=1&credits=1000000&sign=3915137d74b665793fc974d0e06daf69&appKey=jlg88lyxz7siqtmr&timestamp=1548830527332&'
#编码
url1_data = parse.quote(url1)
print('免登的兑换记录链接为：http://activity.m.duiba.com.cn/customShare/share?id=1288&redirect=' + url1_data)
url3_data = parse.quote(url3)
print('url3的编码结果为：' + url3_data)
#解码
url4 = parse.unquote(url4_data)
print('url4解码结果为：' + url4)
