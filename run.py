from app.global_state import login_user
from app.wine_app import create_app

def main():
    """
    Entry point for the Rosa Negra application.
    
    This function creates an instance of the WineApp and starts the main event loop.
    """
    app = create_app()
    app.mainloop()

if __name__ == "__main__":
    login_user(18, 'kalebe@gmail.com', '1234', 'admin')	
    main()