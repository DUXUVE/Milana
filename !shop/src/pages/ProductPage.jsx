import { useLoaderData } from "react-router"

function ProductPage() {
    const product = useLoaderData();

    return <div>
        <img src={product.image} alt="картинка товара"/>
        <span>{product.title}</span>
        <span>{product.price}</span>
    </div>
}

export default ProductPage