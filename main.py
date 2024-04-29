from gemini_api import gemini
from gpt4_api import gpt4
from tqdm import tqdm
from utils import data

# 사용 예시
# gemini = GeminiAPI('model123', 'api-key-abc123')
# generated_text = gemini.generate('Hello world', b'YourImageBinaryDataHere')
# print(generated_text)

if __name__ == "__main__":
    data_directory_path = "C:\\Users\\Auto-Labling-with-API\\data"
    data_len = data.count_image_files(data_directory_path)
    
    ## 파일 이름 n.png 형식으로 바꾸기
    formatting = False
    if formatting:
        data.formatting_data(data_directory_path)
    
    text = "Describe this image"
    
    gpt4_api_key = ""
    gpt4_api_model=""
    
    ### GPT4
    if gpt4_api_key != "" and gpt4_api_model != "":
        gpt4_lst = []
        gpt4_API = gpt4.GPTAPI(gpt4_api_model, gpt4_api_key)
        for i in tqdm(range(1, data_len+1)):
            image_path = data_directory_path +f"{i}.png"
            generated_text = gpt4_API.generate(text,image_path)
            if not generated_text:
                print("not generated!!")
                break
            gpt4_lst.append(generated_text)
        else:
            data.list_to_csv(gpt4_lst,gpt4_api_model,"gpt4_text.csv")
    
    
    gemini_api_key = ""
    gemini_api_model=""
    
    ### Gemini
    if gemini_api_key != "" and gemini_api_model != "":
        gemini_lst = []
        gemini_API = gemini.GeminiAPI(gemini_api_model, gemini_api_key)
        for i in tqdm(range(1, data_len+1)):
            image_path = data_directory_path +f"{i}.png"
            generated_text = gemini_API.generate(text,image_path)
            if not generated_text:
                print("not generated!!")
                break
            gemini_lst.append(generated_text)
        else:
            data.list_to_csv(gemini_lst,gemini_api_model,"gpt4_text.csv")
    
    
    
    
    