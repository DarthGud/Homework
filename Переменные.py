from builtins import PythonFinalizationError

kolichestvo_rabot = 12
kolichestvo_chasov = 1.5
name_kurs = 'Python'
vremya_zadanya = kolichestvo_chasov / kolichestvo_rabot
print ('Курс:', name_kurs, ', всего задач:', kolichestvo_rabot, ', затрачено часов:', kolichestvo_chasov, ', среднее время выполнения', vremya_zadanya, 'часов.')