""" 데이터 전처리에 사용되는 모듈입니다. """
from __future__ import annotations

# -------------내장 라이브러리--------------------
import re, pickle
from typing import Tuple, List, Callable
from pathlib import Path

# --------------외부 라이브러리---------------------
from kss import split_sentences
from pykospacing import Spacing
from hanspell import spell_checker

BASE_DIR = Path(__file__).resolve().parent.parent


class Preprocessing:
    """GooglePlayBook_Scanner 모듈에서 생성한 데이터를 전용으로 전처리 할때 사용하는 클래스입니다."""

    def __init__(
        self,
        marge_output: str,
        result_output: str,
        target_name_gen: Callable[[int], str],
        target_range: Tuple[int] = (1, 1574),
        spacing_ruls: List[str] = [],
    ):
        """
        생성된 인스턴스는 target_dir의 데이터를 합쳐서 전처리를 거친 뒤 marge_output의 이름으로 저장합니다.
        이렇게 marge_output은 해당 책의 텍스트본이 됩니다.

        target_name_gen인자 -> 대상 파일 이름 이터레이터용 함수입니다.
        예시: lambda i: f"/book/TXT/laws of human nature [{i}]_새로 만들기.txt"

        target_range인자 -> 이터레이션 범위입니다 (내장 라이브러리의 스캔은 한계가 있어서 이런 방식을 사용합니다.)

        전처리 과정중 띄어쓰기를 교정하는데, 이때 성능을 높이기 위해서 spacing_ruls인자를 넣어줄 수 있습니다.
        인자 형식은 붙여써야 하는 단어를 알려주는 List입니다.
        """

        self.marge_output, self.result_output, self.target_name_gen, self.target_range = (
            marge_output,
            result_output,
            target_name_gen,
            target_range,
        )
        # -----------------------------------------------------------------------------------
        self.spacing = Spacing(rules=spacing_ruls)

    def save(self, corpus: tuple):
        """corpus를 직렬화해서 바이너리로 저장합니다. 경로는 self.result_output 입니다."""
        with open(f"{self.result_output}.corpus", "wb") as file:
            pickle.dump(corpus, file)

    def run(self, capacity_limit=None) -> Tuple[str]:
        """
        각종 조건이 충족될때 가장 빠르고 편하게 실행시키는 방법입니다.

        디버깅 시 capacity_limit을 통해서 입력 용량을 제한할 수 있습니다.

        반환되는 결과값은 corpus 튜플 입니다.
        """

        text_data = self.marge_txts()[: capacity_limit if capacity_limit else None]
        sentence_tokenized_text = self.tokeniztion(text_data)

        cleaned = (self.clean_text(sent) for sent in sentence_tokenized_text)
        corpus = tuple(self.clean_grammar(text) for text in cleaned)

        self.save(corpus)
        return corpus

    def clean_grammar(self, text: str) -> str:
        """텍스트의 문법을 올바르게 교정합니다"""

        spacing_corrected = self.spacing(text)
        spelling_corrected = spell_checker.check(spacing_corrected).checked

        return spelling_corrected

    def clean_text(self, text: str) -> str:
        """텍스트에서 불필요한 요소들을 제거합니다."""

        letters = "∞θ÷α•à−β∅³π‘₹´°£€\×™√²—–& @%\\*=()/#&\+á\xc3\xa1\-\|\:\;\_" + "…" + "करना" + "है"

        for punct in letters:
            text = text.replace(punct, "")  # 불용문자 제거

        txt = re.sub("[a-zA-Z]", "", text)  # 영어 제거
        txt = txt.replace(" ", "")  # spacing을 위한 띄어쓰기 제거
        return txt

    @staticmethod
    def tokeniztion(text: str) -> Tuple[str]:
        """문장으로 토큰화해서 튜플로 반환합니다."""

        return tuple(sent.strip() for sent in split_sentences(text))

    def marge_txts(self) -> str:
        """
        디렉토리 내부에 존재하는 대량의 txt 파일을 하나로 합칩니다.
        이 함수를 거치면 모든 줄바꿈이 없어집니다.
        합쳐진 데이터는 txt파일로 저장하고 str로도 반환됩니다.
        """

        text_data: str = ""
        not_scanned: List[str] = []

        start, end = self.target_range

        for file_name in (self.target_name_gen(i) for i in range(start, end + 1)):
            try:
                with open(file_name, "r", encoding="utf-8") as file:
                    text_data += file.read().replace("\n", "")
            except FileNotFoundError:
                print(f"데이터 결측-{file_name}")
                not_scanned.append(file_name)

        if not_scanned:
            print(f"결측 데이터 갯수: {len(not_scanned)}")
        print(f"[marge_txts]데이터 {end-(start-1)-len(not_scanned)}개 처리 완료")

        with open(self.marge_output, "w", encoding="utf-8") as file:
            file.write(text_data)

        return text_data

    @staticmethod
    def open_txt(file_name: str, encoding="utf-8") -> str:
        """루트경로의 txt파일을 읽어서 str로 반환합니다."""

        with open(file_name, "r", encoding=encoding) as file:
            text = file.read()

        return text


if __name__ == "__main__":
    #! 메서드 실행 순서 가이드 -> 이 프로세스는 객체 외부에서 함수화 하는게 나을듯

    BOOK_NAME = "인간 본성의 법칙"

    preprocessing = Preprocessing(
        marge_output=f"{BASE_DIR}/DATA/books/{BOOK_NAME}.txt",
        result_output=f"{BASE_DIR}/DATA/corpus/{BOOK_NAME}",
        target_name_gen=lambda i: BASE_DIR
        / f"GooglePlayBook_Scanner/data/{BOOK_NAME}/TXT"
        / f"laws of human nature [{i}]_새로 만들기.txt",
        target_range=(1, 1574),
    )
    # text_data = preprocessing.marge_txts()[:400]
    # sentence_tokenized_text = preprocessing.tokeniztion(text_data)

    # cleaned_corpus = [preprocessing.clean_text(sent) for sent in sentence_tokenized_text]
    # basic_preprocessed_corpus = [preprocessing.clean_grammar(text) for text in cleaned_corpus]

    result = preprocessing.run(capacity_limit=5000)
    for corpus in result:
        print(corpus)
