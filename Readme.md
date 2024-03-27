# Langchain Examples

> 본 프로젝트는 __랭체인 완벽 입문 (위키북스)__ 실습예제의 버전 이슈로 인한 문제를 해결하기 위해 작성된 프로젝트 입니다.

교재의 예제가 **Deprecated된 코드**들을 다수 포함하고 있어 특정 버전 종속을 제거하고 **정상 동작하는 샘플로 재작성**하는 작업을 진행

## I. Getting Started

### I-1. OepnAI API Key Setting

> Langchain은 기본적으로 __OPENAPI_API_KEY__ 환경변수의 값을 참조하게 설정

#### [MacOS]

```shell
$ export OPENAI_API_KEY="sk-beOSbZBrVS1KSOP0Ox....."
```

#### [Windows]

```shell
c:/> set OPENAI_API_KEY "sk-beOSbZBrVS1KSOP0Ox....."
```

### I-2. Install Modules

```shell
$ pip install openai
$ pip install langchain
$ pip install langchain-openai
$ pip install langchain-community
```

### I-3. References

* 교재: https://product.kyobobook.co.kr/detail/S000212260283
* 예제: https://github.com/wikibook/langchain

## II. Model I/O

| 파일명 | 예제 설명 |
| --- | --- |
| [01_setting/sample.py](https://github.com/julio-space/hello-langchain-py/blob/main/01_setting/sample.py) | OpenAI ChatCompletion Sample |
| [02_model_io/language_models.py](https://github.com/julio-space/hello-langchain-py/blob/main/02_model_io/language_models.py) | HumanMessage를 이용해 모델 호출 |
| [02_model_io/language_models_ai_message.py](https://github.com/julio-space/hello-langchain-py/blob/main/02_model_io/language_models_ai_message.py) | HumanMessage / AIMessage를 이용해 모델 호출 |
| [02_model_io/language_models_system_message.py](https://github.com/julio-space/hello-langchain-py/blob/main/02_model_io/language_models_system_message.py) | HumanMessage / SystemMessage를 이용해 모델 호출 |
| [02_model_io/prompt.py](https://github.com/julio-space/hello-langchain-py/blob/main/02_model_io/prompt.py) | PromptTemplate 기본 생성 |
| [02_model_io/prompt_and_language_model.py](https://github.com/julio-space/hello-langchain-py/blob/main/02_model_io/prompt_and_language_model.py) | LLM과 PromptTemplate의 결합 |
| [02_model_io/prompt_template_from_template_save_sample.py](https://github.com/julio-space/hello-langchain-py/blob/main/02_model_io/prompt_template_from_template_save_sample.py) | PromptTemplate을 파일로 저장 |
| [02_model_io/prompt_template_from_template_load_sample.py](https://github.com/julio-space/hello-langchain-py/blob/main/02_model_io/prompt_template_from_template_load_sample.py) | 파일로 저장된 PromptTemplate을 로드 |
| [02_model_io/list_output_parser.py](https://github.com/julio-space/hello-langchain-py/blob/main/02_model_io/list_output_parser.py) | 목록 형식으로 결과 받기 |
| [02_model_io/model_io_llm.py](https://github.com/julio-space/hello-langchain-py/blob/main/02_model_io/model_io_llm.py) | LLM으로 다음 문장 예측 |
| [02_model_io/chat_model_cache.py](https://github.com/julio-space/hello-langchain-py/blob/main/02_model_io/chat_model_cache.py) | Caching |
| [02_model_io/chat_model_streaming.py](https://github.com/julio-space/hello-langchain-py/blob/main/02_model_io/chat_model_streaming.py) | 결과를 스트리밍 |
| [02_model_io/model_io_few_shot.py](https://github.com/julio-space/hello-langchain-py/blob/main/02_model_io/model_io_few_shot.py) | FewShotPromptTemplate |

## III. Retrieval


## IV. Memory


## V. Chain


## VI. Agent


## VII. Callback

