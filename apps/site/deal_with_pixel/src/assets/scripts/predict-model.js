import { BASE_URL_API_MODEL } from '@/main';

export function getPredictModel(){
    let res = axios.get(`${BASE_URL_API_MODEL}predict-select-type`)
        .then(response => {
            return response.data;
        })
        .catch(response => {
            console.log(response.message);
            return [];
        })
        return res
}