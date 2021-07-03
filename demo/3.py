'''try:
    print("-----test----1")
    f = open("123.txt","r")
    print("-----test----2")
    print(num)
except (NameError,IOError) as result:
    print("产生错误了")
    print(result)'''
import time

'''try:
    print("-----test----1")
    f = open("123.txt","r")
    print("-----test----2")
    print(num)
except Exception as result:
    print("产生错误了")
    print(result)'''
try:
    f=open("textd.txt","r")
    try:
        while True:#如果能顺利打开
            content = f.readline()#判别是否有内容
            if len(content) == 0:如果没内容直接跳出while
                break
            time.sleep(2)#停2秒再进行下一步
            print(content)#打印出content的内容
    finally:#finally后面一定会被执行，不管try是否报错，一定要关闭文件f，否则容易出错
        f.close()
        print("文件关闭")
except Exception as result:
    print("发生异常。。。")