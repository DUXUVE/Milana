import sessionApi from "./sessionApi";

const cartsApi = {
    async get() {
        const response = await fetch(_apiUrl + `?sessionId=${sessionApi.getSessionId()}`);
        
        const data = await response.json();
        
        return data(0);
    },
    async addItem(product, quantity = 1) {
        const card = get();
        const foundProduct = card.products.find((p) => p.id === product.id)
        if (foundProduct) {
            foundProduct.quantity += quantity;
        } else {
            card.products.push({
                productId: product.id,
                quantity
            })
        }
        const response = await fetch(apiUrl + `/${card.id}`, {
            method: 'PUT',
            body: JSON.stringify(card)
        });
        return response.ok;
    }
}

export default cartsApi