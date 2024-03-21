# Currency Exchange API

## Overview

This project provides a simple and efficient API for querying currency exchange rates and performing currency conversions. The API is designed to be easy to use, with straightforward endpoints for retrieving exchange rates and converting currency values.

## Features

- [x] Retrieve currencies
- [x] Register currencies
- [x] Retrieve currency by name
- [x] Retrieve currency by ID
- [x] Ensure test coverage reaches 80% to guarantee robustness and reliability ([Sonar](https://sonarcloud.io/summary/new_code?id=murilohenzo_currency-exchange-rate)).

## Architecture

### Hexagonal Architecture

The **Hexagonal Architecture** is a software design model that promotes the isolation of domain logic, located in the inner (business core), from external factors. Communication with domain logic occurs through ports and adapters, ensuring a clear separation between the internal and external parts of the application.

#### Components of Hexagonal Architecture:

1. **Application Layer:**
   - Interface through which users and other programs interact with the application.
   - Includes elements such as user interfaces, RESTful controllers, and JSON serialization libraries.
   - Responsible for exposing the entry point in the application and orchestrating the execution of domain logic.

2. **Domain Layer:**
   - Contains the code that implements the business logic, serving as the core of the application.
   - Isolated from application and infrastructure parts.
   - Includes interfaces that define the API for communication with external parts, such as a database.

3. **Infrastructure Layer:**
   - Contains all the resources necessary for the application to function.
   - Includes database configuration, Spring configuration, and implementations of infrastructure-dependent interfaces from the domain layer.

![hexagonal_architecture](https://github.com/murilohenzo/mono-to-micro/assets/28688721/467e9210-2584-4204-96e0-f4d8a36e9e78)

### Dependency Inversion in Repository Layer

In the infrastructure layer, we implement the principle of **Dependency Inversion** in the repository layer. This is achieved by creating an interface in the domain and a corresponding implementation in the infrastructure layer. This approach makes our domain service depend on abstractions, not specific implementations, making the code more flexible and adaptable to changes.

### Installation

To install the dependencies required for this project, use the following command:

```bash
pip install -r requirements.txt
```

### Usage

#### Step 1: Start MySQL Database

- Navigate to the `docker-compose` directory:

  ```bash
  cd docker-compose
  ```

- Start the MySQL database using Docker Compose:

  ```bash
  docker-compose up -d
  ```

#### Step 2: Run the Application

- Navigate back to the project root directory:

  ```bash
  python src/Application.py
  ```

### Run tests
- To run the tests with coverage

```bash	
  pytest --cov=src
```

- To generate test coverage report with html

```bash	
  pytest --cov=src --cov-report=html
```

### Retrieve Exchange Rates

```
GET /exchange-rates
```

This endpoint returns the latest exchange rates between different currencies.

### Convert Currency

```
GET /convert?from={source_currency}&to={target_currency}&amount={amount}
```

This endpoint converts a specified amount from one currency to another based on the provided exchange rates.

## Rate Limiting

To prevent abuse, this API implements rate limiting. Each user is allowed a certain number of requests within a specified time period. If the rate limit is exceeded, subsequent requests will be rejected until the rate limit period resets.

## Example

Retrieve exchange rates:

```
GET /exchange-rates
```

Response:

```json
{
  "USD": 1.0,
  "EUR": 0.87,
  "GBP": 0.75,
  ...
}
```

Convert currency:

```
GET /convert?from=USD&to=EUR&amount=100
```

Response:

```json
{
  "from": "USD",
  "to": "EUR",
  "amount": 100,
  "converted_amount": 87
}
```

## Contribution

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
