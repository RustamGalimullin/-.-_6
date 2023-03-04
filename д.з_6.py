#задача 1

import numpy as np
import scipy.stats as stats

l_border=80-1.96*16/256**0.5
r_border=80+1.96*16/256**0.5
print(f'>>> Доверительный интервал: [{l_border} ; {r_border}].')

"Ответ: Доверительный интервал: [78.04 ; 81.96]."

#Задача 2


array = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
n = len(array)
x = np.mean(array)
print(f'>>> Среднее арифметическое для выборки: {x}')
a = 0.05
sigma = np.std(array, ddof=1)
print(f'>>> Среднее квадратическое отклонение по выборке(несмещенное): {sigma}')
stats = stats.t.ppf( 1-a/2, n-1)
print(f'>>> Значение t-критерия для {1-a}% доверительного интервала: {stats}')
l_border=x-stats*sigma/np.sqrt(n)
r_border=x+stats*sigma/np.sqrt(n)
print(f'>>> Доверительный интервал для величины "X" составляет: [{l_border:.3f} ; {r_border:.3f}]')

"Среднее арифметическое для выборки: 6.590000000000001"
"Среднее квадратическое отклонение по выборке(несмещенное): 0.4508017549014448"
"Значение t-критерия для 0.95% доверительного интервала: 2.2621571627409915"
"Доверительный интервал для величины X составляет: [6.268 ; 6.912]"

#Задача3

mothers = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
daughters = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])

difference_of_means = np.mean(mothers) - np.mean(daughters)
standard_error = np.sqrt(np.var(mothers, ddof=1)/len(mothers) + np.var(daughters, ddof=1)/len(daughters))
t_critical = stats.t.ppf(0.975, len(mothers) + len(daughters) - 2)
l_border = difference_of_means - t_critical * standard_error
r_border = difference_of_means + t_critical * standard_error

print(f'>>> 95% доверительный интервал для разности среднего роста родителей и детей: [{l_border:.2f}, {r_border:.2f}]')

"Ответ: 95% доверительный интервал для разности среднего роста родителей и детей: [-6.27, 10.07]"

