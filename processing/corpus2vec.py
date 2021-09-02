import pickle
from pathlib import Path

# --------------외부 라이브러리---------------------
import numpy as np
from gensim.models.fasttext import load_facebook_vectors
from sklearn.decomposition import PCA

BASE_DIR = Path(__file__).resolve().parent.parent


class Vectorization:
    """corpus 벡터화를 조작하는 클래스"""

    def __init__(self, corpus: str, model: str, data_name: str, save_dir: str):
        """
        corpus와 model인자는 경로/파일이름을 나타냅니다

        더럽게 오래걸리기 때문에 연산 후 저장 할 수 있습니다.
        save_dir 안에 data_name 으로 저장합니다.
        """
        self.save_dir, self.data_name = save_dir, data_name
        # --------------------------------------------------
        with open(corpus, "rb") as file:
            self.corpus = pickle.load(file)
        self.model = load_facebook_vectors(model)

    def fit(self):
        """corpus를 벡터화합니다. [1]"""
        self.origin_vectors = np.array(tuple(self.model[token] for token in self.corpus))

    def compression(self, dimension: int = 3) -> np.array:
        """dimension 차원인 벡터 하나로 압축합니다.  [2]"""

        self.conpressed_dimension = dimension
        vertors = PCA(n_components=dimension, random_state=2).fit_transform(self.origin_vectors)
        self.compressed_vector = np.mean(vertors, axis=0)
        return self.compressed_vector

    def save(self):
        """객체 정보를 저장합니다. [3]"""
        path = f"{self.save_dir}/{self.data_name}.vec"
        with open(path, "wb") as file:
            data = {
                "origin": self.origin_vectors,
                "compressed": self.compressed_vector,
                "compressed_dimension": self.conpressed_dimension,
            }
            pickle.dump(data, file)

        print(f"[Vectorization] 객체 정보가 {path}에 저장되었습니다.")


if __name__ == "__main__":

    vec = Vectorization(
        corpus=BASE_DIR / "DATA/corpus" / "인간 본성의 법칙.corpus",
        model=BASE_DIR / "DATA/model/cc.ko.300.bin",
        data_name="인간 본성의 법칙",
        save_dir=BASE_DIR / "DATA/vectors",
    )

    vec.fit()
    vec.compression()
    vec.save()
