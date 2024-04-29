import pandas as pd
import os

def list_to_csv(lst, model_name, file_name):
    """
    리스트를 csv파일로 저장하는 함수입니다.
    
    :param lst: 리스트입니다.
    :param model_name: 저장할 열의 모델 이름입니다.
    :param file_name: 파일 개수를 세고 싶은 디렉토리의 경로입니다.
    """
    
    tmp_dict = dict()
    tmp_dict[model_name] = lst
    pd.DataFrame(tmp_dict, index=list(range(len(lst)))).to_csv(f"../{file_name}")

    print(f"{file_name} 저장 완료!")
    

def count_image_files(directory_path):
    """
    지정된 디렉토리 내의 파일 수를 세는 함수입니다.
    
    :param directory: 파일 개수를 세고 싶은 디렉토리의 경로입니다.
    :return: 디렉토리 내의 파일 수입니다.
    """

    entries = os.listdir(directory_path)
    
    # 파일만 세기 위해, 각 항목이 파일인지 디렉토리인지 확인합니다.
    # os.path.isfile() 함수는 주어진 경로가 파일인지 확인합니다.
    file_count = sum(os.path.isfile(os.path.join(directory_path, entry)) for entry in entries)
    
    return file_count

def formatting_data(directory_path):
    files = os.listdir(directory_path)
    
    count = count_image_files(directory_path)
    
    
    for filename in files:
        if filename.endswith(".jpg"):  # PNG 파일만 처리
            new_filename = f"{count}.png"
            os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))
            count += 1

    print("파일 이름 변경 완료!")