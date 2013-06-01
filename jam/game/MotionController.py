from jam.common.Vec3d import Vec3d
from collections import deque

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
    
    distance = 0.
    
    points = deque()
    for x in range(steps):
        points.append(Vec3d(f))
        delta = fd + fdd_per_2 + fddd_per_6
        distance += delta.length
        f += delta
        fd += fdd + fddd_per_2
        fdd += fddd
        fdd_per_2 += fddd_per_2
    points.append(Vec3d(f))
    
    return points, distance

class MotionController:
    def __init__(self, owner):
        self.owner = owner
        self.path = None
        self.afterMove = None
        self.speed = 1.
    
    def update(self, delta):
        if self.path is not None:
            speed = self.speed * delta
            
            goal = self.path[0]
            rel = (goal - self.owner.pos).normalized() * speed
            self.move(rel)
            
            if self.owner.pos.get_distance(goal) <= speed:
                self.path.popleft()
                if len(self.path) == 0:
                    self.path = None
                    if self.afterMove is not None:
                        self.afterMove(self.owner)
                        self.afterMove = None
        
    def move(self, relative):
        self.owner.capsule.move(relative)

    def moveToPosition(self, pos, duration):
        self.moveAlongPath([Vec3d(self.owner.pos), Vec3d(pos), Vec3d(pos)], duration)
        
    def moveAlongPath(self, path, duration):
        if len(path) != 3:
            print("Invalid path length")
            self.path = None
            return
            
        self.path, dist = calculate_bezier([Vec3d(self.owner.pos)] + path)
        self.speed = dist / duration
        self.path.popleft()
        
    def afterMoveDo(self, function):
        self.afterMove = function
        
    def isMoving(self):
        return self.path is not None