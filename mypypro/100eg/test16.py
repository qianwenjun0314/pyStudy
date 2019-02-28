import test
import datetime

#__name__等于python的名字（即模块名）
#“Make a script both importable and executable”
#意思就是说让你写的脚本模块既可以导入到别的模块中用，另外该模块自己也可执行

def main():
  print ("we are in %s"%__name__)
if __name__ == '__main__':
  print('11')
  main()

def test16():
  # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
  print(datetime.date.today().strftime('%d/%m/%Y'))

  #创建日期对象
  date1 = datetime.date(1993,3,14)
  print('我的生日是：%s'%(date1.strftime('%d/%m/%y')))

  #日期运算
  date2 = date1 + datetime.timedelta(days=1)
  print('计算之后的日期是：%s'%(date2.strftime('%d/%m/%y')))

  # 日期替换
  date3 = date2.replace(year=date2.year + 1)

  print('替换之后的日期是：%s'%date3.strftime('%d/%m/%Y'))

test16()