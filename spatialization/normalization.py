""" 벡터 정규화 스케일러를 만들어줍니다 """
import os, pickle
from pathlib import Path
from sklearn.preprocessing import MinMaxScaler

__all__ = ["scaler"]

BASE_DIR = Path(__file__).resolve().parent.parent
path = BASE_DIR / "DATA/vectors"

vectors = []
for name in os.listdir(path):
    with open(path / name, "rb") as file:
        data = pickle.load(file)
        vectors.append(data["compressed"])

scaler = MinMaxScaler(feature_range=(-45, 45))
scaler.fit(vectors)
