from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from typing import List, Dict

# AI와의 상호작용을 위한 유틸리티 함수
def ai_query(system_prompt: str, user_prompt: str, conversation: str = "", chat_history: List = []) -> str:
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("placeholder", "{chat_history}"),
            ("human", user_prompt.format(conversation=conversation)),
        ]
    )
    chain = chat_template | llm
    response = chain.invoke({'conversation': conversation, 'chat_history': chat_history})
    return response

def simple_ai_query(prompt: str) -> Dict:
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    chat_template = ChatPromptTemplate.from_message(
        [
            ("human", "{prompt}")
        ]
    )
    chain = chat_template | llm
    response = chain.invoke({'prompt': prompt})