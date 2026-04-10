from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np, pandas as pd

__all__ = [
    'PredictTypeImage'
]

URL_MODEL = './model/model_СNN.keras'
URL_CLASS_NAMES = './model/class_names.txt'
SIZE_IMAGE = (224, 224)


class PredictTypeImage:
    def __init__(self):
        self.model =  self.load_model_type_image()
        self.class_names =  self.load_class_names()
        self.russian_class_names = {
            'cat' : 'Кот',
            'dog' : 'Собака',
            'cow' : 'Корова',
            'panda' : 'Панда',
            'ant' : 'Муравей',
            'fish' : 'Рыба',
            'airplane' : 'Самолёт',
            'bicycle' : 'Велосипед',
            'car' : 'Машина',
            'helicopter' : 'Вертолёт',
            'circle' : 'Круг',
            'square' : 'Квадрат',
            'hexagon' : 'Шестиугольник',
            'triangle' : 'Треугольник',
        }

    def load_model_type_image(self):
        return load_model(URL_MODEL, compile=False)
    
    def load_class_names(self):
        with open(URL_CLASS_NAMES, 'r') as file:
            return file.read().split(',')

    def create_data_to_predict(self, file):
        image = Image.open(file) 
        image = ImageOps.fit(image, SIZE_IMAGE).convert('L')
        image_array = np.asarray(image, dtype=np.float32) / 255
        return np.asarray([image_array], dtype=np.float32)

    def check_class_name(self, type_image: str) -> bool:
        return type_image in self.class_names

    def predict_model(self, file):
        data = self.create_data_to_predict(file)
        prediction = self.model.predict(data)
        return pd.DataFrame({
            'Классы' : self.class_names,
            'Процент схожести' : [float(pred) for pred in prediction[0]]
        }).sort_values(by=['Процент схожести'], ascending=False)

    def predict_select_type_image(self, type_image: str, file):
        data = self.create_data_to_predict(file)
        prediction = self.model.predict(data)[0]
        percent_select_type = round(float(prediction[self.class_names.index(type_image)]), 5)
        select_type_pred = f'Схожесть c «{self.russian_class_names[type_image]}» на {percent_select_type}%'
        max_pred = round(float(prediction[np.argmax(prediction)]), 5)
        max_type_pred = f'Максимальная схожесть - «{self.russian_class_names[self.class_names[np.argmax(prediction)]]}» на {max_pred}%'
        return select_type_pred + '\n' + max_type_pred
