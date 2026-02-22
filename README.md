# FastAPI Secure Auth

A secure authentication system built with FastAPI, featuring user management, JWT token-based authentication, and database integration.

## Features

- **User Authentication**: JWT-based token authentication
- **User Management**: Create and manage users
- **Password Security**: Secure password hashing and verification
- **Database Integration**: SQLAlchemy ORM with database session management
- **Role-Based Access**: Core security and dependencies for access control
- **API Routing**: Organized routing for auth and user endpoints

## Requirements

- Python 3.8+
- FastAPI
- SQLAlchemy
- Pydantic
- python-jose (for JWT tokens)
- passlib (for password hashing)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/s33m0/FastAPI-Secure-Auth.git
cd FastAPI-Secure-Auth
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```bash
cp .env.example .env  # if available, or create manually
```

## Environment Configuration

All sensitive and environment-specific variables are stored in a `.env` file instead of being hardcoded in the source code.

This includes:
- Database connection URL
- Secret keys
- JWT configuration
- API keys
- Debug mode

The application loads these variables through the configuration module using Pydantic `BaseSettings`.

For development, copy `.env.example` to `.env` and provide your own values.

> ⚠️ The `.env` file is excluded from version control for security reasons.

## Project Structure

```
app/
├── auth/              # Authentication routes and services
│   ├── router.py
│   ├── schemas.py
│   └── services.py
├── users/             # User management routes and services
│   ├── model.py
│   ├── router.py
│   ├── schemas.py
│   └── services.py
├── core/              # Core configuration and security
│   ├── config.py
│   ├── dependencies.py
│   └── security.py
├── database/          # Database configuration
│   ├── base.py
│   ├── session.py
│   └── __init__.py
└── main.py            # Application entry point
```

## Usage

1. Start the development server:
```bash
uvicorn app.main:app --reload
```

2. Access the API documentation:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## API Endpoints

### Authentication
- `POST /auth/login` - Login and get access token
- `POST /auth/register` - Register a new user

### Users
- `GET /users` - List all users
- `GET /users/{user_id}` - Get user details
- `PUT /users/{user_id}` - Update user
- `DELETE /users/{user_id}` - Delete user

## Configuration

Configuration is managed in `app/core/config.py`. Update settings as needed for your environment.

## Database

The application uses SQLAlchemy ORM for database operations. Configure your database connection in the `.env` file or `config.py`.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions, please open an issue on the [GitHub repository](https://github.com/s33m0/FastAPI-Secure-Auth/issues).
