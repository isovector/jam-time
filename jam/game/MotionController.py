from jam.common.Vec3d import Vec3d
from collections import deque

EPSILON = 0.01

# from http://www.pygame.org/wiki/BezierCurve
def calculate_bezier(p, steps = 30):
    t = 1.0 / steps
    temp = t*t
    
    f = p[0]
    fd = 3 * (p[1] - p[0]) * t
    fdd_per_2 = 3 * (p[0] - 2 * p[1] + p[2]) * temp
    fddd_per_2 = 3 * (3 * (p[1] - p[2]) + p[3] - p[0]) * temp * t
    
    fddd = 2 * fddd_per_2
    fdd = 2 * fdd_per_2
    fddd_per_6 = fddd_per_2 / 3.0
    
    points = deque()
    for x in range(steps):
        points.append(Vec3d(f))
        f += fd + fdd_per_2 + fddd_per_6
        fd += fdd + fddd_per_2
        fdd += fddd
        fdd_per_2 += fddd_per_2
    points.append(Vec3d(f))
    
    return points

class MotionController:
    def __init__(self, owner):
        self.owner = owner
        self.path = None
    
    def update(self, delta):
        if self.path is not None:
            goal = self.path[0]
            rel = (goal - self.owner.pos).normalized() * delta
            self.move(rel)
            if self.owner.pos.get_distance(goal) < EPSILON:
                self.path.popleft()
                if len(self.path) == 0:
                    self.path = None
        
    def move(self, relative):
        self.owner.capsule.move(relative)

    def moveToPosition(self, pos):
        self.moveAlongPath([Vec3d(self.owner.pos), Vec3d(pos), Vec3d(pos)])
        
    def moveAlongPath(self, path):
        if len(path) != 3:
            print("Invalid path length")
            self.path = None
            return
            
        self.path = calculate_bezier([Vec3d(self.owner.pos)] + path)
        self.path.popleft()