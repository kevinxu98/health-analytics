import catboost
import os

class HealthPredict:

    def __init__(self):
        pass

    def predict(self, feat):
        os.chdir('app/models')
        self.model = catboost.CatBoostClassifier()
        self.model.load_model('model_prod/Catboost1')
        return self.model.predict(feat)
    

obj_1 = HealthPredict()
print(obj_1.predict([1, 20, 1, 1, 3, 2, 1, 0, 0.9, 2000, 25, 378, 150, 40, 22, 23, 120, 80, 1, 1, 5, 1]))