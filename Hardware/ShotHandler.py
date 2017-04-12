import time as time_m
import os.path
from Networking import
class ShotHandler:
    shot_queue = []
    player = None
    shot_allowed = True
    shot_file = "/etc/shots.csv"
    def __init__(self, player, shot_file="/etc/shots.csv"):

        self.player = player
        self.shot_file = shot_file

        if not (os.path.exists(shot_file) and os.path.isFile(shot_file)):
            return

        self.load_from_file()


    def post_shots(self):
        basket_handler = BasketHandler(self.shot_queue[0])
        del self.shot_queue[0]

    # a player has taken a shot and we want to append the shot to our shot queue
    def shoot(self):
        if self.shot_allowed:
            self.shot_queue.append( Shot(self.player) )
            print "[EVENT] Shot taken at " , self.shot_queue[-1].get_time() , " by ", self.shot_queue[-1].get_user_id()
        else:
            print "[EVENT] DISSALLOWED! Shot taken at " , self.shot_queue[-1].get_time() , " by ", self.shot_queue[-1].get_user_id()

    def load_from_file(self):
        f = open(self.shot_file,'r')
        # load all of the shots into the shot_queue
        for line in f:
            params = line.split(",")
            shot_queue.append((params[0],params[1]))

        f.close()

    def save_to_file(self):
        f = open(self.shot_file,'w')
        # load all of the shots into the shot_queue
        for shot in shot_queue:
            f.write(shot.get_user_id(), "," , shot.get_time());
        f.close()

    # Getters and setters for what file to save too
    def get_shot_file(self):
        return self.shot_file
    def set_shot_file(self, shot_file):
        self.shot_file = shot_file

# Define what a shot is
# Tracks who took the shot, and the time at which it was taken
class Shot:
    def __init__(self, user_id, time1="now"):
        if (time1 == "now"):
            self.time = time_m.strftime('%Y-%m-%d %H:%M:%S')
        else:
            self.time = time1

        self.user_id = user_id

    def __str__(self):
        return self.get_user_id(), "," , self.get_time()

    def get_time(self):
        return self.time
    def get_user_id(self):
        return self.user_id
