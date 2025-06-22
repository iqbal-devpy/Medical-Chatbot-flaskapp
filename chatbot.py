from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import spacy
import logging

logging.basicConfig(filename='chatbot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

nlp = spacy.load("en_core_web_md")

def load_medical_terms(file_path):
    try:
        with open(file_path, 'r') as file:
            return [nlp(line.strip()) for line in file.readlines() if line.strip()]
    except Exception as e:
        logging.error(f"Error loading medical terms: {e}")
        return []

core_terms = load_medical_terms('medical_term.txt')

template = '''
You are a knowledgeable medical assistant AI. Follow these rules:
- Avoid diagnosing or prescribing medication.
- Recommend seeking professional medical advice.
- Provide general health information.
- Be empathetic and respectful.

Conversation:
{context}

User: {question}

Response:
'''

model = OllamaLLM(model='gemma:2B')
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def is_medical_question(user_input, threshold=0.4):
    user_doc = nlp(user_input.lower())
    for term_doc in core_terms:
        if user_doc.similarity(term_doc) > threshold:
            return True
    return False

def update_context(context, user_input, response, max_turns=5):
    context_lines = context.strip().split('\n')[-2 * max_turns:] if context else []
    return '\n'.join(context_lines + [f"User: {user_input}", f"AI: {response}"])


context = ""

def handle_chat(user_input):  # Accept user_input as an argument
    global context
    if not user_input.strip():
        return "Please enter a valid message."

    if is_medical_question(user_input):
        try:
            response = chain.invoke({'context': context, 'question': user_input}).strip()
        except Exception as e:
            logging.error(f"Error in chatbot response: {e}")
            response = "I'm sorry, I encountered an issue. Please try again later."
    else:
        response = "This doesn't seem like a medical-related question. Please ask about health."

    context = update_context(context, user_input, response)
    return response
