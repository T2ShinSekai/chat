import openai


class OpenAI:
    MAX_TOKENS = 150
    IS_RES_WITH_PROMPT_ECHO = False
    ENGINE = "davinci"
    STOP = "\n"

    def __init__(self, key):
        openai.api_key = key

    def call_gpt3_api(
        self,
        prompt="",
        engine=ENGINE,
        max_tokens=MAX_TOKENS,
        stop=STOP,
        is_res_with_prompt_echo=IS_RES_WITH_PROMPT_ECHO,
    ):
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=max_tokens,
            stop=stop,
            echo=is_res_with_prompt_echo,
        )
        answer = response["choices"][0]["text"]
        return answer

    def generate_prompt(self, query):
        prompt = (
            "元気な女性のチャットボットです。\n"
            "私: こんにちは、調子はどう？\n"
            "AI: 元気です！\n"
            f"私: {query} \n"
            "AI:"
        )
        return prompt
