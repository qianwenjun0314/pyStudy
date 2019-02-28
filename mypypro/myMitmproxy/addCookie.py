from mitmproxy import ctx, http
import json


class Modify:
            
    # @staticmethod
    def request(self, flow):
        if flow.request.url.startswith("http://activity-1.m.duiba.com.cn/customActivity/bookcode/doJoin"):
            ctx.log.info("modify request form")
            if flow.request.urlencoded_form:
                flow.request.urlencoded_form["code"] = "11111"
            else:
                flow.request.urlencoded_form = [
                    ("activityId", "20727"),("nick","name")
                ]

        #替换请求链接
        if flow.request.url.startswith("http://spay1.shuqireader.com/api/ios/info?method=priceList"):
            #有分享
            flow.request.url = "http://activity.m.duiba.com.cn/customShare/share?id=2653&useShare=1"
            ctx.log.info("修改链接")

        #替换cookie
        # if flow.request.host == "activity-4.m.duiba.com.cn":
        if flow.request.url.startswith("https://activity-4.m.duiba.com.cn/"):
            print(flow.request.url)
            print(flow.request.cookies)
            flow.request.cookies["_duibaServiceGroupKey"] = "miria-91"
            flow.request.cookies["dcustom"] = "123"

            req = flow.request.cookies["_duibaServiceGroupKey"]
            ctx.log.info(req)


    # @staticmethod
    def response(self, flow):
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


addons = [
    Modify()
]

