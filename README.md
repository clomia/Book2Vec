책들을 공간에 벡터화 하는 프로젝트 입니다.
==================================
### 딥러닝 자연어(한국어) 처리 - fasttext모델을 사용하였습니다.  
  
  
가상공간은 [LifeGame](https://github.com/clomia/LifeGame) 프로젝트때 만든 모듈 중 몇가지를 리펙토링해서 구현하였습니다.

평면이라는 환경은 인간이 정보를 인식하기에는 너무 제한적입니다.  
서점의 정렬,검색 알고리즘부터 콘텐츠 추천 시스템에 이르기까지  
인간에게 효율적으로 정보를 제공하기 위한 시도는 계속되어오고 있습니다.   
   
현재 많은 서비스는 정보처리에 카테고리, 태그등을 사용한 평면적인 인터페이스를 제공합니다.

아래 사진은 SF영화에 흔히 나오는 요소 중 하나가 3차원 인터페이스입니다.

<img src="https://media.githubusercontent.com/media/clomia/Book2Vec/main/image/3D%20interface.png" width="40%" height="40%"></img>
  
사진처럼 홀로그램이나 VR,AR이 아니어도  
단순히 콘텐츠간의 관계가 나타난 공간이 있다면  
사용자의 정보 인식이 훨씬 수월해질것 같다고 생각하였습니다.  

그래서 "책"이라는 콘텐츠로 공간적인 인터페이스를 만들어보기로 하였습니다.  
![](https://media.githubusercontent.com/media/clomia/Book2Vec/main/image/%EA%B3%B5%EA%B0%84%ED%99%94.jpg)
프로젝트 기간상 많은 공을 들이지 못해서 최소한의 요구사항만 충족해 보았습니다.  
  
workflow는 아래와 같습니다.
  
1. GooglePlayBook_Scanner 모듈을 사용해서 Google Play Books의 책을 스크래핑 한다.  
2. execute.py txt_to_vec를 사용해서 스크래핑된 데이터를 3차원 벡터로 변환한다.  
3. execute.py virtual_space를 사용해서 가상공간을 렌더링한다.  

> 데이터 전처리 과정과 렌더링 프로세스등 모든 처리들은 execute.py 수준의 API에서 모두 간단하게 wrapping되어 있습니다.  
>  
> 명령행 호출 가이드(예시)  
> 1. 벡터화  
> python execute.py --txt_to_vec 어린왕자 --ep=3 --limit=3000  
> 2. 가상공간 실행  
> python execute.py --virtual_space  
> 
> (상세한 내용은 해당 모듈 docstring 참조)

--------
벡터화 과정  

1. [알아서 해줌]전처리가 완료된 txt파일 (책 한권의 내용이 전부 들어있다.)
2. 문장으로 토큰화 한 뒤 DATA/corpus 디렉토리에 데이터 저장  
3. 토큰들을 DATA/model에 있는 facebook의 한국어 fastext모델에 넣어서 벡터로 반환받는다.  
4. (300차원 X 토큰 갯수)만큼의 벡터를 하나의 3차원 벡터로 압축  
    > 압축은 PCA 차원축소 -> 벡터평균 -> Normalization 순서로 진행
5. 압축된 벡터는 메타정보와 함께 DATA/vectors 디렉토리에 저장된다.

-------