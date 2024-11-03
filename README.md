# Multilingual Translator

This is a simple web application built with Streamlit that allows users to translate text between multiple languages using pre-trained models from Hugging Face's Transformers library.

## Features

- Supports translation between:
  - English and Spanish
  - Spanish and English
  - French and English
  - English and French
  - German and English
  - English and German
- Saves translations to a text file (`translations.txt`).
- Logs user actions and errors to a log file (`log.txt`).
- User feedback on translation usefulness.

## Requirements

To run this application, you need to have Python installed along with the following libraries:

- Streamlit
- Transformers
- Logging
- Regex

You can install the required packages using pip:

```bash
pip install r requirements.txt
```

## Running the Application

1. Clone this repository or download the script.
2. Navigate to the directory containing the script.
3. Run the Streamlit application using the following command:

```bash
streamlit run translator_app.py
```

4. Open the URL provided in your terminal (usually `http://localhost:8501`).

## Usage

1. Select the desired translation language from the dropdown menu.
2. Enter the text you want to translate (up to 500 characters).
3. Click the "Translate" button.
4. The translated text will be displayed, and you can choose to save it or provide feedback.

## Logging

The application logs user interactions and any errors that occur during the translation process. You can check `log.txt` for this information.
