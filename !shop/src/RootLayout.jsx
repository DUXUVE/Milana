import { useRouteLoaderData } from "react-router"
import "./RootLayout.css"

export function RootLayout() {

    return (
        <div className="app-shell">
            <header className="topbar">
                <link className="brand" to="/">
                    TreadLine
                </link>
                <nav className="nav-links" aria-label="Primary navigation">
                    <NavLink className = { (o) => `${o.isPending ? "pending": ""} ${o.isActive ? "active": ""}` } to="/">
                        Каталог
                    </NavLink>
                    <NavLink className = { (o) => `${o.isPending ? "pending": ""} ${o.isActive ? "active": ""}` } to="/about">
                        О компании
                    </NavLink>
                </nav>
            </header>
            <main> 
                <Outlet />
            </main>
        </div>
    )
} 

export default RootLayout