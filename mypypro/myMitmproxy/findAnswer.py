from mitmproxy import http,ctx
import json
import csv


class Modify:

    def __init__(self):
        self.answer = self.findAnswerByCsv()
        # GetQuestion.answer = self.findAnswerByCsv()
        print(self.answer)


    def findAnswerByCsv(self):
        csv_file = csv.reader(open('../../resource/quest-1.csv','r',encoding="gbk"))
        print(csv_file)
        dict = {}
        for row in csv_file:
            dict[row[0]] = row[1]
        return dict

    def response(self, flow):

        if flow.request.url.startswith('https://activity.m.duiba.com.cn/hdtool/watsons/recon/question/list'):
            question = []
            response = json.loads(flow.response.get_text())
            # for i in range(0,6):
            #     for key, v in response['data'][i][]:
            #         print(self.answer[key])
            #     # question.append(response['data'][i]['name'])
            # print('问题列表是：%s'%question)
            # print(self.answer)

            for i in response['data']:
                print(self.answer[i['name']])




addons = [
    Modify()
]