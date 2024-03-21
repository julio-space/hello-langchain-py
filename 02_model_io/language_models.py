# check-0321
from langchain_openai import ChatOpenAI  #← 모듈 가져오기

llm = ChatOpenAI(  #← 클라이언트를 만들고 chat에 저장
    model="gpt-3.5-turbo",  #← 호출할 모델 지정
)

result = llm.invoke("안녕하세요!")

print(result)
print(result.content)
