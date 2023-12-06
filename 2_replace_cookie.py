import re 
import sys 

# 读取txt文件
# with open("input.txt", "r") as f:
#     line = f.readline()

f = sys.stdin.read().strip()
# 替换等号后，；前的值为test222，包括最后一个等号
import re
line = re.sub(r"(?<=\=).+?(?=;|$)", "test222", f) # $ is end 
# line = re.sub(r"(?<=\=).+?(?=;)", "test222", f)
# line = re.sub(r"(?<=\=).+?(?=;)", "test222", f)

print(line)
