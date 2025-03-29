# User Management App

This project is a web application designed to manage users through a visually appealing interface. It allows users to add, update, list, and delete user information.

## Project Structure

```
user-management-app
├── static
│   ├── css
│   │   └── style.css        # Styles for the web application
│   └── js
│       └── main.js          # JavaScript for handling user interactions
├── templates
│   ├── base.html            # Base template for the web application
│   └── index.html           # Main HTML template for user management
├── app.py                   # Main application file
├── database.py              # Database interaction functions
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

## Getting Started

### Prerequisites

Make sure you have Python installed on your machine. You will also need to install the required packages listed in `requirements.txt`.

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd user-management-app
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

To start the web application, run the following command:
```
python app.py
```

The application will be accessible at `http://127.0.0.1:5000`.

### Usage

- Use the interface to add new users, view the list of existing users, update user information, or delete users.
- Follow the prompts on the web page to interact with the application.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

<!-- cd user-management-app
pip install -r requirements.txt
python app.py -->