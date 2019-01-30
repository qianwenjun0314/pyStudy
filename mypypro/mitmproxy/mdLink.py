from mitmproxy import ctx, http
import json
import mitmproxy.http

class Modify:
            
    def request(self, flow):
        if flow.request.url.startswith("http://activity-1.m.duiba.com.cn/customActivity/bookcode/doJoin"):
            ctx.log.info("modify request form")
            if flow.request.urlencoded_form:
                flow.request.urlencoded_form["code"] = "11111"
            else:
                flow.request.urlencoded_form = [
                    ("activityId", "20727"),("nick","name")
                ]
           

   
        # if flow.request.url.startswith("http://www.duiba.com.cn/autoLogin/autologin?uid=59725841&credits=31&appKey=4RjniQxgtG2cTVQEEz82g8kbgVvQ"):
        #     ctx.log.info("replace url-ios-8")
  
        if flow.request.url.startswith("http://www.duiba.com.cn/autoLogin/autologin?uid=59737157&credits=30&appKey=4RjniQxgtG2cTVQEEz82g8kbgVvQ"):
            ctx.log.info("replace url-Android")
            # with open('link.json','rb') as l1:
            #     res = json.load(l1)
            #     # ctx.log.info(json.load(l1))
            # flow.request.url = json.dumps(res)
            flow.request.url = 'http://www.duiba.com.cn/autoLogin/autologin?uid=30404300&credits=0&appKey=PFw6coiXGY3cZFQDkLRqGThTy6a&timestamp=1545902268000&dcustom=avatar%3Dhttp%253A%252F%252Ft-static2.ivwen.com%252Fusers%252F30404300%252F95bd62c1840c46fca8e98c6d358bb064.jpg%253Fmeipian%252Fbucket%252Fivwen%252Fkey%252FdXNlcnMvMzA0MDQzMDAvOTViZDYyYzE4NDBjNDZmY2E4ZTk4YzZkMzU4YmIwNjQuanBn%252Fsign%252F97d0da5094596dc8c0527091ba2c58f5%26nickname%3D%25E9%2592%25B1%25E9%259B%25AF%25E5%2590%259B%26wechat_bind%3D0%26phone_bind%3D0&redirect=https%3A%2F%2Factivity.m.duiba.com.cn%2Fhdtool%2Findex%3Fid%3D3284948%26dpm%3D52618.41.1.0%26dcm%3D216.296.255.0%26appKey%3DPFw6coiXGY3cZFQDkLRqGThTy6a&sign=26b26e7c22f5a1bac0a4988d774ebc0f'

        if flow.request.url.startswith("http://www.duiba.com.cn/autoLogin/autologin?uid=59738749&credits=30&appKey=4RjniQxgtG2cTVQEEz82g8kbgVvQ"):
            ctx.log.info("replace url-ios-5s") 
            flow.request.url = 'http://www.duiba.com.cn/autoLogin/autologin?uid=30404300&credits=0&appKey=PFw6coiXGY3cZFQDkLRqGThTy6a&timestamp=1545890543000&dcustom=avatar%3Dhttp%253A%252F%252Ft-static2.ivwen.com%252Fusers%252F30404300%252F95bd62c1840c46fca8e98c6d358bb064.jpg%253Fmeipian%252Fbucket%252Fivwen%252Fkey%252FdXNlcnMvMzA0MDQzMDAvOTViZDYyYzE4NDBjNDZmY2E4ZTk4YzZkMzU4YmIwNjQuanBn%252Fsign%252F97d0da5094596dc8c0527091ba2c58f5%26nickname%3D%25E9%2592%25B1%25E9%259B%25AF%25E5%2590%259B%26wechat_bind%3D0%26phone_bind%3D0&redirect=https%3A%2F%2Factivity.m.duiba.com.cn%2Fhdtool%2Findex%3Fid%3D3284948%26dpm%3D52618.41.1.0%26dcm%3D216.296.255.0%26appKey%3DPFw6coiXGY3cZFQDkLRqGThTy6a&sign=0c0201d0664ec5882785c9ed7091b8e6'
         

        if flow.request.url.startswith("http://activity.m.duiba.com.cn/customShare/share?id=2353"):
            flow.request.url = "http://activity.m.duibatest.com.cn/customShare/share?id=671&activityId=16"
            ctx.log.info("修改链接")
            
        if flow.request.url == "http://shouji.360.cn/360cleanmsg/index.html":
            flow.request.url = "https://activity.m.duiba.com.cn/ngame/index?id=3041539&appKey=EjjWosTrA1zdf1noUTSVv2EJh1s&open4share=tongdun"
            ctx.log.info("修改链接")

    def response(self, flow):
        # 修改抽奖结果，为处理中
        if flow.request.url.startswith("https://activity.m.duibatest.com.cn/collectRule/getOrderStatus11"):
            # flow.response.set_text('{"result":0,"success":true,"message":"处理中。。。"}')
            with open('getOrderStatus.json','rb') as f:
                res = json.load(f)
            flow.response.set_text(json.dumps(res))
            ctx.log.info("modify order status")
            
        if flow.request.url.startswith("http://activity.m.duiba.com.cn/hdtool/ajaxElementss"):
            flow.response.set_text('{"showchat":true,"throughCurrent":"1","isPopup":false,"throughMode":1,"jsTest":"//yun.duiba.com.cn/h5/showCouponPrize/4.0.0/index_201710191434.js","rule":"规则规则","type":"hdtool","throughNum":1,"throughCurrentStep":24,"success":true,"cssTest":"//yun.duiba.com.cn/h5/showCouponPrize/4.0.0/index_201710191440.css","options":[{"hidden":true,"id":264806,"logo":"//yun.duiba.com.cn/upload/uP99F1462438316972.png","name":"谢谢参与","prizeType":"thanks"},{"hidden":true,"id":264913,"logo":"//yun.duiba.com.cn/upload/uP99F1462438316972.png","name":"谢谢参与2","prizeType":"thanks"}],"element":{"freeEmpty":false,"freeLimit":0,"isCreditsTypeOpen":false,"myCredits":"289892","needCredits":"5","status":4}}')
        
        #修改签到返回-为签到失败
        if flow.request.url.startswith("https://activity.m.duiba.com.cn/signactivity/doSign"):
            with open('signError.json','rb') as q1:
                res = json.load(q1)
            flow.response.set_text(json.dumps(res))
            ctx.log.info("modify sign signError success")

        # 修改美餐实物
        if flow.request.url.startswith("https://restaurant.dui88.com/dingding/daily/food?startDay=2018-12-05&endDay=2018-12-05"):
            # flow.response.set_text('{"success":true,"message":null,"data":{"days":[{"dfDay":"2018-11-20","noon":{"orderId":264911,"foodId":2860,"foodName":"椒盐带鱼","foodDesc":"番茄炒蛋\t宫保鸡丁\t三鲜日本豆腐","groupId":6,"groupName":"05","dfDayMoment":1,"status":2},"night":{"orderId":267528,"foodId":2882,"foodName":"经典凯撒沙拉","foodDesc":null,"groupId":6,"groupName":"05","dfDayMoment":2,"status":1}}],"full":true}}')
            # ctx.log.info("modify food success")
            with open('food.json','rb') as f5:
                res = json.load(f5)
            flow.response.set_text(json.dumps(res))
            ctx.log.info("modify food success")

        if flow.request.url.startswith("http://activity.m.duiba.com.cn/ngame/new/submitss"):
            flow.response = http.HTTPResponse.make(404)
            ctx.log.info("modify status code")

        # 契约签到轮播
        if flow.request.url.startswith("http://activity.m.duiba.com.cn/sign/contract/getRewardTodayLimit200999"):
            with open('getRewardTodayLimit200.json','rb') as f:
                res = json.load(f)
            flow.response.set_text(json.dumps(res))
            
        # 契约签到主页
        if flow.request.url.startswith('http://activity.m.duibatest.com.cn/sign/contract/getHomeInfo?activityId=11'):
            with open('getHomeInfo.json','rb') as f2:
                resHomeInfo = json.load(f2)
            flow.response.set_text(json.dumps(resHomeInfo))
    
        # 往期战绩
        if flow.request.url.startswith('http://activity.m.duiba.com.cn/sign/contract/getContractsaaa'):
            with open('getContracts.json', 'rb') as f4:
                resContracts = json.load(f4)
            flow.response.set_text(json.dumps(resContracts))
        # 周收益排行榜
        if flow.request.url.startswith('http://activity.m.duiba.com.cn/sign/contract/getRewardRank?activityId=6aa'):
            with open('rank.json', 'rb') as f3:
                resRank = json.load(f3)
            flow.response.set_text(json.dumps(resRank))
        
        if flow.request.url.startswith("https://ydactive.sogou.com/yd/activity/duiba/wc/readingTime"):
            flow.response.set_text('jsonp1({"duration":8000,"msg":"操作成功","status":"success"})')
            ctx.log.info("replace jsonp")
            
        if flow.request.url.startswith("https://activity.m.duiba.com.cn/sign/reSign/queryCountAndStatus=="):
            flow.response.set_text('{"success":true,"code":null,"desc":null,"timestamp":null,"data":{"retryCount":9,"task":[{"taskurl":null,"vipStatus":2,"params":null},{"readStatus":2,"taskurl":null,"params":null}]}}')
            ctx.log.info("modify task status")
            
        if flow.request.url.startswith("https://activity.m.duiba.com.cn/activityPlugDrawInfo/getPrizeInfo=="):
            response = json.loads(flow.response.get_text())
            response['limitCount'] = 1
            flow.response.set_text(json.dumps(response))
            ctx.log.info('modify limitCount')
            
        if flow.request.url.startswith("http://activity.m.duiba.com.cn/sign/custom/getProfitDetail?actId=240"):
            response = json.loads(flow.response.get_text())
            response["data"][0]["changeMoney"] = 0.06
            flow.response.set_text(json.dumps(response))
            
            
addons = [
    Modify()
]
