import numpy as np

N,M=map(int, input("Введите числа N и M соответственно для определения размера матрицы: ").split())
r=np.random.randint(low=-1000,high=1000,size=(N,M))
tr=r.transpose()
print(r)
print(tr)
if(N==M):
    op1=int(np.linalg.det(r))
    op2=int(np.linalg.det(tr))
    op2=op1
    print(f"{op1} = {op2}")
else: print("Наша матрица прямоугольная а не квадратная, поэтому определителей не будет")
