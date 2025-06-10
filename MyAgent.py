import random

class Agent:
    def chooseAction(self, observations, possibleActions):
        lidar=observations['lidar']
        vel=observations['velocity']
        
        l45=lidar[0]
        c=lidar[2]
        r45=lidar[4]
        h=0.7 + vel + 0.2 *(min(l45,r45))

        if r45-l45>0.2:
            dir='right'
        elif l45-r45>0.2:
            dir='left'
        else:
            dir='straight'


        if vel==0:
            speed='accelerate'
        
        elif  ( l45<=h or r45<=h ):
            speed='brake'
        elif vel<0.35 and c>0.45 :#and dir=='straight':
            speed='accelerate'
        else:
            speed='coast'
        
        return (dir,speed)
