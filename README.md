# GEN_AI_MCQs_generator with Streamlit

This web-based MCQ Generator allows users to upload text or PDF documents and automatically generate multiple-choice questions (MCQs) based on the content. Users can customize the number of questions, choose a subject, and set the tone. The app leverages OpenAI’s language models for natural language processing and provides feedback on quiz complexity.

## Key Features
- **Document Upload**: Supports PDF and text file uploads for question generation.

- **Customizable Inputs**: Users can define the number of questions, select a subject, and choose the desired tone.

-**Instant Feedback**: Offers real-time insights into the difficulty level of the quiz and provides suggestions for improvement.

- **Structured Output**: Presents the generated MCQs in a clean, tabular format for better clarity.

## Requirements
- Python 3.x

- Streamlit

- Langchain

- OpenAI API Key

## Setup Instructions
1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/mcq-generator-streamlit.git
    ```

2. Install the necessary packages:
  ```bash
    pip install -r requirements.txt
  ```
3. Configure environment variables:

Create a .env file in the project’s root directory.

Add your OpenAI API key:
  ```plaintext
        OPEN_AI_KEY=your-openai-api-key
   ```
4. Install the package locally:
 ```bash
    python setup.py install
 ```
## How to Use
1. Launch the Streamlit app:
 ```bash
    streamlit run main.py
 ```

2.Open the app in your browser.

3.Upload a file, set your preferences (number of questions, subject, tone), and click “Create MCQs.”

4.Review the generated questions along with the complexity analysis.

Logging Details
Logs are saved in the logs folder.

Each log file is timestamped for easy tracking.
