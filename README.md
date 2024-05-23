# Bellman AI

## Project Overview

Bellman is a one-stop source for AI news. It functions as a news digest, pulling articles from trusted sources and curating them with AI as the central topic. It processes the article content, summarizes it, and provides key takeaways and detailed explanations through a chat interface.

```
+---------------------+
|     Web Browser     |
+---------------------+
            |
            | Streamlit App
            |
+---------------------+
|       Streamlit     |
|        Server       |
+---------------------+
            |
            |
+---------------------+
|   Snowflake Cortex  |
|   (Language Models) |
|                     |
| - Summarization     |
| - Classification    |
| - Chat              |
+---------------------+
            |
            |
+------------------------+
|      Snowflake Cloud   |
|         Database       |
|                        |
| - Article Data         |
| - User Preferences(TBD)|
+------------------------+
            |
            |
+---------------------+
|   News API Sources  |
+---------------------+
```

### Technologies/libraries used

- Python
- Streamlit library (including experimental components like dialog boxes)
- Snowflake Arctic family models (4K context window model for summarization and chat, snowflake-arctic-embed-m embeddings model for classification)
- Snowflake Cortex
- Snowpark library
- Snowflake Cloud interface

## Installation & Usage

1. Prepare virtual environment using tools like conda or venv.

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the app

```
python -m streamlit run app.py
```

## Methodology

### Approach and techniques used

Used Streamlit for building the application interface
Leveraged Snowflake Arctic family models for summarization, chat, and classification functionalities
Interacted with Snowflake models through Snowflake Cortex and Snowpark library
Implemented category filtering and card detail view with summary and insights

### Data preprocessing steps

Pulled articles from a pool of trusted sources
Processed article content using Snowflake models for summarization and classification

### Deployment

Streamlit community cloud was used for deployment

## Why Bellman AI?

Keeping up with the influx of new terms, products, and companies in the rapidly evolving AI landscape can be overwhelming. Bellman aims to provide users with a comprehensive overview of the AI landscape, helping them stay updated with the latest trends with minimal stress.

## Results

![Alt Text](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/901/318/datas/original.png)

## Contributors

Yumi Ko: Worked on project ideation, development plan, front-end development, database connection module, and app deployment.

Anthony Santana: Worked on app design, front-end development, API integration, and prompt engineering.
