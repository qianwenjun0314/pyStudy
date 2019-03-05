from mitmproxy import http ,ctx
import json

class Modify:
    def response(self, flow):
        if flow.request.url.startswith('https://activity.m.duiba.com.cn/hdtool/doJoin'):
            response = json.loads(flow.response.get_text())


            flow.response.set_text(json.dumps(response))






addons = [
    Modify()
]
