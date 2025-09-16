"""
디렉토리 관련 유틸함수들 추가 필요

check_dir : 입력 인자가 디렉토리에 있는지 확인하고 없으면 만들어줌

"""
import os
import num

def check_dir(path):
    """
    #TODO : 
    이름 규칙 필요
    """
    if not os.path.exists(path):
        print(f"{path} 가 없어서 새로 만듭니다.")
        os.makedirs(path)    
    pass

def check_dir_tree():
    """
    재귀호출 함수로 경로에 있는 모든 폴더 생성
    """

    pass