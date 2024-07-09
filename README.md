# Women in data science
## Build an AI chatbot leveraging AI Agents and a locally hosted LLM. 

### Ollama set up
- We will be using Ollama to run a local LLM. Make sure you have at least 8GB RAM since we are using Gemma:2b. Download Ollama here - https://ollama.com/
- Run `Ollama pull gemma:2b`

### Python env set up
- I like using Python venv to manage local Python environments.
- `python3 -m venv <env-name>`
- `source <env-name>/bin/activate`
- Install required package dependencies: `pip install -r requirements.txt` in `backend` to install backend files and also in `frontend` to install frontend files
- You need to get an Open AI Api key for the CrewAI agent using so create a free account and set the API key in your environment
  `export OPENAI_API_KEY=<openai api key>` 

### Run the Uvicorn server in backend folder:  
- `uvicorn api:app --reload`
### Run the streamlit server in front end folder:
- `streamlit run app.py` 
