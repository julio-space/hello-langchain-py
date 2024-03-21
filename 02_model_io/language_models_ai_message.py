# check-0321
from langchain_openai import ChatOpenAI  #← 모듈 가져오기
from langchain_core.messages import HumanMessage, AIMessage

llm = ChatOpenAI(  #← 클라이언트를 만들고 chat에 저장
    model="gpt-3.5-turbo",  #← 호출할 모델 지정
)

messages = [
    HumanMessage(content="계란찜을 만드는 법을 알려줘"), 
    AIMessage(content="""
    1. 물 500ml을 준비한다.
    2. 양파 당근을 잘게 썰어 넣는다.
    3. 치킨 스톡 작은스푼 하나 넣는다.
    4. 계란물 300ml 풀어 넣는다.
    5. 타지 않게 잘 저어주며 중불에 끓인다          
    """), 
    HumanMessage(content="답변을 영어로 번역해줘")
]

result = llm.invoke(messages)

# print(result)
print(result.content)
