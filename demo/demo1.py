'''f = open ('text.txt','w')#open("打开的文件名"，“模式”)
f.write("hello world, i am here!")#将字符串写入文件中'
f.close()'''
#读取指定字符开始时定位在文件头部，没执行一次向后依次指定字符数
f = open ('text.txt','r')#open("打开的文件名"，“模式”)
'''print(f.read(5))#f.read(n)读取f中前n个字符
print(f.read(5))#f.read(n)读取f中前n个字符后的n个,每次读取都会往后以此读下去'''
#print(f.readlines())
'''i=1
for temp in f.readlines():#readlines可以读取全部行
    print("%d:%s"%(i,temp))
    i+=1'''
print(f.readline())
print("1:%s"%f.readline(),end="\n")#readline只能一行一行读取
print("2:%s"%f.readline(),end="\n")