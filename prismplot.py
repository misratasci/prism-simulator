import matplotlib.pyplot as plt
import functions as f

x = []
y = []
angle = f.rad(-10)
while angle < f.rad(10):
    x.append(angle)
    prism = f.Prism(angle)
    y.append(100 - (prism.çıkanınduvaravurduğuyer[1] - 50)/4)
    angle += f.rad(1)
plt.plot(x,y)
fig = plt.gcf()
fig.set_size_inches(5,5)
plt.show()
