Medical Chatbot (Flask App)
A lightweight, yet powerful medical chatbot built with Flask, leveraging LangChain, Hugging Face, and Pinecone to provide semantic healthcare information through a user-friendly web interface.

🚀 Features

Medical Knowledge Base: Fetches and processes content from medical PDFs using PyPDFLoader. 


Text Embeddings: Utilizes sentence-transformer (e.g. LLaMA‑based) to generate contextual embeddings. 


Vector Search: Stores embeddings in Pinecone, enabling efficient semantic retrieval. 


Flask-powered Backend: Handles chat requests and orchestrates embedding and retrieval operations.

Interactive Chat UI: HTML/CSS frontend supporting real-time chat experience.

Modular Codebase: Includes scripts such as store_indexes.py for indexing, and app.py for serving the chat.

📦 Tech Stack

Layer	Technologies
Backend	Python, Flask, LangChain, Hugging Face Transformers
Embedding & Indexing	LLaMA embeddings via HuggingFaceEmbeddings, Pinecone DB
Frontend	HTML, CSS, JavaScript for clean chat UI
Infrastructure	Docker & docker-compose (optional setup)

📥 Installation

1. Clone the repository:


2. git clone https://github.com/iqbal-devpy/Medical-Chatbot-flaskapp.git
    cd Medical-Chatbot-flaskapp


3. Install dependencies:
pip install -r requirements.txt
Configure environment variables:
Create a .env file:


4. PINECONE_API_KEY=<your_key>
PINECONE_ENV=<env>
PINECONE_INDEX_NAME=<index_name>


5. python store_indexes.py
Launch the app:


6. python app.py
💬 Usage
Open the app in your browser (e.g., http://127.0.0.1:5000/).

Ask medical-related questions via chat interface.

The chatbot fetches semantically matched information from its embedded PDF knowledge base and displays relevant responses.

🛡️ Considerations & Best Practices

    Medical Disclaimer: Not intended for clinical diagnosis—include a clear disclaimer.

    Privacy & Security: Ensure proper handling of user input and vector data.

    Model Adaptation: Potential to replace embeddings model with medical-specific ones for enhanced accuracy.

    Frontend Enhancements: Possibility to support voice interaction or richer UI/UX.



🔗 About
A demonstration of how LangChain, LLaMA-style embeddings, and Pinecone can power an accessible medical chatbot via Flask.

