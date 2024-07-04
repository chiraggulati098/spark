# SPARK: Summarize, Paraphrase and Rewrite Knowledge

SPARK is an end-to-end text processing application designed to simplify and enhance text manipulation tasks. Using SOTA technologies, SPARK provides functionalities for summarizing, paraphrasing, and translating text through an intuitive Streamlit interface.

## Features

- **Summarization**: Quickly generate concise summaries of long text passages.
- **Paraphrasing**: Rewrite text with a different wording while retaining the original meaning.
- **Translation**: Translate text between multiple languages.

## Technologies Used

- **Streamlit**: For creating the frontend interface.
- **txtai**: For text summarization.
- **Hugging Face Transformers**: For text paraphrasing using the Pegasus model.
- **Deep Translator**: For translating text between different languages.

## Project Structure

```
project/
├── .gitignore
├── README.md
├── app.py
├── requirements.txt
└── notebooks/
└── exploration.ipynb
```

## Installation

### Prerequisites
- Python 3.7+
- pip

### Clone the Repository
```bash
git clone https://github.com/your-username/SPARK.git
cd SPARK
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Running the Application
```bash
streamlit run app.py
```

## Future Enhancements
- Add slider to choose size of summary being generated.
- Add options to change intensity of paraphrasing.
- Improve model performance and accuracy.

---

This project was made by Chirag with ❤️
