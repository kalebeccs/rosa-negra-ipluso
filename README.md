# Rosa Negra

<img src="app/assets/icon.ico" width="170">

## Overview

Rosa Negra is a wine management application designed to help users explore and manage different categories of wines. The application provides a user-friendly interface to navigate through various sections such as product listings, cart, user profiles, and more.

## Features

- **Home Page**: Displays an introductory section with an image and text, followed by wine categories.
- **Product Page**: Lists all available wines with detailed information.
- **Cart Page**: Allows users to view and manage their selected wines.
- **Login and Register Pages**: Provides user authentication and registration functionalities.
- **Profile Page**: Displays user profile information.
- **Dashboard**: Admin dashboard for managing products, users, and purchases.
- **Product Management**: Allows admins to manage wine products.
- **User Management**: Allows admins to manage user accounts.
- **Purchase Management**: Allows admins to manage purchase orders.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/kalebeccs/rosa-negra-ipluso.git
   ```
2. Navigate to the project directory:
   ```sh
   cd rosa-negra
   ```
3. Create a virtual environment:
   ```sh
   python -m venv .venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```sh
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source .venv/bin/activate
     ```
5. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```sh
   python run.py
   ```
2. The application will start, and you can navigate through the different sections using the provided interface.

## Project Structure

```plaintext
rosa-negra-ipluso/
├── app/
│   ├── assets/
│   └── views/
├── db/
├── src/
│   ├── models/
│   └── utils/
├── README.md
├── requirements.txt
└── run.py
```
