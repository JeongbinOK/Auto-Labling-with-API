from openai import OpenAI
import base64
import requests


def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

class GPTAPI:
    def __init__(self, model_name, api_key):
        """
        Gemini API 클래스의 생성자입니다.
        
        :param model_name: 사용할 모델의 이름입니다.
        :param api_key: Gemini API 사용을 위한 API 키입니다.
        """
        self.model_name = model_name
        self.api_key = api_key
       
        
    def generate(self, text, image_path, temperature = 1):
        """
        입력된 텍스트와 이미지를 기반으로 새로운 텍스트를 생성합니다.
        
        :param text: 기존 텍스트 정보입니다.
        :param image_path: 관련 이미지 데이터입니다. 이미지는 처리 가능한 형식이어야 합니다.
        :param temperature 모델의 temperature입니다. 입력값은 0 ~ 무한대입니다.
        :return: 생성된 텍스트의 결과입니다.
        """
        base64_image = encode_image(image_path)
        # API 호출
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = {
            "model": self.model_name,
            "messages": [
            {
                "role": "user",
                "content": [
                {
                    "type": "text",
                    "text": text
                },
                {
                    "type": "image_url",
                    "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
                ]
            }
            ],
            "max_tokens": 300,
            "temperature": 0.7
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return False

