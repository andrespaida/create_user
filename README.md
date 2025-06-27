# Create User Microservice

This microservice handles the registration of new users in the ToyShop platform. It connects to a PostgreSQL database and stores user data securely, including password hashing.

## Technologies Used

- Python 3
- Flask
- psycopg2 (PostgreSQL driver)
- passlib (for password hashing)
- flasgger (Swagger integration)
- Docker
- GitHub Actions

## Getting Started

### Prerequisites

- Python >= 3.8
- PostgreSQL
- pip

### Installation

```bash
git clone https://github.com/andrespaida/create_user.git
cd create_user
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the root directory with the following content:

```env
PORT=3002
DB_HOST=your_postgres_host
DB_PORT=5432
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
DB_NAME=your_postgres_database
```

### Running the Service

```bash
python app.py
```

The service will be running at `http://localhost:3002`.

### API Documentation (Swagger)

Once the service is running, Swagger UI will be available at:

```
http://localhost:3002/apidocs
```

Use it to explore and test the API endpoints.

## Available Endpoint

### POST `/users`

Creates a new user and stores their information securely in the database.

#### Request body (JSON):

```json
{
  "name": "Admin",
  "email": "admin@example.com",
  "password": "your_password",
  "role": "admin"
}
```

#### Response (on success):

```json
{
  "message": "User created successfully"
}
```

## Docker

To build and run the service using Docker:

```bash
docker build -t create-user .
docker run -p 3002:3002 --env-file .env create-user
```

## GitHub Actions Deployment

This project includes a GitHub Actions workflow for automatic deployment to an EC2 instance. Make sure to configure the following secrets in your GitHub repository:

- `EC2_HOST`
- `EC2_USERNAME`
- `EC2_KEY`
- `EC2_PORT` (optional, defaults to 22)

## License

This project is licensed under the MIT License.