import { Link, NavLink, Outlet } from "react-router";
import "./RootLayout.css"

function RootLayout() {
    return (
        <div className="app-shell">
            <header className="topbar">
                <Link className="brand" to="/">
                    ThreadLine
                </Link>
                <nav className="nav-links" aria-label="Primary navigation">
                    <NavLink 
                        className={(o)  => `${o.isPending ? "pending": ""} ${o.isActive ? "active": ""} nav-link`} 
                        to="/">
                        Catalog
                    </NavLink>
                    <NavLink 
                        className={(o)  => `${o.isPending ? "pending": ""} ${o.isActive ? "active": ""} nav-link`} 
                        to="/about">
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