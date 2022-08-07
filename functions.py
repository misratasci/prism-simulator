import math
center = (250,250)
başlangıçnoktası = (450, 320)
n1 = 1
duvar = ((30, 50), (30, 450))

def rad(angle):
    return angle*math.pi/180
def triangle(thetaB, height):
    tip = (center[0], center[1] - 2/3*height)
    left = (center[0] + height/math.tan(thetaB), center[1] + height/3)
    right = (center[0] - height/math.tan(thetaB), center[1] + height/3)
    return [tip, right, left] 
def slope(p1,p2):
    if p1[0] - p2[0] != 0:
        return (p1[1] - p2[1])/(p2[0] - p1[0])
    else:
        return "Infinite"
def slopeofline(line):
    if line[0][0]- line[1][0] != 0:
        return (line[0][1] - line[1][1])/(line[1][0] - line[0][0])
    else:
        return "Infinite"
def yataylaaçısı(line):
    if slopeofline(line) != "Infinite":
        açı = math.atan(slopeofline(line))
        if açı < 0:
            açı += math.pi
        return açı
    else:
        return math.pi/2
def rotate(point, pivot, angle):
    line = (pivot, point)
    if point[0] >= pivot[0] and pivot[1] >= point[1]:
        newpoint = (point[0] - (math.cos(yataylaaçısı(line)) - math.cos(yataylaaçısı(line) + angle))*dist(point,pivot), point[1] - (math.sin(yataylaaçısı(line) + angle) - math.sin(yataylaaçısı(line)))*dist(point, pivot))
    else:
        newpoint = (point[0] + (math.cos(yataylaaçısı(line)) - math.cos(yataylaaçısı(line) + angle))*dist(point,pivot), point[1] + (math.sin(yataylaaçısı(line) + angle) - math.sin(yataylaaçısı(line)))*dist(point, pivot))
    return newpoint
def dist(p1,p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
def rotateTriangle(triangle, angle):
    return [rotate(triangle[0], center, angle), rotate(triangle[1], center, angle), rotate(triangle[2], center, angle)]
def equation(line):
    b = - line[0][1] - slopeofline(line)*line[0][0]
    return f"y = {slopeofline(line)}x + {b}"
def deg(angle):
    return angle*180/math.pi
def intersection(line1, line2):
    if slopeofline(line1) == slopeofline(line2):
        return "Parallel"
    elif slopeofline(line1) == "Infinite":
        x = line1[0][0]
        b2 = - line2[1][1] - slopeofline(line2)*line2[1][0]
        y = slopeofline(line2)*x + b2
        return (x, -y)
    elif slopeofline(line2) == "Infinite":
        x = line2[0][0]
        b2 = - line1[1][1] - slopeofline(line1)*line1[1][0]
        y = slopeofline(line1)*x + b2
        return (x, -y)
    else:
        b1 = - line1[1][1] - slopeofline(line1)*line1[1][0]
        b2 = - line2[1][1] - slopeofline(line2)*line2[1][0]
        x = (b2-b1)/(slopeofline(line1)-slopeofline(line2))
        y = slopeofline(line1)*x + b1
        return (x,-y)
def line(point, angle):
    p2 = (point[0] + 100, point[1] - 100*math.tan(angle))
    return (point, p2)
def tersline(point, angle):
    p2 = (point[0] - 300, point[1] + 300*math.tan(angle))
    return (point, p2)
def aralarındakiküçükaçı(l1,l2):
    if yataylaaçısı(l1) > yataylaaçısı(l2):
        açı = yataylaaçısı(l1) - yataylaaçısı(l2)
        if açı > math.pi/2:
            açı = math.pi - açı
            if açı < 0:
                açı += math.pi/2
        return açı
    else:
        açı = yataylaaçısı(l2) - yataylaaçısı(l1)
        if açı > math.pi/2:
            açı = math.pi - açı
            if açı < 0:
                açı += math.pi/2
        return açı
def normalleaçısı(gelen, vurduğuyer):
    normalinyataylaaçısı = yataylaaçısı(vurduğuyer) - math.pi/2
    if normalinyataylaaçısı < 0:
        normalinyataylaaçısı += math.pi
    return aralarındakiküçükaçı(gelen, line(intersection(gelen, vurduğuyer), normalinyataylaaçısı))
def kırılan(gelen, normalleaçısı, vurduğuduvar):
    if yataylaaçısı(vurduğuduvar) < yataylaaçısı(gelen):
        açı = yataylaaçısı(vurduğuduvar) - math.pi/2 - normalleaçısı
    else:
        açı = yataylaaçısı(vurduğuduvar) - math.pi/2 + normalleaçısı
    return tersline(intersection(gelen, vurduğuduvar), açı)

class Prism():
    def __init__(self, rotationangle, thetaB = rad(62)):
        self.height = 200
        self.thetaB = thetaB
        self.gelenışın = line(başlangıçnoktası, math.pi*(3/2)-2*self.thetaB)
        self.n2 = n1*(math.tan(self.thetaB))
        self.triangle = rotateTriangle(triangle(self.thetaB, self.height), rotationangle)
        self.uç = self.triangle[0]
        self.sağnokta = self.triangle[2]
        self.solnokta = self.triangle[1]
        self.taban = (self.sağnokta, self.solnokta)
        self.sağkenar = (self.sağnokta, self.uç)
        self.solkenar = (self.solnokta, self.uç)
        self.ışınınilkvurduğuyer = intersection(self.gelenışın, self.sağkenar)
        self.theta1 = normalleaçısı(self.gelenışın, self.sağkenar)
        self.theta2 = math.asin(n1*math.sin(self.theta1)/self.n2)
        if self.theta1 == 0:
            self.theta2 = self.theta1
        self.kırılan = kırılan((başlangıçnoktası, self.ışınınilkvurduğuyer), self.theta2, self.sağkenar)
        self.ışınınikincivurduğuyer = intersection(self.kırılan, self.solkenar)
        self.theta3 = normalleaçısı(self.kırılan, self.solkenar)
        self.theta4 = math.asin(self.n2*math.sin(self.theta3)/n1)
        if self.theta3 == 0:
            self.theta4 = self.theta3
        self.çıkanınyataylaaçısı = yataylaaçısı(self.solkenar) - math.pi/2 + self.theta4
        self.çıkan = tersline(self.ışınınikincivurduğuyer, self.çıkanınyataylaaçısı)
        self.çıkanınduvaravurduğuyer = intersection(duvar, self.çıkan)
    