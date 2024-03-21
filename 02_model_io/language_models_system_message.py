# check-0321
from langchain_openai import ChatOpenAI  #← 모듈 가져오기
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOpenAI(  #← 클라이언트를 만들고 chat에 저장
    model="gpt-3.5-turbo",  #← 호출할 모델 지정
)

messages = [
    SystemMessage(content="당신은 친한 친구입니다. 존댓말을 쓰지 말고 솔직하게 답해주세요."), 
    HumanMessage(content="안녕!")
]

result = llm.invoke(messages)

# print(result)
print(result.content)
