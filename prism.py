import sys, pygame, math, plot


pygame.init()

size = width, height = 1000, 500
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont('arial', 13, False, False)
black = 0,0,0
white = 255,255,255
red = 200,0,0
blue = 0,0,200
green = 0,150,0
center = (250,250)
n1 = 1
başlangıçnoktası = (450, 320)
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
    def __init__(self, rotationangle, thetaB = rad(60)):
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
    def draw(self, ışınrengi):
        pygame.draw.polygon(screen, black, self.triangle, 1)
        pygame.draw.line(screen, ışınrengi, başlangıçnoktası, self.ışınınilkvurduğuyer, 1)
        pygame.draw.line(screen, ışınrengi, self.ışınınilkvurduğuyer, self.ışınınikincivurduğuyer, 1)
        pygame.draw.line(screen, ışınrengi, self.ışınınikincivurduğuyer, self.çıkanınduvaravurduğuyer, 1)

rotationangle = 0
prism = Prism(rotationangle)
prism.draw(red)
thetaB = rad(60)
def duvarçiz():
    pygame.draw.line(screen, black, duvar[0], duvar[1], 1)
    text1 = font.render("0", True, black)
    text2 = font.render("100", True, black)
    screen.blit(text2, [duvar[0][0] + 5, duvar[0][1] - 5])
    screen.blit(text1, [duvar[1][0] + 5, duvar[1][1] - 5])
def yazılarıyaz():
    duvarüstündekiyerinyazısı = font.render(f"Çarptığı yer = {'%.2f' % (100 - (prism.çıkanınduvaravurduğuyer[1] - 50)/4)}", True, black)
    screen.blit(duvarüstündekiyerinyazısı, [330, 20])
    ışınprismadannekadargeçiyor = font.render(f"Prisma içi mesafe (tabana göre) = % {'%.2f' % (dist(prism.ışınınilkvurduğuyer, prism.ışınınikincivurduğuyer)/dist(prism.sağnokta, prism.solnokta)*100)}", True, black)
    screen.blit(ışınprismadannekadargeçiyor, [330, 40])
    thetaB = font.render(f"thetaB = {'%.2f' % (deg(prism.thetaB))}", True, black)
    screen.blit(thetaB, [330, 100])
    theta1 = font.render(f"theta1 = {'%.2f' % (deg(prism.theta1))}", True, black)
    screen.blit(theta1, [330, 120])
    theta2 = font.render(f"theta2 = {'%.2f' % (deg(prism.theta2))}", True, black)
    screen.blit(theta2, [330, 140])
    theta3 = font.render(f"theta3 = {'%.2f' % (deg(prism.theta3))}", True, black)
    screen.blit(theta3, [330, 160])
    theta4 = font.render(f"theta4 = {'%.2f' % (deg(prism.theta4))}", True, black)
    screen.blit(theta4, [330, 180])
    dönmeaçısı = font.render(f"Dönme açısı = {'%.2f' % (deg(rotationangle))}", True, black)
    screen.blit(dönmeaçısı, [330, 200])
    n1yazısı = font.render(f"Dışarının n'i = {'%.2f' % (n1)}", True, black)
    screen.blit(n1yazısı, [330, 60])    
    n2 = font.render(f"Prizmanın n'i = {'%.2f' % (prism.n2)}", True, black)
    screen.blit(n2, [330, 80])
def yönerge():
    yazı = font.render("Sağ-Sol: döndür", False, black)
    screen.blit(yazı, [310, 410])
    yazı = font.render("Yukarı-Aşağı: thetaB'yle oyna", True, black)
    screen.blit(yazı, [310, 430])
    yazı = font.render("W-S: gelen ışını indirip çıkar", True, black)
    screen.blit(yazı, [310, 450])
    yazı = font.render("A-D: duvarı sağa sola oynat", True, black)
    screen.blit(yazı, [310, 470])

def drawline(line, color):
    pygame.draw.line(screen, color, line[0], line[1], 1)
def plotçiz(tb):
    angle = rad(-10)
    xvalues = []
    yvalues = []
    while angle < rad(11):
        xvalues.append(deg(angle))
        prism = Prism(angle, tb)
        yvalue = (100 - (prism.çıkanınduvaravurduğuyer[1] - 50)/4)
        yvalues.append(yvalue)
        angle += rad(0.5)
    plot1 = plot.Plot((600,400), 300, "dönme açısı (deg)", "çarptığı yer", xvalues, yvalues)
    plot1.draw(black, red)
    
    # - buraya thetaB vs prisma içi mesafe grafiği çiz, her thetab için max çarptığı yer 
    # rotationangle 0'a denk geldiğinde prisma içi mesafe kaç oluyor onu.
    # - bir de prisma class inde çok fazla self'le başlayan şey var baya iğrenç onu düzeltebilirsin belki
    # - axis başlıkları tam ortaya gelsin diye pozisyonlarını 
    # (axisin tam ortasının pozisyonu - karakter sayısının yarısı) yap
    

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(white)
    duvarçiz()
    yönerge()
    keys = pygame.key.get_pressed()
    try:
        if keys[pygame.K_LEFT] and prism.çıkanınduvaravurduğuyer[1] < duvar[1][1]:
            rotationangle += rad(0.2)
            prism = Prism(rotationangle, thetaB)
        if keys[pygame.K_RIGHT]:
            rotationangle -= rad(0.2)
            prism = Prism(rotationangle, thetaB)
        if keys[pygame.K_UP] and prism.ışınınilkvurduğuyer[1] > prism.uç[1]:
            thetaB += rad(0.03)
            prism = Prism(rotationangle, thetaB)
        if keys[pygame.K_DOWN] and prism.ışınınilkvurduğuyer[1] < prism.sağnokta[1]:
            thetaB -= rad(0.03)
            prism = Prism(rotationangle, thetaB)
        if keys[pygame.K_s]:
            başlangıçnoktası = (başlangıçnoktası[0], başlangıçnoktası[1] + 0.25)
            prism = Prism(rotationangle, thetaB)
        if keys[pygame.K_w]:
            başlangıçnoktası = (başlangıçnoktası[0], başlangıçnoktası[1] - 0.25)
            prism = Prism(rotationangle, thetaB)
        if keys[pygame.K_a]:
            duvar = (((duvar[0][0] - 0.25), (duvar[0][1])), ((duvar[1][0] - 0.25), (duvar[1][1])))
            prism = Prism(rotationangle, thetaB)
        if keys[pygame.K_d]:
            duvar = (((duvar[0][0] + 0.25), (duvar[0][1])), ((duvar[1][0] + 0.25), (duvar[1][1])))
            prism = Prism(rotationangle, thetaB)
    except:
        pass
    prism.draw(red)
    yazılarıyaz()
    plotçiz(thetaB)
    pygame.display.flip()