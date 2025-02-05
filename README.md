# Tweet-Sentiment-Analysis


This project analyzes the sentiment of tweets using a deep learning model. The backend is built with FastAPI, and the frontend is built with Streamlit.

## Setup

1. Clone the repository.
2. Run `docker-compose up` to start the backend and frontend services.
3. Access the Streamlit app at `http://localhost:8501`.

## API Documentation

The FastAPI backend provides a `/predict/` endpoint to analyze the sentiment of a given text.

## Tests

Run the unit tests with:

```bash
cd backend
pytest tests/