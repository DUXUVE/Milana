import { Link, useLoaderData } from "react-router"

function CatalogPage() {
    const products = useLoaderData();
    return <div>
        Товары
        <ul>{products.map((product) => (
            <li key={product.id}><Link to={`/products/${product.id}`}>
                <article>
                    <img src={product.image} alt="картинка товара"/>
                    <span>{product.title}</span>
                    <span>{product.price}</span>
                </article></Link>
            </li>
        )
            )}</ul>
    </div>
}

export default CatalogPage