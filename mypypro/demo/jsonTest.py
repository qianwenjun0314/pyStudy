import json

from pip._vendor.distlib.compat import raw_input


class jsonTets:
    def read(self):
        try:
            with open('../../resource/testJson.json','r') as test:
                print(test)
                # 读取json文件
                # 从文件句柄中打开文件，加载到Python的变量中，并以字典的格式转换
                f = json.load(test)
                print(type(f))

                # loads必须对于Python内存中的序列化对象转换成字符串。
                # f2 = json.loads(test)
                # print(type(f2))

                print(test.readlines())
                # print ('your like number is :%s' % f)
        except:
            inpu = raw_input('输入你喜欢的数字：')
            with open('../../resource/testJson2.json','w') as test:
                json.dump(inpu, test)  # 数据写入json文件



    def dumpsTest(self):
        name_emb = {'a': '1111', 'b': '2222', 'c': '3333', 'd': '444489'}
        #dumps用户将dict类型的数据转换成str
        jsObj = json.dumps(name_emb)

        print(name_emb)
        print(jsObj)

        print(type(name_emb))
        print(type(jsObj))


        with open('../../resource/testJson2.json','w') as f:
            #直接写入dict类型的数据到json文件中会报错
            #需要将dict类型的数据转换成str
            # f.write(name_emb) #错误方法
            # f.write(jsObj)
            # f.close()

            # dump()用于将dict类型的数据转成str，并写入到json文件中。
            json.dump(name_emb,f)


    def loadsTest(self):
        name_emb = {'a': '1111', 'b': '2222', 'c': '3333', 'd': '4444'}
        pyStr = json.dumps(name_emb)
        # loads()用于将str类型的数据转成dict。
        pyDict = json.loads(pyStr)

        print(name_emb)
        print(pyStr)
        print(pyDict)

        print(type(name_emb))
        print(type(pyStr))
        print(type(pyDict))

        # load()用于从json文件中读取数据。
        with open('../../resource/testJson.json','r') as f:
            jsObj = json.load(f)

            print(jsObj.keys())
            print(jsObj.values())
            print(type(jsObj))

            # for key in jsObj.keys():
            #     print('key:%s, value:%s'%(key, jsObj.get(key)))
            for key in jsObj.keys():
                print('%s type= %s'%(jsObj.get(key), type(jsObj.get(key))))
                # if jsObj.get(key) in '{':
                #     print('true')

    def testDict(self):
        tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
        print('testDict')
        print(tinydict.keys())
        print(tinydict.values())
        for key in tinydict.keys():
            print('key:%s, value:%s' %(key, tinydict.get(key)))



    def testJiexiJson(self):
        with open('../../resource/testJson.json', 'r') as f:
            jsObj = json.load(f)

            # print(jsObj.keys())
            # print(jsObj.values())
            # print(type(jsObj))

            # for key in jsObj.keys():
            #     print('key:%s, value:%s'%(key, jsObj.get(key)))
            for key in jsObj.keys():
                print('key:%s, value:%s'%(key, jsObj.get(key)))
                # print('%s type= %s' % (jsObj.get(key), type(jsObj.get(key))))
                # print(jsObj.get(key))
                # print(type(str(jsObj.get(key))))
                if '{' in str(jsObj.get(key)) :
                    jsObj2 = jsObj.get(key)
                    print(jsObj.get(key))
                    print(type(jsObj.get(key)))
                    for key in jsObj2.keys():
                        print('key:%s, value:%s' % (key, jsObj2.get(key)))
                        if '{' in str(jsObj2.get(key)):
                            jsObj3 = jsObj2.get(key)
                            for key in jsObj3.keys():
                                print('key:%s, value:%s' % (key, jsObj3.get(key)))


jsonTets = jsonTets()
# jsonTets.read()
# jsonTets.dumpsTest()
#jsonTets.loadsTest()

# jsonTets.testDict()

jsonTets.testJiexiJson()




