from fastapi import FastAPI, HTTPException, WebSocket
from contextlib import asynccontextmanager
from pydantic import BaseModel
from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser
import os 

from agent import CrewSearch

class Query(BaseModel):
    question: str

chain = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    model = Ollama(model="gemma:2b")
    openai_api_key = os.environ["OPENAI_API_KEY"]
    search_instance = CrewSearch(openai_api_key)
    app.state.context = search_instance.run_search("technology")
    template = """
    System: You are a very helpful assistant who provides accurate 
    and eloquent answers to questions using the context: {context}"
    Human: {question}
    AI Assistant: """

    prompt = PromptTemplate.from_template(template) 
    app.state.chain = LLMChain(prompt=prompt, llm=model)
    yield
    model.clear()


app = FastAPI(lifespan=lifespan)

@app.post("/generate_text/")
async def ask(query: Query):
    try:
        result = await app.state.chain.ainvoke({"question": query.question, "context": app.state.context})
        return {"answer": result['text']}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
