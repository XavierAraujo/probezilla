from .llm_provider import LLMProvider
from openai import OpenAI


class OpenaiProvider(LLMProvider):

    _GPT_3_5_TURBO_MODEL = "gpt-3.5-turbo",
    _GPT_4_MODEL = "gpt-4",

    def __init__(self, apikey):
        self.apikey = apikey
        self.client = OpenAI()
        self.conversation = list()
        self.is_interview_started = False

    def start_interview(self, context: str) -> str:
        if self.is_interview_started:
            raise Exception("Interview already started.")

        self.conversation.append({"role": "system", "content": context})
        reply = self._chat()
        self.conversation.append({"role": "assistant", "content": reply})

        self.is_interview_started = True
        return reply

    def answer(self, answer: str) -> str:
        if not self.is_interview_started:
            raise Exception("Interview not yet started.")

        self.conversation.append({"role": "user", "content": answer})
        reply = self._chat()
        self.conversation.append({"role": "assistant", "content": reply})
        return reply

    def _chat(self):
        response = self.client.chat.completions.create(
            model=self._GPT_3_5_TURBO_MODEL,
            messages=self.conversation)

        reply = response.choices[0].message.content
        return reply
