from mitmproxy import ctx, http
import json
import re



class Modify:
    #新人券订单
    newUserOrderId = 906671818793340412
    #发卡订单
    orderId = 906671818793330412

    time = 3


    def request(self, flow):
        #替换cookie
        # if flow.request.host == "activity-4.m.duiba.com.cn":
        if flow.request.url.startswith("https://activity-4.m.duiba.com.cn/111"):
            print(flow.request.url)
            print(flow.request.cookies)
            flow.request.cookies["_duibaServiceGroupKey"] = "miria-91"
            flow.request.cookies["dcustom"] = "123"

            req = flow.request.cookies["_duibaServiceGroupKey"]
            ctx.log.info(req)



    def response(self, flow):

        if flow.request.url.startswith('https://activity.m.duibatest.com.cn/aaw/yonghui/help?_'):
            print(flow.request.url)
            response = json.loads(flow.response.get_text())
            print(response)

            self.newUserOrderId = response['data']['newUserOrderId']
            self.orderId = response['data']['orderId']
            print(self.newUserOrderId)
            print(self.orderId)

            # response['data']['newUserOrderId'] = self.newUserOrderId
            # response['data']['orderId'] = self.orderId
            # response['success'] = True
            # ctx.log.info('修改后的response')
            # print(response)
            # flow.response.set_text(json.dumps(response))


        # if flow.request.url.startswith('https://activity.m.duibatest.com.cn/plugin/getOrderStatus?orderId=' + self.newUserOrderId):
        #     flow.response.set_text('{"result":0,"lotteryCode":0,"success":true,"message":"处理中。。。"}')
        #     ctx.log.info("replace ")

        # for i in range(10):


        # if flow.request.url.startswith('https://activity.m.duibatest.com.cn/plugin/getOrderStatus'):
        #     if self.time > 0:
        #         flow.response.set_text('{"result":0,"lotteryCode":0,"success":true,"message":"处理中。。。"}')
        #         print(self.time)
        #         ctx.log.info("replace ")
        #         self.time -= 1
        #         print(self.time)

        if flow.request.url.startswith('https://activity.m.duibatest.com.cn/plugin/getOrderStatus'):
            body = flow.request.get_text()
            print(body)
            pattern = r'orderId=(.*)&'
            res = re.match(pattern, body)
            print(res.group(1))
            # if res.group(1) == self.newUserOrderId:
            if res.group(1) == self.orderId:
                print('匹配到')
                flow.response.set_text('{"result":0,"lotteryCode":0,"success":true,"message":"处理中。。。"}')


addons = [
    Modify()
]