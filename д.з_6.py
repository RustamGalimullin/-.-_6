import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline

zp=np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks=np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

def covar(array1, array2):
    MXY=sum(array1*array2)/len(array1)
    MX=sum(array1)/len(array1)
    MY=sum(array2)/len(array2)
    return MXY-MX*MY

covar(zp,ks)

"9157.839999999997"

np.cov(zp, ks, ddof=0)

"array([[ 3494.64,  9157.84],"
"[ 9157.84, 30468.89]])"

def sigma(array, offset=True):
    mean_array=sum(array)/len(array)
    square_dev=(array-mean_array)**2
    variance=sum(square_dev)/len(array) if offset else sum(square_dev)/(len(array)-1)
    return variance**0.5

r=covar(zp, ks)/(sigma(zp)*sigma(ks))
print(f'Коэффициент корреляции r = {r: .5f}')

"Коэффициент корреляции r =  0.88749"

r1=np.cov(zp, ks, ddof=1)/(sigma(zp, offset=False)*sigma(ks, offset=False))
print(f'Коэффициент корреляции r = {r1}')

"Коэффициент корреляции r = [[0.33866702 0.88749009]"
"[0.88749009 2.95275283]]"

np.corrcoef(zp,ks)

"array([[1.        , 0.88749009],"
"       [0.88749009, 1.        ]])"

df=pd.DataFrame(data={'zp':zp, 'ks':ks})
df

"zp	ks"
#0	35	401
#1	45	574
#2	190	874
#3	200	919
#4	40	459
#5	70	739
#6	54	653
#7	150	902
#8	120	746
#9	110	832

df.corr()


"zp	ks"
#zp	1.00000	0.88749
#ks	0.88749	1.00000

"Взаимосвязь между исходными данными сильная"

"задача 2"

arr=np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
print(f'Среднее выборочное: {np.mean(arr): .2f},\n'
      f'Размер выборки n={len(arr)},\n'
      f'Среднее квадратическое отклонение по выборке(несмещенное): {np.std(arr, ddof=1): .2f}.'
     )

#Среднее выборочное:  118.10,
#Размер выборки n=10,
#Среднее квадратическое отклонение по выборке(несмещенное):  10.55.

import scipy.stats as stats

def t_from_table(confidens, len_array):
    alpha=(1-confidens)
    return stats.t.ppf(1-alpha/2, len_array-1)
print(f'Табличное значение t-критерия для 95%-го доверительного интервала данной выборки: {t_from_table(0.95, len(arr)): .3f}')

#Табличное значение t-критерия для 95%-го доверительного интервала данной выборки:  2.262

def confidens_int(arr, confidens):
    return round(np.mean(arr)-t_from_table(confidens,len(arr))*np.std(arr, ddof=1)/len(arr)**0.5,3), \
           round(np.mean(arr)+t_from_table(confidens,len(arr))*np.std(arr, ddof=1)/len(arr)**0.5,3)

print(f'95%-й доверительный интервал для истинного значения IQ: {confidens_int(arr, 0.95)}.')

#95%-й доверительный интервал для истинного значения IQ: (110.556, 125.644).

"Задача 3"

left=174.2-(1.96*25**0.5)/27**0.5
right=174.2+(1.96*25**0.5)/27**0.5
print(f'95%-й доверительный интервал для оценки мат. ожидания генеральной совокупности: [{left: .4f};{right: .4f}].')

#95%-й доверительный интервал для оценки мат. ожидания генеральной совокупности: [ 172.3140; 176.0860].
