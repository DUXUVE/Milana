import { createBrowserRouter } from "react-router";
import RootLayout from "./pages/RootLayout";
import CatalogPage from "./pages/CatalogPage";
import AboutPage from "./pages/AboutPage";
import ProductPage from "./pages/ProductPage";
import CartPage from "./pages/CartPage";
import productsApi from "./api/productsApi";
import cartsApi from "./api/cartsApi";


const router = createBrowserRouter([
    {
        id: 'root',
        path: '/',
        element: <RootLayout />,
        children: [
            {
                index: true,
                loader: productsApi.getAll,
                element: <CatalogPage />
            },
            {
                path: '/about',
                element: <AboutPage />,
            },
            {
                path: '/products/:id',
                loader: ({params}) => productsApi.get(params.id),
                element: <ProductPage />,
            },
            {
                path: '/cart',
                loader: cartsApi.get,
                element: <CartPage />,
            }
        ]
    }
])

export default router