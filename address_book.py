import sys
print(sys.executable)

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
bok.index.name=('N', inplace:=True)
bok.drop(0, inplace=True)
print("чтобы закончить работу программы введите ноль")
while True:
    while x!='1' and x!='2' and x!='3':
        x=input("Введи единицу, если ты хочешь добавить новую запись, двойку если удалить и тройку если изменить: ")
        if x!='1' and x!='2' and x!='3' and x!='0': print("Вводить можно только цифры 0,1,2,3")
        if x=='0': sys.exit(0)
        if x=='1':
            k=k+1
            F=input("Введи новый ФИО: ")
            A=input("Теперь адрес этого человека: ")
            T=input("Теперь его/её телефон: ")
            D=input("И дату рождения: ")
            row=pd.DataFrame({'ФИО':[F], 'Адрес':[A], 'Телефон':[T], 'Дата рождения':[D]})
            bok=pd.concat([bok,row], ignore_index=True)
            print(bok)
            print()
        if x=='2':
            if k>0:
                I=int(input("Введи номер строки которую нужно удалить: "))
                if I in bok.index.tolist():
                    bok.drop(I, inplace=True)
                    print(bok)
                    print()
                    k=k-1
                else: print("Такой строки не существует")
            else: print("Нечего удалять, грустно")
        if x=='3':
            I=int(input("Введи номер строки которую нужно изменить: "))
            if I in bok.index.tolist():
                print("Введи Да или Нет на следующие вопросы")
                Q=str('0')
                while Q!="Да" and Q!="Нет":
                    Q=input("    Нужно изменить ФИО? ")
                S=input("На что нужно его заменить? ")
                if Q=="Да":
                    bok.iloc[I,0]=S

                Q=str('0')
                while Q!="Да" and Q!="Нет":
                    Q=input("    Нужно изменить Адрес? ")
                S=input("На что нужно его заменить? ")
                if Q=="Да":
                    bok.iloc[I,1]=S

                Q=str('0')
                while Q!="Да" and Q!="Нет":
                    Q=input("    Нужно изменить Телефон? ")
                S=input("На что нужно его заменить? ")
                if Q=="Да":
                    bok.iloc[I,2]=S

                Q=str('0')
                while Q!="Да" and Q!="Нет":
                    Q=input("    Нужно изменить Дату рождения? ")
                S=input("На что нужно его заменить? ")
                if Q=="Да":
                    bok.iloc[I,3]=S
                print(bok)
    x='4'
