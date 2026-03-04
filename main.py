from ursina import *
import numpy as np
import random
import math

app = Ursina()
window.title = "Panzer III - WWII Semi Realistic"

# =============================
# TERRAIN CON RUMORE
# =============================

def generate_terrain(size=60, scale=4):
    terrain_parent = Entity()
    heights = {}

    for x in range(size):
        for z in range(size):
            height = np.sin(x * 0.2) * np.cos(z * 0.2) * 2
            height += np.random.uniform(-0.3, 0.3)

            heights[(x, z)] = height

            Entity(
                parent=terrain_parent,
                model='cube',
                scale=(1, 1, 1),
                position=(x - size/2, height, z - size/2),
                color=color.rgb(80, 120 + int(height*10), 80),
                collider='box'
            )

    return terrain_parent, heights

terrain, heightmap = generate_terrain()

# =============================
# BULLET (BALISTICA CON GRAVITÀ)
# =============================

class Bullet(Entity):
    def __init__(self, position, direction):
        super().__init__(
            model='sphere',
            scale=0.2,
            color=color.black,
            position=position
        )
        self.velocity = direction * 25
        self.gravity = Vec3(0, -9.8, 0)
        self.lifetime = 5

    def update(self):
        self.velocity += self.gravity * time.dt
        self.position += self.velocity * time.dt
        self.lifetime -= time.dt

        hit = self.intersects()
        if hit.hit:
            if hasattr(hit.entity, "hp"):
                hit.entity.hp -= 40
            destroy(self)

        if self.lifetime <= 0:
            destroy(self)

# =============================
# TANK BASE
# =============================

class Tank(Entity):
    def __init__(self, position=(0,2,0), enemy=False):
        super().__init__(position=position)
        self.enemy = enemy
        self.hp = 100

        # Corpo
        self.body = Entity(parent=self,
                           model='cube',
                           scale=(2.5,0.7,4),
                           color=color.rgb(100,100,100),
                           collider='box')

        # Torretta
        self.turret = Entity(parent=self,
                             model='cube',
                             scale=(1.5,0.5,1.5),
                             y=0.8)

        # Cannone
        self.barrel = Entity(parent=self.turret,
                             model='cube',
                             scale=(0.2,0.2,2.5),
                             z=1.8)

        # Cingoli
        Entity(parent=self, model='cube',
               scale=(0.5,0.4,4),
               x=-1.6, color=color.black)

        Entity(parent=self, model='cube',
               scale=(0.5,0.4,4),
               x=1.6, color=color.black)

        self.speed = 6
        self.turn_speed = 60

    def update(self):
        if self.hp <= 0:
            self.color = color.dark_gray
            return

        if not self.enemy:
            self.player_control()
        else:
            self.ai_behavior()

    # ================= PLAYER =================
    def player_control(self):
        if held_keys['w']:
            self.position += self.forward * time.dt * self.speed
        if held_keys['s']:
            self.position -= self.forward * time.dt * self.speed
        if held_keys['a']:
            self.rotation_y -= self.turn_speed * time.dt
        if held_keys['d']:
            self.rotation_y += self.turn_speed * time.dt

        if mouse.world_point:
            self.turret.look_at(mouse.world_point)

    # ================= AI =================
    def ai_behavior(self):
        if player.hp <= 0:
            return

        self.look_at(player.position)
        self.position += self.forward * time.dt * 3

        self.turret.look_at(player.position)

        if distance(self.position, player.position) < 25:
            if random.random() < 0.01:
                self.shoot()

    def shoot(self):
        if self.hp <= 0:
            return

        direction = self.barrel.forward
        Bullet(self.barrel.world_position + direction*2, direction)

# =============================
# CREA GIOCATORI
# =============================

player = Tank(position=(0,3,0))
enemy = Tank(position=(15,3,15), enemy=True)

# =============================
# CAMERA TERZA PERSONA
# =============================

camera.parent = player
camera.position = (0, 10, -20)
camera.rotation_x = 25

# =============================
# LUCI
# =============================

DirectionalLight(y=20, z=10, shadows=True)
AmbientLight(color=color.rgba(100,100,100,0.4))

# =============================
# HUD
# =============================

hp_text = Text(text="HP: 100", position=(-0.85,0.45), scale=2)

def update():
    hp_text.text = f"HP: {int(player.hp)}"

def input(key):
    if key == 'space':
        player.shoot()

app.run()
