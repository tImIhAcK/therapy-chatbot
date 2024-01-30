# Therapy Chabot

### Overview

The Therapy Chatbot is an AI-driven conversational tool designed to provide support and guidance in a therapeutic context. It utilizes LangChain's natural language processing capabilities to engage users in meaningful conversations, offering empathetic responses and valuable insights.

### How to Run

1. Clone this repository:

```
git clone https://github.com/tImIhAcK/therapy-chatbot.git
```

2. Navigate to the project directory:

```
cd therapy-chatbot
```

3. Create a virtual environment and activate:

```
python -m venv <venv_name>
```

On Windows:

```
<venv_name>\Scripts\activate
```

on linux:

```
source <venv_name>/bin/activate
```

Replace `<venv_name>` with your environment name

4. Create a .env file:

```
OPENAI_API_KEY='your_api_key'
```

5. Install dependencies:

```
pip install -r requirements.txt
```

Replace `your_api_key` with your api from openai

6. Run the application:

```
streamlit run app.py
```

7. Access the application in your browser at http://localhost:8501.
