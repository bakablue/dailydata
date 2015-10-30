#! /usr/bin/env python3

from db_manager import *

import os.path
import dailymotion

#def dailydata(idVideo):
#    d = dailymotion.Dailymotion
#    fields = { 'fields', 'title' };
#    d.get('/video/' + idVideo, fields)



if __name__ == "__main__":
    if not os.path.exists('test.db'):
        create_db()

    d = dailymotion.Dailymotion()
    data = d.get('/video/x26ezj5',
                    {
                        'fields' :
                        'title,description,thumbnail_url,duration,views_total'
                    }
                )
    if not is_video_present('x26ezj5'):
        video_data = ('x26ezj5', data['title'], data['description'],
                data['duration'], data['views_total'], data['thumbnail_url'],)
        insert_data(video_data)
