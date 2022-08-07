import sys, pygame

pygame.init()
font = pygame.font.SysFont('arial', 13, False, False)
size = width, height = 1500, 500
screen = pygame.display.set_mode(size)
def drawline(line, color):
    pygame.draw.line(screen, color, line[0], line[1], 1)
class Tick():
    def __init__(self, type, value, startpoint):
        self.value = value
        if type == "x":
            self.line = (startpoint, (startpoint[0], startpoint[1]+5))
            self.valueposition = (startpoint[0]-10, startpoint[1]+10)
        elif type == "y":
            self.line = (startpoint, (startpoint[0]-5, startpoint[1]))
            self.valueposition = (startpoint[0]-40, startpoint[1]-7)
    def draw(self, color):
        drawline(self.line, color)
        valueyazısı = font.render(f"{'%.2f' % self.value}", True, color)
        screen.blit(valueyazısı, self.valueposition)
class Axis():
    def __init__(self, type, startpoint, length, title, values):
        self.title = title
        self.length = length
        self.type = type
        if type == "x":
            self.titleposition = (startpoint[0]+115, startpoint[1]+30)
            self.axis = (startpoint, (startpoint[0]+length, startpoint[1]))
        elif type == "y":
            self.titleposition = (startpoint[0]-65, startpoint[1]-170)
            self.axis = (startpoint, (startpoint[0], startpoint[1]-length))
    def draw(self, color):
        titletext = font.render(self.title, True, color)
        if self.type == "y":
            titletext = pygame.transform.rotate(titletext, 90)
        screen.blit(titletext, self.titleposition)
        drawline(self.axis, color)
class Plotline():
    def __init__(self, xaxis, yaxis, xvalues, yvalues):
        self.xvalues = xvalues
        self.yvalues = yvalues
        self.xaxis = xaxis
        self.yaxis = yaxis
        self.points = []
        for i in range(len(self.xvalues)):
            self.points.append((self.xposition(self.xvalues[i]), self.yposition(self.yvalues[i])))
        self.lines = []
        for i in range(len(self.points)-1):
            self.lines.append((self.points[i], self.points[i+1]))
        self.ticks = []
        for i in range(0, int(self.xaxis.length/75)):
                tickposition = self.xposition(self.xvalues[::int(len(self.xvalues)/(self.xaxis.length/75))][i])
                tickvalue = self.xvalue(tickposition)
                tick = Tick("x", tickvalue, (tickposition, self.xaxis.axis[1][1]))
                self.ticks.append(tick)
        for i in range(0, int(self.yaxis.length/75)):
                tickposition = self.yposition(self.yvalues[::int(len(self.yvalues)/(self.yaxis.length/75))][i])
                tickvalue = self.yvalue(tickposition)
                tick = Tick("y", tickvalue, (self.yaxis.axis[1][0], tickposition))
                self.ticks.append(tick)
    def xposition(self, value):
        return self.xaxis.axis[0][0]+(-min(self.xvalues)+value)*(self.xaxis.length/(max(self.xvalues)-min(self.xvalues)))
    def yposition(self, value):
        return self.yaxis.axis[0][1]-(-min(self.yvalues)+value)*(self.yaxis.length/(max(self.yvalues)-min(self.yvalues)))
    def xvalue(self, position):
        return (position-self.xaxis.axis[0][0])/(self.xaxis.length/(max(self.xvalues)-min(self.xvalues)))+min(self.xvalues)
    def yvalue(self, position):
        return (-position+self.yaxis.axis[0][1])/(self.yaxis.length/(max(self.yvalues)-min(self.yvalues)))+min(self.yvalues)
    def draw(self, color, maxcolor):
        maxline = [(0,500), (0,500)]
        for line in self.lines:
            if line[0][1] < maxline[0][1]:
                maxline = line
            drawline(line,color)
        drawline(maxline, maxcolor)
        
class Plot():
    def __init__(self, startpoint, axislength, xaxistitle, yaxistitle, xvalues, yvalues):
        self.xaxis = Axis("x", startpoint, axislength, xaxistitle, xvalues)
        self.yaxis = Axis("y", startpoint, axislength, yaxistitle, yvalues)
        self.plotline = Plotline(self.xaxis, self.yaxis, xvalues, yvalues)
    def draw(self, axiscolor, linecolor):
        self.xaxis.draw(axiscolor)
        self.yaxis.draw(axiscolor)
        self.plotline.draw(linecolor, linecolor)
        for tick in self.plotline.ticks:
            tick.draw(axiscolor)
