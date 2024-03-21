from openai import OpenAI #← OpenAI에서 제공하는 Python 패키지 가져오기

client = OpenAI() # API Keys는 환경변수 참조 ($OPENAI_API_KEY)
completion = client.chat.completions.create(  #←OpenAI API를 호출하여 언어 모델을 호출합니다.
    model="gpt-3.5-turbo",  #← 호출할 언어 모델의 이름
    messages=[
        {
            "role": "user",
            "content": "iPhone8 출시일을 알려주세요"  #←입력할 문장(프롬프트)
        },
    ]
)

print(completion)
print(completion.choices[0].message.content)