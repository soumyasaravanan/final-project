from django.apps import AppConfig
from django.conf import settings
import os
import pickle

class AisentimentechnoverseConfig(AppConfig):
    name = "aisentimentechnoverse"
    path = os.path.join(settings.MODELS,"models.p")
    with open(path,"rb") as pickled:
        data = pickle.load(pickled)
    model = data['model']
    vectorizer = data['vectorizer']
