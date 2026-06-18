from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# --- THE COSMOS ---
window.title = 'A E T H E R'
window.borderless = False
window.color = color.black
Entity(model='sphere', scale=500, double_sided=True, texture='sky_sunset', color=color.black) # Void

# --- TECHNICAL LIGHTING ---
sun = DirectionalLight()
sun.look_at(Vec3(1, -1, 1))
Sky(texture='sky_dark')

# --- THE MONOLITH (SUDOKU) ---
class SudokuCrystal(Button):
    def __init__(self, pos, val):
        super().__init__(
            parent=scene,
            position=pos,
            model='cube',
            texture='white_cube',
            color=color.rgba(0, 255, 255, 50) if val == 0 else color.rgba(255, 255, 255, 200),
            scale=0.9,
            text=str(val) if val != 0 else ""
        )
        self.val = val
        self.original_color = self.color

    def on_mouse_enter(self):
        self.scale = 1.1
        self.color = color.white

    def on_mouse_exit(self):
        self.scale = 0.9
        self.color = self.original_color

# Generate a 9x9 Vertical Monolith
for y in range(9):
    for x in range(9):
        v = random.choice([0, 0, 0, 1, 2, 3, 4, 5])
        SudokuCrystal(pos=(x - 4, y + 2, 10), val=v)

# --- THE PULSING MINES ---
class LogicTile(Entity):
    def __init__(self, pos):
        super().__init__(
            model='plane',
            position=pos,
            scale=0.95,
            texture='white_cube',
            collider='box',
            color=color.random_color()
        )
        self.is_mine = random.random() > 0.8
        self.active = False

    def update(self):
        # Distant-based glow
        dist = distance(self.world_position, player.position)
        if dist < 3:
            self.animate_y(0.5, duration=0.2)
            if self.is_mine:
                self.color = color.red
            else:
                self.color = color.cyan
        else:
            self.animate_y(0, duration=0.5)
            self.color = color.dark_gray

# Create a massive 20x20 floor of reacting logic tiles
for x in range(-10, 10):
    for z in range(-10, 10):
        LogicTile(pos=(x, 0, z))

# --- PLAYER CONTROLLER ---
player = FirstPersonController(model='cube', z=-10, color=color.orange)
player.cursor.visible = False

# --- THE "BOREDOM" EVENT ---
def input(key):
    if key == 'q' or key == 'escape':
        quit()
    
    if key == 'space': # "Ascension Mode"
        player.animate_y(player.y + 10, duration=2, curve=curve.out_expo)

    if key == 'f': # The Bore-Reveal (F to Pay Respects to the Puzzle)
        for e in scene.entities:
            if isinstance(e, SudokuCrystal) and e.val == 0:
                e.text = str(random.randint(1,9))
                e.color = color.gold
                e.shake()

# --- UI OVERLAY ---
info = Text(
    text='A E T H E R\n[WASD] Navigate | [SPACE] Ascend | [F] Resolve Chaos',
    position=(-0.85, 0.45),
    scale=1.5,
    color=color.white
)

app.run()