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
        self.russian_class_names = [
            'Кот', 
            'Собака', 
            'Корова', 
            'Панда',
            'Муравей',
            'Рыба',
            'Самолёт',
            'Велосипед',
            'Машина',
            'Вертолёт',
            'Круг',
            'Квадрат',
            'Шестиугольник',
            'Треугольник',
        ]

    def load_model_type_image(self):
        return load_model(URL_MODEL, compile=False)
    
    def load_class_names(self):
        with open(URL_CLASS_NAMES, 'r') as file:
            return file.read().split(',')

    def create_data_to_predict(self, file):
        image = Image.open(file)
        image_bg = Image.new("RGB", image.size, (255, 255, 255))
        image_bg.paste(image, mask=image)
        image_bg = ImageOps.fit(image_bg, SIZE_IMAGE, Image.Resampling.LANCZOS).convert('L')
        image_array = np.asarray(image_bg, dtype=np.float32) / 255
        return np.asarray([image_array], dtype=np.float32)

    def check_class_name(self, type_image: str) -> bool:
        return type_image in self.russian_class_names

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
        percent_select_type = round(float(prediction[self.russian_class_names.index(type_image)]) * 100, 5)
        max_pred_type = round(float(prediction[np.argmax(prediction)]) * 100, 5)
        return f'Схожесть c типом «{type_image}» на {percent_select_type}%\nМаксимальная схожесть с типом «{self.russian_class_names[np.argmax(prediction)]}» на {max_pred_type}%'
