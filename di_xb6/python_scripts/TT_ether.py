from __future__ import print_function
import requests
import os
import datetime
import sys
from pprint import pprint
from time import sleep

#IP address of turn table
tt = '192.168.0.100'

class Turntable ():
    '''this class operates a turntable'''
    def __init__(self,address,action="pos",enable="1",pos_target="0",vel_target="10000"):
        self.address=address
        self.data=requests.get("http://{}/api/turntable".format(self.address))
        self.action=action      
        self.enable=enable
        self.pos_target=pos_target
        self.vel_target=vel_target

    def set_position(self,pos_target):
        '''this method will set the turntable to the given pos_target'''
        if pos_target > 720:
            raise NameError('Position may not exceed 720')
        set_position_submission={
            "action":"pos",
            "enable":"1",
            "pos_target":pos_target,
            "vel_target":self.vel_target
            }     
        x = requests.post("http://{}/api/turntable".format(self.address),json=set_position_submission)
        return x

    def get_info(self):
        '''this method will get return the info on the turntable'''
        x=requests.get("http://{}/api/turntable".format(self.address))
        return x

if __name__=='__main__':
    ##simple program to set turn table to given set_position
    turntable=Turntable(tt)
    # info = turntable.get_info()
    # pprint(info.json())
    spin_value = sys.argv[1]
    spin_value = int(spin_value)
    pos=turntable.set_position(spin_value) ##set any number for the position of the turntable
    # pprint(pos.json())
    sleep(2)
    #info = turntable.get_info()
    # pprint(info.json())    
