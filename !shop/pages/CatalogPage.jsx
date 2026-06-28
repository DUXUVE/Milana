import products from "./products"

function CatalogPage() {
    return <div>
        Товары
        <ul>{products.map((product) => (
            <li><article>
                {product.title}
            </article></li>
        ))}
        </ul>
        </div>
}

export default CatalogPage