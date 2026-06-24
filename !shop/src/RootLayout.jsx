import { useRouteLoaderData } from "react-router"

export function RootLayout() {

    return (
        <div className="app-shell">
            <header className="topbar">
                <link className="brand" to="/">
                    TreadLine
                </link>
            </header>
            <main> 
                <Outlet />
            </main>
        </div>
    )
}