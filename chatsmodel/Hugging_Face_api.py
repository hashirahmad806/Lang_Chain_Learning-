from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
import warnings

warnings.filterwarnings("ignore")
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.1-8B-Instruct',
    task='text-generation'
)


model = ChatHuggingFace(llm=llm)

result = model.invoke(
    " About  pakistan best cricket player and his performance in 2023 world cup")
print(result.content)
