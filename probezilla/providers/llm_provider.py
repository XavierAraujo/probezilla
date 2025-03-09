from abc import ABC, abstractmethod


class LLMProvider(ABC):
    @abstractmethod
    def get_initial_question(self, context: str) -> str:
        pass

    @abstractmethod
    def answer(self, answer: str) -> str:
        pass