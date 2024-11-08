# WordPress Plugin Backend Services

This repository contains the backend services for the WordPress Plugin MVP. It is built using FastAPI and integrates with various services to generate personalized emails for customers.

## Features

- **Email Generation**: Dynamically generate personalized emails using customer data and predefined templates.
- **Integration with Google Cloud AI**: Utilize Google Cloud's Vertex AI for generating email content.
- **Asynchronous Operations**: Leverage Python's `asyncio` for non-blocking operations.
- **MongoDB Integration**: Use Motor, an async MongoDB client, for database operations.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kundannanubala/wordpress-plugin.git
   cd wordpress-plugin-backend
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add the necessary environment variables as specified in `core/config.py`.

5. **Run the application**:
   ```bash
   uvicorn app:app --reload
   ```

## API Endpoints

- **Generate Email**: `POST /email/generate-email`
  - Request Body: JSON object containing customer and email data.
  - Response: JSON object with the generated email content.

## Project Structure

- **`api/`**: Contains the FastAPI router for email generation.
- **`services/`**: Business logic for email generation and integration with external services.
- **`models/`**: Pydantic models for request validation.
- **`core/`**: Configuration and settings management.
- **`app.py`**: Entry point for the FastAPI application.

## Usage

To generate an email, send a POST request to the `/email/generate-email` endpoint with a JSON body containing the necessary customer data. The service will return a JSON object with the generated email content.
make use of the services\samplejson.json file to test the endpoint.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Contact

For any questions or support, please contact [kundannanubala@gmail.com].