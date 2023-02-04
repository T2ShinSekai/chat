import configparser
from libs import AWS, OpenAI

CONFIG_PATH = "../config/config.ini"
FINE_TUNED_MODEL = "davinci:ft-personal-2023-01-15-05-41-59"


def main():
    config = configparser.ConfigParser()
    try:
        config.read(CONFIG_PATH)
        openai_client = OpenAI(config["OPEN_AI"]["API_KEY"])
        query = input("話しましょう！何か入力してください : ")
        prompt = openai_client.generate_prompt(query)
        res = openai_client.call_gpt3_api(prompt=prompt, engine=FINE_TUNED_MODEL)
        print(f"受付嬢 :{res}")
        aws_client = AWS(
            config["AWS"]["ACCESS_KEY"],
            config["AWS"]["SECRET_ACCESS_KEY"],
            config["AWS"]["REGION"],
        )
        sentiment = aws_client.call_detect_sentiment(res)
        print(f"感情 :{sentiment['Sentiment']}")
        sentiment_score = sentiment["SentimentScore"]
        print(f"ポジティブスコア:{sentiment_score['Positive']}")
        print(f"ネガティブスコア:{sentiment_score['Negative']}")
        print(f"ニュートラルスコア:{sentiment_score['Neutral']}")
        print(f"混合スコア:{sentiment_score['Mixed']}")
    except Exception as e:
        print(e)
