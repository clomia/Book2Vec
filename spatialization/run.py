from os import listdir
from pathlib import Path
from ursina import *
from .space import Universe
from .controller import Eye
from .rendering import BookBox

BASE_DIR = Path(__file__).resolve().parent.parent


def virtual_space():
    """DATA/vectors에 저장된 벡터들을 가상공간에 렌더링합니다."""

    app = Ursina()

    walls = {
        "bottom": "src/wall_bottom.jpg",
        "top": "src/wall_top.jpg",
        "left": "src/wall_front.jpg",
    }
    space_cube = Universe(walls, "src/universe.jpg")
    Eye(limit=space_cube.scale)

    for book in listdir(BASE_DIR / "DATA/vectors"):
        book_box = BookBox(book[:-4])
        print(f"{book}의 3차원 좌표: {book_box.position}")

    window.fullscreen = True
    app.run()
