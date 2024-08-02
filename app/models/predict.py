import catboost
import os
from typing import List

class HealthPredict:

    @staticmethod
    def predict_risk(params: List):
        os.chdir('app/models')
        model = catboost.CatBoostClassifier()
        model.load_model('renders/Catboost1')
        return model.predict(params)
    
