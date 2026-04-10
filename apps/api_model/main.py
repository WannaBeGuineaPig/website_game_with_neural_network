import uvicorn
from fastapi import FastAPI, UploadFile, HTTPException
from prediction_model import PredictTypeImage

app = FastAPI()
ptp = PredictTypeImage()

@app.post('/predict')
async def predict(image: UploadFile):
    return ptp.predict_model(image.file)

@app.post('/predict-select-type')
async def predict(type_image: str, image: UploadFile):
    if not ptp.check_class_name(type_image):
        return HTTPException(status_code=404, detail='Тип изображения не было найдено!')
    return ptp.predict_select_type_image(type_image, image.file)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5555)