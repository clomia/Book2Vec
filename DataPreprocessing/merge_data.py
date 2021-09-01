from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def marge_txts(save: str = "The Laws of Human Nature.txt", start: int = 1, end: int = 1574) -> str:

    target_dir = "GooglePlayBook_Scanner/data/TXT"
    text_data = ""
    not_scanned = []

    for file_name in (f"laws of human nature [{i}]_새로 만들기.txt" for i in range(start, end + 1)):
        try:
            with open(BASE_DIR / target_dir / file_name, "r", encoding="utf-8") as file:
                text_data += file.read()
        except FileNotFoundError:
            not_scanned.append(file_name)

    if not_scanned:
        print(f"결측 데이터 갯수: {len(not_scanned)}")
    print(f"[marge_txts]데이터 {end-(start-1)-len(not_scanned)}개 처리 완료")

    if save:
        with open(save, "w", encoding="utf-8") as file:
            file.write(text_data)

    return text_data


marge_txts()
