import config from "../config";

const _apiUrl = config.apiUrl + '/products'

const productsApi = {
    async getAll() {
        const response = await fetch(_apiUrl);
        
        const data = await response.json();
        
        return data;
    },
    async get(id) {
        const response = await fetch(_apiUrl + `/${id}`);
        
        const data = await response.json();
        
        return data;
    }
};

export default productsApi;