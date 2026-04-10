import axios from 'axios';
import { BASE_URL_API_DB } from '@/main';

export function getTopics() {
    let res = axios.get(`${BASE_URL_API_DB}topics`)
    .then(response => {
        return response.data;
    })
    .catch(response => {
        console.log(response.message);
        return [];
    })
    return res
}