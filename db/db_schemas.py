TABLES = {
    "users": """
        CREATE TABLE IF NOT EXISTS users (
            pk_user INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            dob DATE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            vat_number INTEGER,
            address_1 TEXT,
            address_2 TEXT,
            role TEXT NOT NULL
        );
    """,
    "wines": """
        CREATE TABLE IF NOT EXISTS wines(
            pk_wine INTEGER PRIMARY KEY,
            brand TEXT NOT NULL, 
            name TEXT NOT NULL,
            price REAL NOT NULL,
            type TEXT NOT NULL,
            alcohol REAL NOT NULL,
            year INTEGER NOT NULL,
            region TEXT NOT NULL,
            description TEXT NOT NULL
        );
    """,
    "stocks": """
        CREATE TABLE IF NOT EXISTS stocks(
            pk_stock INTEGER PRIMARY KEY,
            fk_wine INTEGER NOT NULL,
            movement TEXT CHECK(movement IN ('purchase', 'sale', 'adjustment')) NOT NULL,
            quantity INTEGER NOT NULL,
            fk_user INTEGER,
            reason TEXT,
            FOREIGN KEY(fk_wine) REFERENCES wine(pk_wine),
            FOREIGN KEY(fk_user) REFERENCES users(pk_user)
        );
    """,
    "purchases": """
        CREATE TABLE IF NOT EXISTS purchases(
            pk_purchase INTEGER PRIMARY KEY,
            fk_user INTEGER NOT NULL,
            total_value REAL NOT NULL,
            FOREIGN KEY(fk_user) REFERENCES users(pk_user)
        );
    """,
    "purchase_items": """
        CREATE TABLE IF NOT EXISTS purchase_items(
            pk_item INTEGER PRIMARY KEY,
            fk_purchase INTEGER NOT NULL,
            fk_wine INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY(fk_wine) REFERENCES wines(pk_wine),
            FOREIGN KEY(fk_purchase) REFERENCES purchases(pk_purchase)
        );
    """
}
