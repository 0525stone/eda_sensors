"""
디렉토리 관련 유틸함수들 추가 필요

check_dir : 입력 인자가 디렉토리에 있는지 확인하고 없으면 만들어줌

데이터를 합치고 띄우고를 편하게 하려면 함수화를 미리 해놓으면 좋을 것 같음...
figure 단위로 덕지덕지 붙이기 좋게 코드를 함수화할 수는 없을까?
xlabel 도 자유롭게 조정할 수 있게 하면 좋을 듯



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