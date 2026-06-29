import { createBrowserRouter } from "react-router";
import { RootLayout } from "../pages/RootLayout";
import CatalogPage from "../pages/CatalogPage";
import AboutPage from "../pages/AboutPage";

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
                element: <AboutPage />,
            }
        ]
    }
])

export default router