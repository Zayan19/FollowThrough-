


import urllib, urllib2
import ball
import requests
# print ("Starting program");
def returnData():

    shot_stats = ball.runVideo(False, 'test_videos/FT_make.MOV')

    # print "Data recieved from OpenCV:"
    # print shot_stats

    entry_angle = (shot_stats[0])
    exit_angle = (shot_stats[1])
    arc_height = (shot_stats[2])
    zone = '3'
    over_under = ''
    if (arc_height > 4):
        over_under = 'over'
    else:
        over_under = 'under'
    made = True


    data_to_post = {}
    # data_to_post['user_id'] = 1
    # data_to_post['zone'] = zone
    # data_to_post['over_under_shot'] = over_under
    data_to_post['exit_angle'] = exit_angle
    data_to_post['entry_angle'] = entry_angle
    data_to_post['arc_height'] = arc_height
    # data_to_post['made'] = made

    # url_values = urllib.urlencode(data_to_post)

    url_api='http://54.145.183.186/api/shot'    #the url you want to POST to
    # req=urllib2.Request(url_api, url_values)
    # req.add_header("Content-type", "application/x-www-form-urlencoded")

    # print "Will post to server when server will properly parse data"

    # try:
    #     urllib2.urlopen(req)
    # except urllib2.HTTPError as e:
    #     # print e.code
    #     print e.read()

    # page=urllib2.urlopen(req).read()


    # url = 'http://url.com'
    # query = {'field': value}
    # res = requests.post(url_api, data={"Zone","3"})
    # print(res.text)
    print( entry_angle);
    print( exit_angle);
    print (arc_height);


returnData()
