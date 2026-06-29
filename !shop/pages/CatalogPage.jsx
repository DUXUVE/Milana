import { Link } from "react-router"
import products from "./products" 
function CatalogPage() {
    return <div>
        Товары
        <ul>{products.map((product) => (
            <li><Link to={`/products/${product.id}`}>
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