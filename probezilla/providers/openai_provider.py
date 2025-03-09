from llm_provider import LLMProvider

class OpenaiProvider(LLMProvider):

    def __init__(self, apikey):
        self.apikey = apikey

    def get_initial_question(self, context: str) -> str:
        print("Get initial question from OpenAI provider")
        return "dummy"

    def answer(self, answer: str) -> str:
        print("Answering question from OpenAI provider")
        pass