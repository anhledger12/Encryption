import random
f = open('D:\pythonProject\PythonApplication1\PythonApplication1\Em03tet\output','r')
u = f.read()
text=u.split()
#str.split(sep, maxsplit)
#Trong đó :
#sep (viết tắt của separator) là ký tự phân cách dùng để tách chuỗi str ban đầu ra các chuỗi nhỏ. Nếu không chỉ định thì python mặc định sep là ký tự trống.
#maxsplit là số lần tách lớn nhất. Nếu không chỉ định thì python mặc định số lần tách là vô hạn.
k = 64
out = ""
for uu in text:
    out = out + str(chr(int(uu)^k))
print(out)