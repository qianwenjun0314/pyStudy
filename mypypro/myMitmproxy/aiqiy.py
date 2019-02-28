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
                    ("activityId", "20727"), ("nick", "name")
                ]

    def response(self, flow):
        # index
        if flow.request.url.startswith("https://activity.m.duibatest.com.cn/hdtool/index?id=20895&11111"):
            flow.response = http.HTTPResponse.make(404)
            ctx.log.info("index 返回404")

        # getShareCode
        if flow.request.url.startswith("https://activity.m.duibatest.com.cn/customActivity/iqiyiYear/getShareCode11"):
            flow.response = http.HTTPResponse.make(404)
            flow.response.set_text(
                '{"success":true,"code":null,"desc":null,"timestamp":1547261226752,"data":{"shareCode":"13b7t7q"}}')
            ctx.log.info("index 返回404")

        # getInfo
        if flow.request.url.startswith("https://activity.m.duibatest.com.cn/customActivity/iqiyiYear/getInfo?collectRuleId=131&isEnterIndex=true"):

            response = json.loads(flow.response.get_text())
            print(response)
            response['data']['collectGoods'][0]['count'] = 1
            response['data']['collectGoods'][1]['count'] = 1
            response['data']['collectGoods'][2]['count'] = 1
            response['data']['collectGoods'][3]['count'] = 1
            response['data']['collectGoods'][4]['count'] = 1
            response['data']['collectGoods'][5]['count'] = 1
            response['data']['collectGoods'][6]['count'] = 1
            response['data']['collectGoods'][7]['count'] = 1

            response['data']['isJinli'] = True
            response['data']['isOpenPrize'] = True
            response['data']['isTakeJinliPrize'] = False
            response['data']['isTakeOpenPrize'] = True
            response['timestamp'] = 1548900000000

            ctx.log.info('修改后的response')
            print(response)
            flow.response.set_text(json.dumps(response))

        # openPrize
        if flow.request.url.startswith("https://activity.m.duibatest.com.cn/customActivity/iqiyiYear/openCollectGoodsPrize"):
            flow.response = http.HTTPResponse.make(404)
            # flow.response.set_text(
            #     '{"success":true,"openReward":false,"orderNum":"889303128077520287","activityType":"ACTIVITY"}')
            # ctx.log.info("index 返回404")

        # getOrderStatus
        if flow.request.url.startswith("https://activity.m.duibatest.com.cn/customActivity/iqiyiYear/getOrderStatus11"):
            flow.response = http.HTTPResponse.make(404)
            # flow.response.set_text('{"success":true,"code":null,"desc":100001,"timestamp":1547263195583,"data":{"result":0,"lotteryCode":0,"lottery":null,"againTag":null,"exposure":null}}')

        # getTokenNew
        if flow.request.url.startswith("https://activity.m.duibatest.com.cn/hdtool/ctoken/getTokenNew"):
            # flow.response = http.HTTPResponse.make(404)
            flow.response.set_text('{"success":false}')

        # trunCard
        if flow.request.url.startswith("https://activity.m.duibatest.com.cn/customActivity/iqiyiYear/turnCard11"):
            # flow.response = http.HTTPResponse.make(404)
            flow.response.set_text(
                '{"success":true,"code":null,"desc":null,"timestamp":1547263195197,"data":{"orderNum":null}}')

        # doJoin
        if flow.request.url.startswith("https://activity.m.duibatest.com.cn/customActivity/iqiyiYear/doJoin11"):
            # flow.response = http.HTTPResponse.make(404)
            # flow.response.set_text('{"success":false,"code":100001,"desc":null,"timestamp":1547261638713,"data":{"itemId":null,"itemName":null,"orderNum":"878468957574570829"}}')
            response = json.loads(flow.response.get_text())
            print(response)
            # response['data']['itemId'] = None
            # response['data']['itemName'] = None
            response['data']['orderNum'] = None
            ctx.log.info('修改后的response')
            print(response)
            flow.response.set_text(json.dumps(response))

        # doHelp
        if flow.request.url.startswith("https://activity.m.duibatest.com.cn/customActivity/iqiyiYear/doHelp11"):
            flow.response = http.HTTPResponse.make(404)
            # flow.response.set_text('{"success":true,"code":null,"desc":null,"timestamp":1547263438417,"data":{"itemId":29141,"itemName":"佩奇","orderNum":null}}')
            # response = json.loads(flow.response.get_text())
            # print(response)
            # response['data']['itemId'] = None
            # response['data']['itemName'] = None
            # response['data']['orderNum'] = None
            # ctx.log.info('修改后的response')
            # print(response)
            # flow.response.set_text(json.dumps(response))

        # redPacketRain
        if flow.request.url.startswith("https://activity.m.duibatest.com.cn/customActivity/iqiyiYear/redPacketRain11"):
            # flow.response = http.HTTPResponse.make(404)
            flow.response.set_text('{"data":{"isCard":false,"orderNum":null},"success":true,"timestamp":1547279389271}')
            # flow.response.set_text('{"data":{"isCard":true,"itemId":null,"itemName":null},"success":true,"timestamp":1547279737421}')
            # flow.response.set_text('{"code":"999999","desc":"今日红包雨已参与过","success":false,"timestamp":1547281018639}')


        if flow.request.url.startswith("https://activity.m.duiba.com.cn/activityPlugDrawInfo/getPrizeInfo=="):
            response = json.loads(flow.response.get_text())
            response['limitCount'] = 1
            flow.response.set_text(json.dumps(response))
            ctx.log.info('modify limitCount')



addons = [
    Modify()
]
