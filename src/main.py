import numpy as np
import matplotlib as plt
import matplotlib.animation as ani

class Sim():
    def __init__(self, timeStep):
        self.robot_element = []
        self.env_element = []
        self.time_step = timeStep

    def add_robot_element(self, element):
        self.robot_element.append(element)

    def add_env_element(self, element):
        self.env_element.append(element)

    def textOutput(self):
        output = ""
        return output
    
    def run_forever(self):
        for i in range(len(self.robot_element)):
            self.robot_element[i].update(self.time_step)
        
        for i in range(len(self.env_element)):
            self.env_element[i].update(self.time_step)


    def run_till(self, total_steps):
        for i in range(total_steps):
            self.run_forever()

class SinglePendulum():
    def __init__(self, length, theta, theta_vel, g=9.8):
        self.length = length
        self.gravity = g
        self.theta = theta
        self.theta_velocity = theta_vel

        self.past_pos = []
        self.past_vel = []

    def getLength(self): return self.length
    def getGravity(self): return self.gravity
    def getTheta(self): return self.theta
    def getThetaVel(self): return self.theta_velocity
    def getPastPos(self): return self.past_pos
    def getPastVel(self): return self.past_vel

    def update(self, time_step):
        self.past_pos.append(self.theta)
        self.past_vel.append(self.theta_velocity)
        theta_accel = -(self.gravity/self.length)*np.sin(self.theta)
        self.theta_velocity += time_step*theta_accel
        self.theta += time_step*self.theta_velocity




sim = Sim(0.01)
leg = SinglePendulum(1, 45, 0)
sim.add_robot_element(leg)
sim.run_till(10000)
x = leg.getPastPos()
for i in range(len(x)):
    print(x[i])