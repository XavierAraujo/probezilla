import argparse
from providers.llm_provider import LLMProvider
from providers.llm_provider_type import LLMProviderType
from providers.openai_provider import OpenaiProvider
from context_provider import ContextProvider

def main():
    args = configure_parser()
    llm_provider_type = args.llm
    apikey = args.api_key
    context_provider = ContextProvider()

    print(f"Using LLM provider: {llm_provider_type}")
    llm_provider = get_chosen_llm_provider(llm_provider_type, apikey)
    initial_context = context_provider.get_interviewer_initial_context(
        context_provider.get_default_interview_subjects()
    )

    llm_provider.get_initial_question(initial_context)
    while True:
        answer = input()
        if answer == "quit":
            break
        llm_provider.answer(answer)


def configure_parser():
    parser = argparse.ArgumentParser(
        prog='Probezilla',
        description='Your friend interviewer',
        epilog='')

    parser.add_argument(
        "--llm",
        type=lambda c: LLMProviderType[c.upper()],
        choices=list(LLMProviderType),
        required=True,
        help="Choose an LLM provider: " + ", ".join([c.value for c in LLMProviderType]))

    parser.add_argument(
        "--api-key",
        type=str,
        required=True,
        help="Provide the API key to the chosen LLM provider"
    )

    return parser.parse_args()

def get_chosen_llm_provider(provider: LLMProviderType, apikey: str) -> LLMProvider:
    if provider == LLMProviderType.OPENAI:
        return OpenaiProvider(apikey)
    else:
        raise Exception("Unknown LLM provider")

if __name__ == "__main__":
    main()
