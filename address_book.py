import pandas as pd
import sys
k=int(0)
x=str('4')
bok=pd.DataFrame({
    'ФИО':[''],
    'Адрес':[''],
    'Телефон':[''],
    'Дата рождения':['']
})
print("чтобы закончить работу программы введите ноль")
while True:
    while x!='1' and x!='2' and x!='3':
        x=input("Введи единицу, если ты хочешь добавить новую запись, двойку если удалить и тройку если изменить: ")
        if x!='1' and x!='2' and x!='3' and x!='0': print("Вводить можно только цифры 0,1,2,3")
        if x=='0': sys.exit(0)
        if x=='1':
            k+=1
            F=input("Введи новый ФИО: ")
            A=input("Теперь адрес этого человека: ")
            T=input("Теперь его/её телефон: ")
            D=input("И дату рождения: ")
            row=pd.DataFrame({'ФИО':[F], 'Адрес':[A], 'Телефон':[T], 'Дата рождения':[D]})
            bok=pd.concat([bok,row], ignore_index=True)
            print(bok)
        if x=='2':
            I=int(input("Введи номер строки которую нужно удалить: "))
            PP=(I in bok)
            print(PP)
            bok.drop(I, inplace=True)
            print(bok)
    x='4'