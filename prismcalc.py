import math
def deg(angle):
    return angle*180/math.pi
def rad(angle):
    return angle*math.pi/180
thetaB = rad(65)
n1 = 1
n2 = n1*(math.tan(thetaB))
theta1 = thetaB
theta2 = math.asin(n1*math.sin(theta1)/n2)
theta3 = math.pi - 2*thetaB - theta2
theta4 = math.asin(n2*math.sin(theta3)/n1)

print(f"n1 = {n1}\nn2 = {n2}\ntheta1 = {deg(theta1)}\ntheta2 = {deg(theta2)}\ntheta3 = {deg(theta3)}\ntheta4 = {deg(theta4)}\nthetaB = {deg(thetaB)}\n")