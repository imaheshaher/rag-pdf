from langchain.llms import Ollama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = Ollama(model="deepseek-r1")

memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

response = conversation.run("What are the CRM lead statuses?")
print(response)
