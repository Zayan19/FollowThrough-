import time
import os.path

class shot_handler:
    shot_queue = []
    player = None
    def __init__(self, shotfile="/etc/shots.csv"):
        # TODO: Load all old shots from file and try to post
        if not (os.path.exists(shotfile) and os.path.isFile(shotfile)):
            return

        f = open(shotfile,'r')
        # load all of the shots into the shot_queue
        for line in f:
            params = line.split(",")

            shots_queue.append((params[0],params[1],params[2]))

    def post_shots():
        # TODO: Post all shots in the shots queue and check for confirmation

    def shoot():
        # TODO: A player has shot the ball add the new shot to the shot queue


# Define what a shot is
# Tracks who took the shot, and the time at which it was taken
class Shot:
    def __init__(self, user_id):
        self.time = time.time()
        self.user_id = user_id
