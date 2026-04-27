import uvicorn
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from prediction_model import PredictTypeImage

app = FastAPI()
pti = PredictTypeImage()

origins = [
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/predict')
async def predict(image: UploadFile):
    return pti.predict_model(image.file)

@app.post('/predict-select-type')
async def predict(type_image: Annotated[str, Form()], image: UploadFile = File(...)):
    if not pti.check_class_name(type_image.capitalize()):
        return HTTPException(status_code=404, detail='Тип изображения не было найдено!')
    return pti.predict_select_type_image(type_image.capitalize(), image.file)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5555)