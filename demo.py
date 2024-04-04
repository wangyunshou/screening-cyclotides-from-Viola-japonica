# _*_ coding:utf-8 _*_
#用于将txt文本的英文，根据词库提取生词
import re
import string
from tempfile import tempdir
from turtle import showturtle

#将文本转换为列表
def Changetxt(input_path):
	r = open(input_path,"r",encoding='UTF-8')	#输入文本
	strs =r.read()
	s = re.findall("\w+",str.lower(strs))	#使用正则提取单词来，修改为小写
	l = list(set(s))			#去除列表中的重复项
	l.sort(key = s.index)			#set会乱序，使用sort保持原来的顺序
	r.close()
	return l





def Handle_data(output_path,new_paper_word):
    num = 0					#用于记录本次匹配的生词数
    f = open(output_path,"w",encoding='UTF-8')	#用于记录筛选的生词
    for i in new_paper_word:
        num2=0
        # m = re.search("\d+",i)
		# n = re.search("\W+",i)
		#num2=0
        for j in i:
            num2 += 1
            if j == "g":
                num3 = 24
                while num3<40:
                    num3 += 1
                    shou=i[num2-1:num2+num3]
                    #print(shou)
                    if  shou.endswith("n") or shou.endswith("d"):#尾字母要求
                        #if not shou.endswith(" "):
                        if "c" in shou:
                            f.write(shou +"\n")
                            num += 1
    print('第一步筛选成功，本次共成功筛选了' + str(num) + '个生词')

def Ela(two_input,two_output):
    yy= 0					#用于记录本次匹配的生词数
    f2 = open(two_output,"w",encoding='UTF-8')	#用于记录筛选的生词
    print(two_input)
    for i2 in two_input:
        num2=0
        for j2 in i2:
            if j2 == "c":
                num2 += 1
            if num2 > 5:
                f2.write(i2 +"\n")
                yy += 1
                break
    print('第二步筛选成功，本次共成功筛选了' + str(yy) + '个生词')
            



input_path = r'C:\Users\lenovo\Desktop\ye.txt'	#用于筛选生词的txt路径，txt里应该是能够正常阅读的英文
output_path = r'C:\Users\lenovo\Desktop\get.txt'	#筛选出的生词
two_output = r'C:\Users\lenovo\Desktop\finally.txt'

new_paper_word = Changetxt(input_path)		#获取论文单词list
Handle_data(output_path,new_paper_word)	#数据匹配处理，最终赛选出结果
two_input = Changetxt(output_path)
Ela(two_input,two_output)