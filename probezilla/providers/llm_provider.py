from abc import ABC, abstractmethod


class LLMProvider(ABC):
    @abstractmethod
    def start_interview(self, context: str) -> str:
        pass

    @abstractmethod
    def answer(self, answer: str) -> str:
        pass