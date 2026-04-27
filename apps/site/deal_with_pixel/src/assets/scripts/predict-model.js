import axios from 'axios';
import { BASE_URL_API_MODEL } from '@/main';

export function getPredictModel(type_image, image_file){
    let formData = new FormData()
    formData.append('type_image', type_image)
    formData.append('image', image_file)
    let res = axios.post(`${BASE_URL_API_MODEL}predict-select-type`, formData, { headers: {'Content-Type': 'multipart/form-data' }})
        .then(response => {
            return response.data;
        })
        .catch(response => {
            console.log(response.message);
            return '';
        })
    return res
}