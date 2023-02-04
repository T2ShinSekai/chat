import boto3


class AWS:
    def __init__(self, key, secret, region):
        self.key = key
        self.secret = secret
        self.region = region

    def call_detect_sentiment(self, query):
        SERVICE_NAME = "comprehend"
        LANGUAGE_CODE = "ja"

        client = boto3.client(
            SERVICE_NAME,
            aws_access_key_id=self.key,
            aws_secret_access_key=self.secret,
        )
        semtiment = client.detect_sentiment(Text=query, LanguageCode=LANGUAGE_CODE)
        return semtiment
