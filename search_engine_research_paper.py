import streamlit as st
import openai

# Set up your OpenAI API key
openai.api_key = "API_KEY"


# Dummy data
papers = [
    {"title": "Paper 1 Title", "authors": ["Author 1", "Author 2"], "abstract": "Abstract of Paper 1..."},
    {"title": "Paper 2 Title", "authors": ["Author 3", "Author 4"], "abstract": "Abstract of Paper 2..."},
    # Add more papers as needed
]

# Step 3: Application Development

## User Interface
st.title('Semantic Search Engine for Academic Literature')

query = st.text_input('Enter your query in natural language:')

if st.button('Search'):
    if query.strip() == "":
        st.warning("Please enter a query.")
    else:
        # Step 3: Backend Logic (Semantic Search using OpenAI's GPT)
        search_results = []

        # Loop through papers
        for paper in papers:
            abstract = paper['abstract']
            
            # Construct prompt by concatenating query and abstract
            prompt = f"Query: {query}\nAbstract: {abstract}\nIs this paper relevant to the query?"
            
            # Generate text using OpenAI's GPT model
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",  # Use the latest Davinci Beta model
                prompt=prompt,
                max_tokens=1,
                stop=["\n"]
            )
            
            # Get the relevance score (logit)
            relevance_logit = response.choices[0].logit
            
            # Add paper and relevance to results
            search_results.append((paper, relevance_logit))

        # Sort results based on relevance
        search_results.sort(key=lambda x: x[1], reverse=True)

        # Display search results
        st.subheader('Search Results:')
        for result in search_results[:3]:  # Display top 3 results
            paper, relevance_logit = result
            st.write(f"**Title:** {paper['title']}")
            st.write(f"**Authors:** {', '.join(paper['authors'])}")
            st.write(f"**Abstract:** {paper['abstract']}")
            st.write(f"**Relevance Score:** {relevance_logit}")
            st.markdown('---')  # Add a horizontal line between papers
