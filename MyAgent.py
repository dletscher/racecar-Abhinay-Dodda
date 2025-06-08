import random

class Agent:
    def chooseAction(self, observations, possibleActions):
        lidar=observations['lidar']
        vel=observations['velocity']
        
        l45=lidar[0]
        c=lidar[2]
        r45=lidar[4]
        h=0.07

        if r45-l45>0.1:
            dir='right'
        elif l45-r45>0.1:
            dir='left'
        else:
            dir='straight'


        if vel==0:
            speed='accelerate'
        elif vel<0.2 and c>0.5 and dir=='straight':
            speed='accelerate'
        elif l45<h or r45<h:
            speed='brake'
        else:
            speed='coast'
        
        return (dir,speed)
