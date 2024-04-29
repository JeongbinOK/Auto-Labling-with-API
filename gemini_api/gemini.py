import google.generativeai as genai
import PIL.Image

class GeminiAPI:
    def __init__(self, model_name, api_key):
        """
        Gemini API 클래스의 생성자입니다.
        
        :param model_name: 사용할 모델의 이름입니다.
        :param api_key: Gemini API 사용을 위한 API 키입니다.
        """
        self.model_name = model_name
        self.api_key = api_key
        genai.configure(api_key=self.api_key)
        
        self.model = genai.GenerativeModel(model_name=model_name)
        
        
    def generate(self, text, image_path, temperature = 1):
        """
        입력된 텍스트와 이미지를 기반으로 새로운 텍스트를 생성합니다.
        
        :param text: 기존 텍스트 정보입니다.
        :param image_path: 관련 이미지 데이터입니다. 이미지는 처리 가능한 형식이어야 합니다.
        :param temperature 모델의 temperature입니다. 입력값은 0 ~ 무한대입니다.
        :return: 생성된 텍스트의 결과입니다.
        """
        image = PIL.Image.open(image_path)
        # API 호출
        response = self.model.generate_content([text, image], generation_config={"temperature": temperature})

        if response._done:
            return response.text
        else:
            return False

