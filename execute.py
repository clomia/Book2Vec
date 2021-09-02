"""
작업 순서
책 이름을 "샘플책" 이라고 하겠다.

1. 책을 캡쳐하면서 OCR로 텍스트 변환을 한다. (GooglePlayBook_Scanner모듈을 사용할 수도 있다.) 
이때, 특정 폴더에 "샘플책[(counter)].txt"형식으로 저장되도록 한다.

2. processing.preprocessing 모듈을 사용해서 해당 폴더의 텍스트 파일을 처리한다.
전처리를 거쳐서 완성된 파일은 DATA/corpus 폴더로 저장된다. 이름은 "샘플책.corpus"로 한다

3. processing.corpus2vec 모듈을 사용해서 DATA/corpus에 저장된 파일을 벡터화하고 
차원축소 등의 프로세스를 거쳐서 3차원 벡터 하나로 압축시킨 뒤 해당 벡터를 DATA/vectors 폴더에 저장합니다.

4. 책의 정사각형 사진을 spatialization/src/books 에 "샘플책.jpg"로 저장합니다.

5. spatialization.run.virtual_space 함수를 사용해서 BookBox들이 만들어진 가상공간으로 진입합니다.


!! txt_to_vec함수로 대부분 엮어놨지만 1, 4단계는 직접 수행해야 합니다.
"""
from sys import argv
from pathlib import Path

# ------------------------------
from processing import Preprocessing, Vectorization
from spatialization import virtual_space

BASE_DIR = Path(__file__).resolve().parent
print(f"실행 위치: {BASE_DIR}")


def txt_to_vec(book_name: str, endpoint: int, ocr_name: str = None):
    """
    [이 함수를 거친 데이터는 가상공간에 렌더링 할 수 있게됩니다.]

    여러 모듈이 wrapping된 함수입니다. 실행 조건과 방법은 모듈 doc과 디렉토리 구조를 참조해주세요.

    ocr_name 인자는 book_name과 ALPDF 프로그램을 사용할떄의 이름이 다를때만 사용합니다.
    """
    if not ocr_name:
        ocr_name = book_name

    target_name_iter_func = (
        lambda i: BASE_DIR / f"GooglePlayBook_Scanner/data/{book_name}/TXT" / f"{ocr_name} [{i}]_새로 만들기.txt"
    )

    Preprocessing(
        marge_output=f"{BASE_DIR}/DATA/books/{book_name}.txt",
        result_output=f"{BASE_DIR}/DATA/corpus/{book_name}",
        target_name_gen=target_name_iter_func,
        target_range=(1, endpoint),
    ).run(capacity_limit=400)

    vec_controller = Vectorization(
        corpus=BASE_DIR / "DATA/corpus" / f"{book_name}.corpus",
        model=BASE_DIR / "DATA/model/cc.ko.300.bin",
        data_name=book_name,
        save_dir=BASE_DIR / "DATA/vectors",
    )
    vec_controller.fit()
    vec_controller.compression(dimension=3)
    vec_controller.save()


_, *args = argv

if args[0] == "--txt_to_vec":
    txt_to_vec(args[1], endpoint=int(args[2][5:]))
elif args[0] == "--virtual_space":
    virtual_space()

"""
명령행 호출 가이드

1. 벡터화
python execute.py --txt_to_vec 어린왕자 --ep=3

2. 가상공간 실행
python execute.py --virtual_space

"""
