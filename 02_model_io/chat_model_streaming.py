# check-0321
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(
    model="gpt-3.5-turbo"
)

for chunk in llm.stream("맛있는 스테이크 굽는 법을 알려주세요"):
    print(chunk.content, end="", flush=True)
