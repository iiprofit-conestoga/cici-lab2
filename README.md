# Calculator API

A simple Flask-based Calculator API with Docker support and CI/CD pipeline using GitHub Actions.

## Project Structure 

```
calculator-api/
├── app.py              # Main Flask application
├── test_app.py         # Test cases
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker image configuration
├── docker-compose.yml # Docker compose configuration
└── .github/
    └── workflows/
        └── ci.yml     # GitHub Actions CI/CD pipeline
```

## Features

- RESTful API endpoints for basic calculator operations
- Docker containerization
- Automated testing
- CI/CD pipeline with GitHub Actions
- Automatic Docker image publishing

## API Endpoints

- `GET /` - Welcome message
- `GET /add/<num1>/<num2>` - Add two numbers
- `GET /subtract/<num1>/<num2>` - Subtract second number from first
- `GET /multiply/<num1>/<num2>` - Multiply two numbers
- `GET /divide/<num1>/<num2>` - Divide first number by second

## Local Development

### Prerequisites

- Python 3.9+
- pip
- Docker and Docker Compose

### Setting Up Development Environment

1. Clone the repository:
```bash
git clone https://github.com/yourusername/calculator-api.git
cd calculator-api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Running Tests

```bash
pytest
```

## Docker Support

### Running with Docker Compose

1. Pull and run the application using Docker Compose:
```bash
docker-compose up
```

The application will be available at `http://localhost:5000`

### Manual Docker Commands

1. Build the Docker image:
```bash
docker build -t calculator-api .
```

2. Run the container:
```bash
docker run -p 5000:5000 calculator-api
```

## Using the Published Docker Image

You can directly pull and run the latest version from Docker Hub:

```bash
docker pull iiprofit/calculator-api:latest
docker run -p 5000:5000 iiprofit/calculator-api:latest
```

## CI/CD Pipeline

The project uses GitHub Actions for CI/CD pipeline, which:
- Runs on push and pull requests to the development branch
- Installs dependencies
- Runs tests
- Builds and pushes Docker image to Docker Hub (on successful push to development)

### Pipeline Status
- The pipeline fails if any test fails
- Docker image is only pushed on successful test completion

### Required GitHub Secrets

For the CI/CD pipeline to work, set these secrets in your GitHub repository:
- `DOCKER_HUB_USERNAME`: Your Docker Hub username
- `DOCKER_HUB_TOKEN`: Your Docker Hub access token

## Testing the API

You can test the API using curl:

```bash
# Test welcome message
curl http://localhost:5000/

# Test addition
curl http://localhost:5000/add/5/3

# Test multiplication
curl http://localhost:5000/multiply/4/5

# Test division
curl http://localhost:5000/divide/10/2
```

## Contributing

1. Create a new branch from development
2. Make your changes
3. Write or update tests
4. Create a pull request to the development branch

## License

[MIT License](LICENSE)



