from mitmproxy import ctx, http
import json


class Modify:
    pluginOrderNum = '9999'
    prizeOrderNum = '8888'

    @staticmethod
    def request(flow):
        if flow.request.url.startswith("http://activity-1.m.duiba.com.cn/customActivity/bookcode/doJoin"):
            ctx.log.info("modify request form")
            if flow.request.urlencoded_form:
                flow.request.urlencoded_form["code"] = "11111"
            else:
                flow.request.urlencoded_form = [
                    ("activityId", "20727"), ("nick", "name")
                ]

        if flow.request.url.startswith("https://activity-1.m.duiba.com.cn/hdtool/index?id=3155715"):
            flow.request.url = "https://activity-1.m.duiba.com.cn/signactivity/index?id=240&from=login&spm=6002.1.1.1"
            ctx.log.info("replace url")

    def response(self, flow):
        # 游戏
        if flow.request.url.startswith("https://activity.m.duiba.com.cn/ngapi/dostart11"):
            flow.response.set_text(
                '{"credits":9,"message":"请求成功","success":false,"submitToken":"/*2iF8GjV8ouePJI*/var/*YzRdt*/__4tlBr/*8YOAhkGYt*/=\\u0053\\u0074\\u0072\\u0069\\u006e\\u0067\n/*SJkuMddoM*/./*2fo9WqjRq4ytPW*/\\u0066r\\u006fm\\u0043ha\\u0072C\\u006fde/*RkowfV1aXv7*/;\nvar/*d04Cj*/_x_ODj = [/*5jVo0H2i6*/3048,2123,1049,2975,3865,/*S2UPL16jPlZiiDiM*/];//nI0WVmgjUcakNmqth\nvar/*6yiyH4dzMf3b9Rbk0i5*/_$SSC/*4VFZSwB*/=/*TBiqtve6igEJQ*/function(/*IdIg8320oKPMt*/){\n/*u1L6biH*/return/*knJkE5s4OYfrHi*/arguments[/*R2ICFmxQ2*/0]^/*mNYKpaDQFb7imd1*/\n/*daxlyVFf9kR5dVpx6r*/_x_ODj[/*f5KChFpqBS3kNfT68bn*/0];/*zpSaX*/}/*9qfg2LZ4CZBjKCgdUq*/;\nvar/*xymA6BFV2Tl0YvFe6*/_$Kxf/*0LIDek*/=/*wp66nh6PrW0Fxr*/function(/*1WMGsnb3FWhfwKuFP*/){\n/*i5e78OVN40J7shj1b*/return/*NGFK2d*/arguments[/*1ZLlTQ7AkbTpQ2d*/0]^/*0b1AffjFzt3VmqZ*/\n/*g8FrpZAY8dUEWQ*/_x_ODj[/*wiIocMBdUUkUDIsuY*/1];/*CKy3HL*/}/*yY7vfuxR6hx9dz*/;\nvar/*hnYYIsY3d*/_$qw3/*T5hXLrzvZ*/=/*DXAwF*/function(/*izZDo1KOiIcx9*/){\n/*00PMzp*/return/*0pj7TEq*/arguments[/*vN3Z4AywUbiMwrIVm*/0]^/*kaqXRu3CGu*/\n/*rRp3Pwk*/_x_ODj[/*WTuRsgWywTApx*/2];/*PF2Ot0Js*/}/*CakoU9CBiPCm*/;\nvar/*1GyqhGEuvOOW6aGkEPJ*/_$U6g/*lVVVhC*/=/*YcBl0Xp87*/function(/*k7K6em2vC5KR4*/){\n/*eDpucYkgjHJj5emZnDl*/return/*RYVS3OnkUAFLtv*/arguments[/*BVx0Ct0*/0]^/*ASv0PWt0FgAZdG7FN3G*/\n/*8Dm84yCd5Re4Lm*/_x_ODj[/*m5Utp4rpLkCnYV*/3];/*tNx7S*/}/*WhFALSeG7A1wjU1ma*/;\nvar/*TyB0YZhBZFC*/_$qo99/*KJ7PBXj5BHSAkASU9Vb*/=/*yBIDtuRmtjqSwwi*/function(/*kuf1OF2uU*/){\n/*0l53n7p9C9N9EC4GA5t*/return/*3odSRWSo5wzfh*/arguments[/*f85Uei7dXg*/0]^/*kmMtArOzRW*/\n/*Kz6hUOmN7CF93BYYvQL*/_x_ODj[/*KOEq1FglNkDS6IW*/4];/*jS1azcrih6bJmDvaY4E*/}/*bKLNhj1Clnsu9A*/;\n/*2DrZGsjdYYBphNvzl*/\\u0065\\u0076\\u0061\\u006c/*9gnd1MbXiW*/(__4tlBr(32)\n+/*rNnWGKK8fv7J*/__4tlBr(_$SSC(-1-~/*DHqj*/(0xbb7^0)),111,114,100,_$qo99(~/*QGnLOgVysFd9u*/~/*MKLWKEW*/3964),_$SSC(2970/*YQ*/),Math.abs(84)&-1,111,1075/0xA,101,\n0x0|0x6e,0x20,61,321/0xA,-1-~/*2MGX*/(0x22^0),0x31,49/*Vt*/,_$Kxf(2172&(-1^0x00)),52,97,\n101&(-1^0x00),060,57&(-1^0x00),-1-~/*DX*/(0x37^0),0x3804/0400,-1-~/*Deie*/(0x62^0),0x3991>>/*4VMR7wkMpiQDcrt64*/4>>4,~(0x34^/*gD*/-1),0x65,~/*p8U5d6fzg*/~/*OQy9uKxZXwj*/101,\n_$SSC(~(0xbdb^/*AOsv*/-1)),~(0x61^/*NclI*/-1),53,48,0x39,070,0x0|0x32,~(0x35^/*Ptr*/-1),0x0|0x30,98,\n98/*Vd*/,100,0x3429/0400,51,0x6504>>/*EeQvcn9CdQutFeUK2Wu*/4>>4,~/*FI7sBkW7h19MNDTuy6*/~/*kBKlWlzS8cxh18o*/98,487/0xA,~(0x22^/*02*/-1)/*kS1Y0bHiEooJD*/));/*ghBAv*/\n","ticketId":"326095607","token":"/*FR8IHiVxc*/var/*aJlC4cyKYJ7aZB2su*/__RbXa/*i1lyQ0AluRMP2nqrG*/=\\u0053\\u0074\\u0072\\u0069\\u006e\\u0067\n/*lVSmMABQElytCGKC8PP*/./*4pTtTHbeaT*/\\u0066r\\u006fm\\u0043ha\\u0072C\\u006fde/*GNZP7Ypj*/;\nvar/*ZZOPU32Lg8NqmcqT0*/_x_24Q = [/*EhelO67bJF*/2757,3037,2110,2547,1067,/*DrVTub9AL*/];//a4crsc9wyN0T\nvar/*3klvKfA*/_$O74/*5MdRy8yOMQku8PKzcr*/=/*kPbVpwm9*/function(/*AFk6kL6ESCC9*/){\n/*WeHvFViey*/return/*ZSRUo67oDI7CKmz*/arguments[/*XxuhzKDgq9vuIF6*/0]^/*0HO0YdagWz*/\n/*XCouQjVY*/_x_24Q[/*Mq5MbmiHNk6lv8*/0];/*gXGbnCQ11DEM2*/}/*8cjqYLXAnGB03YWi*/;\nvar/*QbZoho*/_$l6B/*8PWvFRpc89WQ3l*/=/*a8WpxiaGehYIdNLT*/function(/*WnkChEQrOIz6EhZ68*/){\n/*04lLtMXdkPquCsX6K*/return/*yTBdPD76q*/arguments[/*RrpAGRxPPKEf1rhVfs*/0]^/*nxt8eGF803V*/\n/*R3107Uby*/_x_24Q[/*9dbxt7M1Ht1erz2F*/1];/*uTMxYT8fA60gYyifEVD*/}/*Xr2oOzj4cWWjGVl9*/;\nvar/*iO4tiJw*/_$wbZ/*koPCrFU7sq0X3*/=/*ePknnUrT6mnqn6kvnN4*/function(/*fiDR4rGx9*/){\n/*oWsiWf6l4dvk1g4S*/return/*8V68UX*/arguments[/*Fm4djq7vuC4zwdwPDMP*/0]^/*0kE3ZfEyj*/\n/*CCAkz4by7*/_x_24Q[/*IqjxVjknPldHmYt2*/2];/*Rw4ww*/}/*eQk53HsZaKqWcTtYcw8*/;\nvar/*CeYEhVNnB8yu9FJ1Zoo*/_$ZNZ/*o0aiZ6hevyRC61p*/=/*PFvvX*/function(/*c6B20kW*/){\n/*A2rHC0bOuQa7R*/return/*WOB15Q8xtyGTt2F6D*/arguments[/*D5JQQNd1oyT1gq*/0]^/*hJk71L0*/\n/*K5CxGPe1Z8IEiWZsk*/_x_24Q[/*yWkuQtq*/3];/*cVTsavA*/}/*m5vw5Nc1uAJARrEj*/;\nvar/*nmdFA529aFp1TX*/_$7Mv/*QxGZ4bLYQkx*/=/*6dSiYIBbrtg3BCf*/function(/*avuwQm09p2fDo5a*/){\n/*J3qLVjmnejL1Eg5*/return/*58QnBU7MeWsVo*/arguments[/*i8LJhqDPkAizn*/0]^/*SGU7pGTM*/\n/*FAJco0B*/_x_24Q[/*rFLOeeA2o*/4];/*XiXNK3L6o*/}/*DeOBf7XgCNlU7u*/;\n/*jFHaCJLycGO0l8j*/\\u0065\\u0076\\u0061\\u006c/*IoBPEgwhcbhyxQ*/(__RbXa(32)\n+/*PFqaFnhKyX0TTF2lUte*/__RbXa(0x5f,0x7423/0400,0x6f00>>/*mqx6diob8y*/4>>4,107,~/*yAPHOA8lyyK*/~/*bD9b2nO*/101,~/*xOZMJuSyDBaYIKaCXBv*/~/*0vsWS9wHqIh5t2arOS*/110,32&(-1^0x00),610/0xA,32/*U8*/,_$l6B(30716/0xA),\n067,99/*fS*/,987/0xA,_$ZNZ(2458),54,_$7Mv(~/*5FBo7S*/~/*LMGnzJJviTnJnsC*/1042),1171/0xA,0x22/*MJnFAztzsZV5PDWQizHdxW*/));/*JO2txEVr0K2DFn09*/\n"}')
            ctx.log.info("doStart修改成功")

        if flow.request.url.startswith("https://activity.m.duiba.com.cn/ngapi/getStartStatus11"):
            flow.response.set_text('{"code":0,"success":true,"message":"处理中"}')
            # flow.response.set_text('{"code":1,"success":true,"message":"处理成功"}')
            ctx.log.info("getStartStatus修改成功")

        if flow.request.url.startswith('https://activity.m.duiba.com.cn/ngame/new/submit11'):
            flow.response.set_text(
                '{"success":false,"code":null,"desc":null,"timestamp":1546596771358,"data":{"orderId":326096852,"rsp":{"totalScore":26,"maxScore":2,"maxScoreTime":"2019-01-04 16:18:52","rank":3,"percentage":33.33,"token":"/*beglc00gYYcPI1327Q*/var/*VkEYl*/__XB1GdlK/*sp6ixlK8*/=\\u0053\\u0074\\u0072\\u0069\\u006e\\u0067\n/*AGVu0*/./*TdfFUZVT*/\\u0066r\\u006fm\\u0043ha\\u0072C\\u006fde/*9CN2rV2kmFJP*/;\nvar/*U5wcsVyy3sKcB3yV5aC*/_x_2iD = [/*CqXjiB9235bahVG2je*/1157,782,3038,1651,3577,/*2FeoYBKalr6*/];//FR0QfmxjHDUASojx\nvar/*I0nAzyCjlrxUnS2mPa*/_$BmZ/*3pCICLljR*/=/*Ruj0ctv9xgzpq35EyD*/function(/*c2kgqPa5iZbFIfRIrNG*/){\n/*HtPyujBMmC*/return/*rt2bHhmsg9*/arguments[/*ptwpRkYSvYtDC7o6Ex*/0]^/*a0flPIUP0yNtBUtb2*/\n/*4vXUP2OxISTIVzds*/_x_2iD[/*0P7gTdNwjaIkn*/0];/*zQIvJM1pvDXXzO*/}/*ZmeaGEmPBteCdtgYWF*/;\nvar/*Vb89RxqJvycwwnjJioR*/_$7Fq/*P5jS3OyFrBDS*/=/*ICgP6U7856S8cSe*/function(/*3ho3Z1kDf*/){\n/*gtzRZsvra74NftwTBn*/return/*Zjv9TzlIR8bgIkeOZW*/arguments[/*j4dz52UVR75Gs*/0]^/*MoZJys9CVt83NXAVKo*/\n/*1YwNpfcesQs6QeRQK*/_x_2iD[/*WFCjcsPuIx*/1];/*5diti9WFOKmwOrRY*/}/*2UGqysrla9ZWWTaXT*/;\nvar/*mN2E8*/_$2Oe/*Odn2OnDg1R*/=/*24yJBrJNAIraYi9foB*/function(/*p4k649MDUIA*/){\n/*u4bKdyJM5PVKFu*/return/*oVRjPc*/arguments[/*ypQv20uhtczC24O*/0]^/*SDW83wN62Totg*/\n/*7zGwwLlwBt5Rm5*/_x_2iD[/*9riHRRteRJI*/2];/*eYBW3i6*/}/*xuPKBCqDzMB719I*/;\nvar/*Kpx7mdt5iSlZipYBr*/_$yBa/*Iv6DkiV7W2YbBlihp*/=/*8Qalm5l6ju*/function(/*sHOMN8ui0*/){\n/*qzp92SU6jtNslzMPyQ*/return/*S1SomvEE22E*/arguments[/*XQqD96*/0]^/*p0wVKCi7SpU*/\n/*CDy8jcX*/_x_2iD[/*ZTD8Ggn*/3];/*4oi7IIuJaaus69*/}/*njUMKWUpYR*/;\nvar/*wxp2NbLPBCIPYkC*/_$J8a/*fuEbog*/=/*DZ4JDGb*/function(/*F5CGdkIhoGje0hu*/){\n/*Jl2KbLijAs*/return/*gRJYoXbbdbv*/arguments[/*8IexfrbQ*/0]^/*UWH1eSF4Hgj*/\n/*BvWug41BcimaSOZc*/_x_2iD[/*MPJNYW4cymS2e0f1I*/4];/*E5JJX2*/}/*ZueuGywCt5mg61kKwF*/;\n/*CHFpJB1C08gTYyJ*/\\u0065\\u0076\\u0061\\u006c/*3NMHKp57r*/(__XB1GdlK(32)\n+/*VvpkawQyb*/__XB1GdlK(957/0xA,-1-~/*RkOJ*/(0x74^0),111,0x6b94/0400,101,~(0x6e^/*0Mm*/-1),040,0x0|0x3d,0x0|0x20,_$yBa(1617),\n063,~(0x78^/*aJ*/-1),~(0x74^/*5V*/-1),98,0x0|0x67,~/*UYVRZmdVCLP6X*/~/*G0IGz7rhX1W9RigsVJq*/117,117,343/0xA/*wa6FBkRbmlfLiqUVn2oof6fmYEpirY*/));/*lP7QK*/\n","consumerId":280610191,"status":{"code":0,"btnText":"开始游戏","btnDisable":false,"text":"9积分/次","addCount":0,"freeCount":0,"btnEventType":null,"btnEvent":null},"credits":438319,"uid":"3","allowStart":true,"ngameId":null,"lock":false,"nickName":"小黄"},"json":null}}')
            ctx.log.info("submit修改成功")

        if flow.request.url.startswith('https://activity.m.duiba.com.cn/ngame/new/getSubmitResult?orderId'):
            # 失败
            # flow.response.set_text('{"success":false,"code":null,"desc":null,"timestamp":1546596771398,"data":{"success":true,"message":"请求成功","tip":null,"option":null,"useDpm":null,"againDpm":null,"flag":false,"score":null}}')
            # 处理中
            flow.response.set_text(
                '{"success":true,"code":null,"desc":null,"timestamp":1546596771398,"data":{"success":true,"message":"请求成功","tip":null,"option":null,"useDpm":null,"againDpm":null,"flag":true,"score":null}}')
            ctx.log.info("getSubmitResult修改成功")

        # 插件抽奖-测试
        if flow.request.url.startswith("https://activity.m.duibatest.com.cn/activityPlugDrawInfo/doJoinPlugdraw11"):
            flow.response.set_text('{"orderId":"","orderNum":"","success":false}')

        if flow.request.url.startswith("https://activity.m.duibatest.com.cn/plugin/getOrderStatus11"):
            flow.response.set_text('{"result":0,"lotteryCode":0,"success":true,"message":"处理中。。。"}')

        if flow.request.url.startswith("https://activity.m.duibatest.com.cn/customActivity/qqMusic/getLockStatus11"):
            flow.response.set_text(
                '{"success":true,"code":null,"desc":null,"timestamp":1545188847138,"data":{"consumeCredits":828888888888,"pluginTwoStatus":true,"pluginThreeStatus":false}}')
        # 插件抽奖-线上
        if flow.request.url.startswith("https://activity.m.duiba.com.cn/plugin/doJoin11"):
            flow.response.set_text('{"orderId":"","orderNum":"","success":false}')

        if flow.request.url.startswith("https://activity.m.duiba.com.cn/plugin/getOrderStatus11"):
            flow.response.set_text('{"result":0,"lotteryCode":0,"success":false,"message":"处理中。。。"}')

        if flow.request.url.startswith("https://activity.m.duiba.com.cn/customActivity/qqMusic/getLockStatus11"):
            flow.response.set_text(
                '{"success":true,"code":null,"desc":null,"timestamp":1545188847138,"data":{"consumeCredits":828888888888,"pluginTwoStatus":true,"pluginThreeStatus":false}}')

        if flow.request.url.startswith("https://activity.m.duiba.com.cn/activityPlugDrawInfo/doJoinPlugdraw"):
            flow.response.set_text('{"orderId":"862103145132300984","orderNum":"862103145132300984","success":false}')
        if flow.request.url.startswith("https://activity.m.duiba.com.cn/collectRule/getOrderStatus11"):
            flow.response.set_text('{"result":0,"success":true,"message":"处理中。。。"}')

        # 活动工具
        if flow.request.url.startswith("https://activity.m.duiba.com.cn/hdtool/doJoin11"):
            # flow.response.set_text('{"orderId":"858477100366630001","success":false,"needCredits":1}')
            flow.response = http.HTTPResponse.make(404)
            # flow.response.set_text('{"orderId":"858477100366630001","success":true,"needCredits":1}')
            # flow.response.set_text('{"orderId":"","success":true,"needCredits":1}')

        if flow.request.url.startswith("https://activity.m.duiba.com.cn/hdtool/getOrderStatus11"):
            # flow.response.set_text('{"result":2,"showchat":true,"isPopup":false,"success":false,"lottery":{"id":272781,"imgurl":"//yun.duiba.com.cn/images/201812/gj16hy9vd4.png","isAppHidden":true,"isDownloadUrl":true,"itemId":49969,"link":"//activity.m.duiba.com.cn/activity/takePrizeNew?recordId=5296376717&dbnewopen","linkTo":0,"title":"番茄底料","type":"virtual"},"element":{"freeEmpty":true,"freeLimit":4,"isCreditsTypeOpen":false,"myCredits":"1万","needCredits":"1","status":6}}')
            # flow.response.set_text('{"result":0,"lotteryCode":0,"success":true,"message":"处理中。。。"}')
            flow.response = http.HTTPResponse.make(504)

        if flow.request.url.startswith("http://activity.m.duibatest.com.cn/hdtool/doJoin11"):
            with open('hdtoolDojoinError.json', 'rb') as q2:
                res = json.load(q2)
            flow.response.set_text(json.dumps(res))
            ctx.log.info("doJoin Error")

        if flow.request.url.startswith("http://activity.m.duibatest.com.cn/hdtool/getOrderStatus11"):
            # 处理中
            with open('getOrderStatus1.json', 'rb') as q3:
                res = json.load(q3)
            flow.response.set_text(json.dumps(res))
            ctx.log.info("doJoin getOrderStatus Error")

        # pk
        if flow.request.url.startswith("http://activity.m.duibatest.com.cn/betActivity2/doJoin11"):
            with open('pkDojoinError.json', 'rb') as q3:
                res = json.load(q3)
            flow.response.set_text(json.dumps(res))
            ctx.log.info("doJoin Error")
        if flow.request.url.startswith("http://activity.m.duibatest.com.cn/betActivity2/getOrderStatus11"):
            with open('pkStatus1.json', 'rb') as q4:
                res = json.load(q4)
            flow.response.set_text(json.dumps(res))
            ctx.log.info("doJoin Error")

        # 修改抽奖结果，为处理中
        if flow.request.url.startswith("https://activity.m.duibatest.com.cn/collectRule/getOrderStatus11"):
            # flow.response.set_text('{"result":0,"success":true,"message":"处理中。。。"}')
            with open('getOrderStatus.json', 'rb') as f:
                res = json.load(f)
            flow.response.set_text(json.dumps(res))
            ctx.log.info("modify order status")

        if flow.request.url.startswith("http://activity.m.duiba.com.cn/hdtool/ajaxElementss11"):
            flow.response.set_text(
                '{"showchat":true,"throughCurrent":"1","isPopup":false,"throughMode":1,"jsTest":"//yun.duiba.com.cn/h5/showCouponPrize/4.0.0/index_201710191434.js","rule":"规则规则","type":"hdtool","throughNum":1,"throughCurrentStep":24,"success":true,"cssTest":"//yun.duiba.com.cn/h5/showCouponPrize/4.0.0/index_201710191440.css","options":[{"hidden":true,"id":264806,"logo":"//yun.duiba.com.cn/upload/uP99F1462438316972.png","name":"谢谢参与","prizeType":"thanks"},{"hidden":true,"id":264913,"logo":"//yun.duiba.com.cn/upload/uP99F1462438316972.png","name":"谢谢参与2","prizeType":"thanks"}],"element":{"freeEmpty":false,"freeLimit":0,"isCreditsTypeOpen":false,"myCredits":"289892","needCredits":"5","status":4}}')

        # 修改签到返回-为签到失败
        if flow.request.url.startswith("https://activity.m.duiba.com.cn/signactivity/doSign"):
            with open('signError.json', 'rb') as q1:
                res = json.load(q1)
            flow.response.set_text(json.dumps(res))
            ctx.log.info("modify sign signError success")

        if flow.request.url.startswith("https://activity.m.duiba.com.cn/signactivity/doSign11"):
            response = json.loads(flow.response.get_text())
            ctx.log.info(response)
            # "customInfo": "\"\""
            # response['customInfo'] = '""'

            # response['customInfo'] = ''
            response["customInfo"]["orderNum"] = ''
            flow.response.set_text(json.dumps(response))
        # 海底捞签到发卡订单查询
        if flow.request.url.startswith("https://activity.m.duiba.com.cn/plugin/getOrderStatus11"):
            # flow.response.set_text('{"result":0,"lotteryCode":0,"success":true,"message":"处理中。。。"}')
            flow.response.set_text(
                '{"result":2,"lotteryCode":1,"success":true,"lottery":{"id":18108,"imgurl":"//yun.duiba.com.cn/webapp/img/collect_goods.png","isAppHidden":true,"itemId":111,"title":"海底捞-捞卡","type":"collectGoods"},"takeSuccess":false}')

            ctx.log.info("replace ")
        # 海底捞发卡后调插件接口
        if flow.request.url.startswith("https://activity.m.duiba.com.cn/plugin/doJoin11"):
            # flow.response.set_text('{"orderId":"837678477862870696","orderNum":"837678477862870696","success":false}')
            # ctx.log.info("replace ")
            response = json.loads(flow.response.get_text())
            self.pluginOrderNum = response["orderNum"]
            ctx.log.info("pluginOrderNum=" + self.pluginOrderNum)
        if flow.request.url.startswith(
                "https://activity.m.duiba.com.cn/plugin/getOrderStatus?orderId11=" + self.pluginOrderNum):
            flow.response.set_text('{"result":0,"lotteryCode":0,"success":true,"message":"处理中。。。"}')
            ctx.log.info("replace ")

        # 海底捞集卡开大奖
        if flow.request.url.startswith("https://activity.m.duiba.com.cn/plugin/collectRule/openCollectGoodsPrize11"):
            # flow.response.set_text('{"orderId":{"activityType":"plugin","appId":1,"consumeCredits":0,"consumeCreditsStatus":1,"consumerId":2444873380,"duibaActivityId":3807,"exchangeStatus":1,"ip":"124.160.32.2","orderNum":"837678477863110676","partnerUserId":"2777"},"success":false,"openReward":false,"orderNum":"837678477863110676","activityType":"ACTIVITY"}')
            # ctx.log.info("openCollectGoodsPrize replace")
            response = json.loads(flow.response.get_text())
            self.prizeOrderNum = response["orderNum"]
            ctx.log.info("prizeOrderNum=" + self.prizeOrderNum)
        if flow.request.url.startswith(
                "https://activity.m.duiba.com.cn/plugin/getOrderStatus?orderId=" + self.prizeOrderNum):
            flow.response.set_text('{"result":0,"lotteryCode":0,"success":true,"message":"处理中。。。"}')
            ctx.log.info("replace ")

        if flow.request.url.startswith("https://activity.m.duiba.com.cn/plugin/collectRule/openCollectGoodsPrize111"):
            flow.response = http.HTTPResponse.make(404)
            ctx.log.info("modify status code")

        if flow.request.url.startswith("https://activity.m.duiba.com.cn/activityPlugDrawInfo/getPrizeInfo11"):
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
