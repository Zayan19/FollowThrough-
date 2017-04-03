from datetime import datetime
import urllib, urllib2


class Shot_Handler:
    """ Wrapper for posting data (From python module) """
    def __init__(self, entry_angle, exit_angle, arc_height, zone = 0):
        self.entry_angle = entry_angle
        self.exit_angle = exit_angle
        self.arc_height = arc_heigth
        self.zone = zone

        self.over_under = 'over' if arc_height > 4 else 'under'
        self.zone = None
        self.user_id = None

    def post(self, url):
        """ Post data given by constructor to api """
        data_to_post = {}

        assert self.user_id is not None, "Must login before posting to server"
        assert self.zone is not None, "Must set zone before posting to server"

        data_to_post['user_id'] = self.user_id
        data_to_post['zone'] = self.zone
        data_to_post['over_under_shot'] = self.over_under
        data_to_post['exit_angle'] = self.exit_angle
        data_to_post['entry_angle'] = self.entry_angle
        data_to_post['arc_height'] = self.arc_height
        data_to_post['made'] = self.made
        data_to_post['time_of_shot'] = _format_datetime(datetime.now())

        url_values = urllib.urlencode(data_to_post)

        page = None
        try:
           page = urllib2.urlopen(url, url_values)
        except urllib2.HTTPError as e:
            print e.read()

        return page.read()

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_zone(self, zone):
        self.zone = zone

    def _format_datetime(date):
        str_date = str(date)
        i = str_date.index('.')
        return str_date[:i]


class Login_Handler:
    """ Wrapper for posting data (From python module) """
    def __init__(self, username, password):
        self.password = password
        self.username = username

    def post(self, url):
        """ Post data given by constructor to api """
        data_to_post = {}

        assert self.user_id is not None, "Must login before posting to server"
        assert self.zone is not None, "Must set zone before posting to server"

        data_to_post['username'] = self.username
        data_to_post['password'] = self.password


        url_values = urllib.urlencode(data_to_post)

        page = None
        try:
           page = urllib2.urlopen(url, url_values)
        except urllib2.HTTPError as e:
            print e.read()

        return page.read()

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_zone(self, zone):
        self.zone = zone

    def _format_datetime(date):
        str_date = str(date)
        i = str_date.index('.')
        return str_date[:i]

class Basket_Handler:
    """ Wrapper for posting data (From arduino module) """

    def __init__(self, time_of_shot):
        self.time_of_shot = time_of_shot
        self.user_id = None

    def post(self, url):
        """ Post data given by constructor to api """
        data_to_post = {}

        assert self.user_id is not None, "Must login before posting to server"

        data_to_post['user_id'] = self.user_id
        data_to_post['time_of_shot'] = self.time_of_shot

        url_values = urllib.urlencode(data_to_post)

        page = None
        try:
           page = urllib2.urlopen(url, url_values)
        except urllib2.HTTPError as e:
            print e.read()

        return page.read()

    def set_user_id(self, user_id):
        self.user_id = user_id
