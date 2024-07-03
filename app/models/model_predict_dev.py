import catboost
import os

os.chdir('app/models')

gender = 1
age = 20
race = 1
country = 1
in_us = 3
educ = 2
marital = 1
preg = 0
family_pov = 0.9
cal = 2000
prot = 25
carb = 378
sugr = 150
fibre = 40
chol = 22
bmi = 23
bpxs = 120
bpxd = 80
alq = 1
smk = 1
sld = 5
mhds = 1

feat = [gender, age, race, country, in_us, educ, marital, preg, family_pov,
    cal, prot, carb, sugr, fibre, chol, bmi, bpxs, bpxd, alq, smk, sld, mhds]

model = catboost.CatBoostClassifier()
model.load_model('model_prod/Catboost1')

value = model.predict(feat)

print(value)

