import time
import os.path

class shot_handler:
    shot_queue = []
    player = None
    def __init__(self, player, shotfile="/etc/shots.csv"):
        # TODO: Load all old shots from file and try to post
        if not (os.path.exists(shotfile) and os.path.isFile(shotfile)):
            return

        self.load_from_file()


    def post_shots():
        # TODO: Post all shots in the shots queue and check for confirmation


    # a player has taken a shot and we want to append the shot to our shot queue
    def shoot():
        shots_queue.append( Shot() )

    def load_from_file(self, shotfile="/etc/shots.csv"):
        f = open(shotfile,'r')
        # load all of the shots into the shot_queue
        for line in f:
            params = line.split(",")

            shots_queue.append((params[0],params[1]))

    def save_to_file():



# Define what a shot is
# Tracks who took the shot, and the time at which it was taken
class Shot:
    def __init__(self, user_id, time="now"):
        if (time == "now"):
            self.time = time.strftime('%Y-%m-%d %H:%M:%S')
        else:
            self.time = time

        self.user_id = user_id
