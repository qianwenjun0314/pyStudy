from mitmproxy import http,ctx
import json


class Modify:
    def request(self, flow):
        if flow.request.url.startswith('https://hd.dlp.duiba.com.cn/signin/configEdit11'):
            if flow.request.urlencoded_form:
                print(flow.request.urlencoded_form)
                # flow.request.urlencoded_form["reSignRule"] = '{"open":true,"dateUnit":"CUSTOM","days":null,"conType":null,"credits":null,"card":null,"awardType":null,"countLimit":null,"openAddLimit":true,"addLimitCycle":"WEEK","addLimitCount":null}'
                # print(flow.request.urlencoded_form["reSignRule"]['open'])
                # req = flow.request.urlencoded_form.to_dict()
                # print(req)
                # flow.request.urlencoded_form["reSignRule"]['open'] = True

    def response(self, flow):
        if flow.request.url.startswith('https://hd.dlp.duiba.com.cn/signin/findConfigById11'):
            response = json.loads(flow.response.get_text())
            response['data']['reSignRule']['open'] = True
            flow.response.set_text(json.dumps(response))




        if flow.request.url.startswith('https://activity.m.duiba.com.cn/hdtool/recon/doJoin11'):
            response = json.loads(flow.response.get_text())
            response['data'] = False
            flow.response.set_text(json.dumps(response))

        if flow.request.url.startswith('https://activity.m.duiba.com.cn/hdtool/recon/ngame/getNgameStartStatus11'):
            response = json.loads(flow.response.get_text())
            response['success'] = False
            response['code'] = 'C000000001'
            flow.response.set_text(json.dumps(response))

        if flow.request.url.startswith('https://activity.m.duiba.com.cn/hdtool/recon/ngame/resurrection11'):
            response = json.loads(flow.response.get_text())
            response['success'] = False
            response['data'] = None
            flow.response.set_text(json.dumps(response))

        if flow.request.url.startswith('https://activity.m.duiba.com.cn/hdtool/recon/ngame/resurrectionStatus11'):
            response = json.loads(flow.response.get_text())
            response['success'] = False
            response['code'] = 'C000000001'
            flow.response.set_text(json.dumps(response))


        if flow.request.url.startswith('https://activity.m.duiba.com.cn/hdtool/recon/ngame/ngameManySubmit111'):
            response = json.loads(flow.response.get_text())
            response['success'] = False
            response['data'] = None
            response['code'] = '99999999'
            flow.response.set_text(json.dumps(response))

        if flow.request.url.startswith('https://activity.m.duiba.com.cn/hdtool/recon/getOrderStatus?orderId=11'):
            response = json.loads(flow.response.get_text())
            response['success'] = False
            response['code'] = '999999'
            flow.response.set_text(json.dumps(response))



addons = [
    Modify()
]