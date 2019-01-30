from mitmproxy import ctx, http
import json

class Modify:
            
    @staticmethod
    def request(flow):
        if flow.request.url.startswith("http://activity-1.m.duiba.com.cn/customActivity/bookcode/doJoin"):
            ctx.log.info("modify request form")
            if flow.request.urlencoded_form:
                flow.request.urlencoded_form["code"] = "11111"
            else:
                flow.request.urlencoded_form = [
                    ("activityId", "20727"),("nick","name")
                ]
                
        if flow.request.url.startswith("https://activity-1.m.duiba.com.cn/hdtool/index?id=3155715"):
            flow.request.url = "https://activity-1.m.duiba.com.cn/signactivity/index?id=240&from=login&spm=6002.1.1.1"
            ctx.log.info("replace url")
            
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
