import os
import csv


class readCsv:

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
        # print(dict)
        return dict



    def findAnswerByFile(self):
        # reload(sys)
        # sys.setdefaultencoding('utf8')
        with open("../../resource/quest-1.csv", 'r', encoding="gbk") as file:
            print(file)
            for line in file:
                print(line)

    def test222(self):
        csv_file = csv.reader(open('../../resource/quest-1.csv', 'r', encoding="gbk"))
        # print(csv_file)
        answer = []
        for row in csv_file:
            print(row)
            dict = {row[0],row[1]}
            answer.append(dict)
        print(answer)


    def findAnswer(self):
        csv_file = csv.reader(open('../../resource/findAnswer.csv'))
        print(csv_file)
        for i in csv_file:
            print(i)

readCsv = readCsv()
readCsv.findAnswer()