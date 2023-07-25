# Perplexity API

Perplexity API is a high-performance FastAPI backend application designed to seamlessly integrate with vector databases, LangChain, HuggingFace, and OpenAI. It uses an OpenAPI spec and Swagger utilizing JSON Schema to provide a robust and scalable backend solution for AI and machine learning applications. 

## Features

- **FastAPI Backend**: Offers a high-performance backend solution that incorporates modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

- **Vector Database Integration**: Seamlessly connects with vector databases to ensure efficient data storage and retrieval, which is crucial in handling high-dimensional data vectors.

- **LangChain Integration**: Incorporates LangChain for comprehensive language processing capabilities, helping to effectively understand, analyze, and generate human language data.

- **HuggingFace & OpenAI Integration**: By integrating state-of-the-art AI platforms like HuggingFace and OpenAI, Perplexity API allows leveraging their extensive capabilities in machine learning and artificial intelligence.

- **Swagger Compatibility**: Supports Swagger, a powerful interface for REST APIs that allows both developers and non-developers to interact with the API’s resources. It provides insightful information about the operations, parameters, responses, and the direct testing of API endpoints within its UI.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You'll need to install the following items before you can use Perplexity API:

- Python 3.6 or later
- Poetry (Python dependency management)
- Docker (for containerization)

### Installation

Clone the repository:
```bash
git clone https://github.com/bastosmichael/perplexity.git
```

Navigate to the project directory:
```bash
cd perplexity
```

Install the required dependencies using Poetry:
```bash
poetry install
```

Run the application:
```bash
poetry run uvicorn main:app --reload
```

The server should be running and the API can be accessed at `localhost:8000`.

### API Documentation

The API documentation can be viewed at `localhost:8000/docs` when the server is running. The documentation is interactive, so you can test out API calls directly in your browser.

## Contributing

We welcome contributions to Perplexity API! Please see our [Contributing Guide](CONTRIBUTING.md) for more details.

## License

This project is licensed under the GNU General Public License v2.0 - see the [LICENSE](LICENSE.md) file for details.

## Contact

If you have any questions, feel free to reach out to us at [bastosmichael@gmail.com](mailto:bastosmichael@gmail.com).

## Acknowledgments

We would like to thank the creators and contributors of FastAPI, LangChain, HuggingFace, OpenAI, Swagger, and Poetry for their amazing tools that have helped make this project possible.
