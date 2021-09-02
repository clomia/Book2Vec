from ursina import *
from space import Universe
from controller import Eye
from rendering import BookBox


app = Ursina()

walls = {
    "bottom": "src/wall_bottom.jpg",
    "top": "src/wall_top.jpg",
    "left": "src/wall_front.jpg",
}
space_cube = Universe(walls, "src/universe.jpg")

Eye(limit=space_cube.scale)

book = BookBox("인간 본성의 법칙")
print(book.position)
window.fullscreen = True
app.run()
