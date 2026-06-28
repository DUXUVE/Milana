import { createBrowserRouter } from "react-router"
import { RootLayout } from "./RootLayout"
import CatalogPage from "../pages/CatalogPage"

const router = createBrowserRouter([
    {
        id: 'root',
        path: '/',
        element: <RootLayout />,
        children: [
            {
                index: true,
                element: <CatalogPage />
            },
            {
                path: '/about',
                element: 
            }
        ]
    }
])

export default router