import pickle
import numpy as np
from pathlib import Path

# ----------------------------
from ursina import *

# -----------------------------
from normalization import scaler


BASE_DIR = Path(__file__).resolve().parent.parent
Text.default_font = "src/main_font.ttf"


class VectorGetter:
    """Vectorization 객체가 생성,저장한 벡터를 불러올때 사용하는 클래스입니다."""

    def __init__(self, data_name: str, dir_path: str):
        self.data_name, self.dir_path = data_name, dir_path

        self.opener()

    def opener(self) -> dict:
        with open(f"{self.dir_path/self.data_name}.vec", "rb") as file:
            self._data = pickle.load(file)

    @property
    def vec3(self) -> np.array:
        if (dim := self._data["compressed_dimension"]) != 3:
            raise Exception(f"해당 데이터는 3차원으로 압축되어있지 않습니다! | 압축상태={dim}차원")
        return self._data["compressed"]

    @property
    def origin(self) -> np.array:
        return self._data["origin"]


class BookBox(Entity):
    def __init__(self, title: str):
        super().__init__()
        vector = VectorGetter(title, dir_path=BASE_DIR / "DATA/vectors").vec3
        normalized_vector = scaler.transform([vector])
        print(f"앙~! {normalized_vector}")
        self.position = Vec3(*normalized_vector[0])
        self.scale = 3
        self.model = "cube"
        self.texture = load_texture("src/books/인간 본성의 법칙.jpg")
