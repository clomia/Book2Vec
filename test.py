from pathlib import Path
from typing import Dict

BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "인간 본성의 법칙.txt", encoding="utf-8") as file:
    text = file.read()


# ------------------------------------------------------------------------------------------

sample = text[:300]

punct = "/-'?!.,#$%'()*+-/:;<=>@[\\]^_`{|}~" + '""“”’' + "∞θ÷α•à−β∅³π‘₹´°£€\×™√²—–&"
punct_mapping = {
    "‘": "'",
    "₹": "e",
    "´": "'",
    "°": "",
    "€": "e",
    "™": "tm",
    "√": " sqrt ",
    "×": "x",
    "²": "2",
    "—": "-",
    "–": "-",
    "’": "'",
    "_": "-",
    "`": "'",
    "“": '"',
    "”": '"',
    "“": '"',
    "£": "e",
    "∞": "infinity",
    "θ": "theta",
    "÷": "/",
    "α": "alpha",
    "•": ".",
    "à": "a",
    "−": "-",
    "β": "beta",
    "∅": "",
    "³": "3",
    "π": "pi",
}


def clean_punct(text: str, punct: str, mapping: Dict[str, str]) -> str:
    """구두점을 처리합니다. 처리가능한 문자로 바꾸며, 마침표나 따움표 양쪽에는 공백을 생성합니다."""

    for p in mapping:
        text = text.replace(p, mapping[p])

    for p in punct:
        text = text.replace(p, f" {p} ")

    specials = {"\u200b": " ", "…": " ... ", "\ufeff": "", "करना": "", "है": ""}
    for s in specials:
        text = text.replace(s, specials[s])

    return text.strip()


import kss, re
from pykospacing import Spacing

sentence_tokenized_text = [sent.strip() for sent in kss.split_sentences(sample)]
cleaned_corpus = [clean_punct(sent, punct, punct_mapping) for sent in sentence_tokenized_text]


def clean_text(text: str) -> str:
    """텍스트에서 불필요한 요소들을 제거합니다."""

    txt = re.sub(r"[@%\\*=()#&\+á\xc3\xa1\-\|\:\;\-\_\~\$]", "", str(text))  # 불용 구두점 제거
    txt = re.sub(r"<[^>]+>", "", txt)  # HTML 태그 제거
    txt = re.sub("[a-zA-Z]", "", txt)  # 영어 제거
    txt = txt.replace(" ", "")  # 띄어쓰기 제거
    return txt


basic_preprocessed_corpus = [clean_text(text) for text in cleaned_corpus]

print(basic_preprocessed_corpus)

spacing = Spacing()

for sent in basic_preprocessed_corpus:
    print(spacing(sent))
