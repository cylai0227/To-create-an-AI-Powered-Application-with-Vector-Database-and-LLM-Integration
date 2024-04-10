# To-create-an-AI-Powered-Application-with-Vector-Database-and-LLM-Integration  

This repository contains code for a Semantic Search Engine built using Streamlit and OpenAI's GPT (Generative Pre-trained Transformer) model. The application allows users to input a natural language query, which is then used to search through a collection of academic papers. The relevance of each paper to the query is determined using OpenAI's GPT model.  

# How it Works  
**User Interface**   
The user interface is developed using Streamlit, a Python library for building interactive web applications.  
Users can input their queries in natural language through a text input field.  
Upon clicking the "Search" button, the application initiates the search process.  

**Backend Logic**  
The application utilizes a collection of dummy academic papers, each represented by a title, authors, and an abstract.  
For each paper in the collection, the abstract is combined with the user's query to form a prompt.  
This prompt is then passed to OpenAI's GPT model for semantic analysis.  
The model generates a relevance score (logit) indicating the likelihood of the paper being relevant to the query.  
The search results are sorted based on the relevance scores, and the top three results are displayed to the user.  

**Dependencies**  
Streamlit: Used for building the user interface.  
OpenAI Python Library: Utilized for interfacing with OpenAI's GPT model.  

**Usage**  
Clone the repository to your local machine.  
Install the required dependencies using **pip install -r requirements.txt**  
Set up your OpenAI API key in the code.  
Run the application using **streamlit run search_engine_research_paper.py**  
Input your query and click the "Search" button to see the search results.  
