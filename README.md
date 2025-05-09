Collecting workspace information# FastAPI CI/CD Demo Project

This is a simple FastAPI application to demonstrate CI/CD practices. The project includes a basic API with two endpoints.

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd ci-cd
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the virtual environment:

```bash
# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the application using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at http://127.0.0.1:8000

## API Documentation

The API documentation is automatically generated and can be accessed at:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

### Endpoints

- `GET /`: Returns a welcome message
- `GET /items/{item_id}`: Returns an item by its ID with an optional query parameter `q`

## CI/CD Demo

This project serves as a playground for implementing CI/CD practices:

- Continuous Integration: Automated testing on each commit
- Continuous Deployment: Automatic deployment to staging/production environments
- Infrastructure as Code: Defining deployment environments
- Automated Testing: Unit and integration tests

## Next Steps

1. Add tests for the API endpoints
2. Configure a CI/CD pipeline (GitHub Actions, Jenkins, etc.)
3. Set up automatic deployment to a cloud provider
4. Add monitoring and logging
