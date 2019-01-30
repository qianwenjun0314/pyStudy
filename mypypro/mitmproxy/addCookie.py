from mitmproxy import ctx, http
import json


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


        if flow.request.url.startswith("http://spay1.shuqireader.com/api/ios/info?method=priceList"):
            #有分享
            flow.request.url = "http://activity.m.duiba.com.cn/customShare/share?id=2653&useShare=1"
            #无分享
            #flow.request.url = "http://activity.m.duiba.com.cn/customShare/share?id=2653"

            ctx.log.info("修改链接")


        if flow.request.url.startswith("https://activity.m.duibatest.com.cn/"):
            print(flow.request.cookies)            
            flow.request.cookies["_duibaServiceGroupKey"] = "miria-91"
            req = flow.request.cookies["_duibaServiceGroupKey"]
            ctx.log.info(req)


        # # 设置cookies
        # if flow.request.host == "activity.m.duibatest.com.cn":
        #     #pass
        #     flow.request.cookies["_duibaServiceGroupKey"] = "miria-91"
        #     #print(flow.request.cookies)

    def response(self, flow):
    	#index
        # if flow.request.url.startswith(""):


        if flow.request.url.startswith("https://activity.m.duibatest.com.cn/collectRule/getOrderStatus11"):
            # flow.response.set_text('{"result":0,"success":true,"message":"处理中。。。"}')
            with open('getOrderStatus.json','rb') as f:
                res = json.load(f)
            flow.response.set_text(json.dumps(res))
            ctx.log.info("modify order status")
            
     
        if flow.request.url.startswith("http://activity.m.duiba.com.cn/ngame/new/submitss"):
            flow.response = http.HTTPResponse.make(404)
            ctx.log.info("modify status code")
            
        if flow.request.url.startswith("https://activity.m.duiba.com.cn/activityPlugDrawInfo/getPrizeInfo=="):
            response = json.loads(flow.response.get_text())
            response['limitCount'] = 1
            flow.response.set_text(json.dumps(response))
            ctx.log.info('modify limitCount')
            
        if flow.request.url.startswith("http://activity.m.duiba.com.cn/sign/custom/getProfitDetail?actId=240"):
            response = json.loads(flow.response.get_text())
            response["data"][0]["changeMoney"] = 0.06
            flow.response.set_text(json.dumps(response))

        if flow.request.url.startswith("https://activity.m.duiba.com.cn/hdtool/ctoken/getTokenNew"):
            req = flow.request.headers["Cookie"]
            # req = req + "; _duibaServiceGroupKey=miria-40"
            req = ""
            ctx.log.info(req)
            flow.request.headers["Cookie"] = req


    #     if flow.request.url.startswith("http://activity.m.duibatest.com.cn/"):
    #         ctx.log.info(flow.request.url)
    #         # cookie = flow.response.headers["Cookie"]
    #         ctx.log.info(flow.response.headers["Server"])
    #         ctx.log.info(flow.request.headers["Accept"])
    #         ctx.log.info(flow.request.headers["Cookie"])
    #         # req = flow.request.headers["Cookie"]
    #         req = flow.request.cookies["_duibaServiceGroupKey"]
    #         ctx.log.info(req)
    #         flow.request.cookies["_duibaServiceGroupKey"] = "miria-91"
			 # # req = req + "; _duibaServiceGroupKey=miria-91"



            
addons = [
    Modify()
]
