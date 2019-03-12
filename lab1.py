import pandas as pd
data = pd.read_csv('titanic.csv', index_col='PassengerId')
data['Pclass'] = data['Pclass'].astype(object)

# 1. Какое количество мужчин и женщин ехало на корабле? В качестве ответа приведите два числа через пробел.
sex_counts = data['Sex'].value_counts()
print("Ответ№1:" , '{} {}'.format(sex_counts['male'], sex_counts['female']))
# 2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
embarked_counts = data['Embarked'].value_counts()
print("Ответ№2:" , '{} {} {}'.format(embarked_counts['C'], embarked_counts['S'],embarked_counts['Q']))
# 3. Посчитайте долю погибших на параходе (число и процент)?
surv_counts = data['Survived'].value_counts()
surv_percent = 100.0 * surv_counts[0] / surv_counts.sum()
print("Ответ№3:", "{:0.2f}".format(surv_percent), surv_counts[0])
# 4. Какие доли составляли пассажиры первого, второго, третьего класса?
pclass_counts = data['Pclass'].value_counts()
pclass_percent1 = 100.0 * pclass_counts[1] / pclass_counts.sum()
pclass_percent2 = 100.0 * pclass_counts[2] / pclass_counts.sum()
pclass_percent3 = 100.0 * pclass_counts[3] / pclass_counts.sum()
print("Ответ№4:", "{:0.2f}".format(pclass_percent1), "{:0.2f}".format(pclass_percent2), "{:0.2f}".format(pclass_percent3))
# 5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
corr = data['SibSp'].corr(data['Parch'])
print("Ответ№5:", "{:0.2f}".format(corr))
# 7. Посчитайте средний возраст пассажиров и медиану.
