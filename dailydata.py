#! /usr/bin/env python3

from db_manager import *

import os.path
import sys
import getopt
import dailymotion

def print_usage():
    print("Usage: ./dailydata -v <idVideo>")

def retrieveData(idVideo):
    # Create database if it doesn't exists
    if not os.path.exists('videos_data.db'):
        create_db()

    d = dailymotion.Dailymotion()
    data = d.get('/video/' + idVideo,
                    {
                        'fields' :
                        'title,description,thumbnail_url,duration,views_total'
                    }
                )
    video_data = get_video_infos(idVideo)
    if video_data is None:
        video_data = (idVideo, data['title'], data['description'],
                data['duration'], data['views_total'], data['thumbnail_url'],)
        insert_data(video_data)

    print_data(video_data)

def dailydata(argv):

    if not argv:
        print_usage()
        sys.exit(1)
    try:
        opts, args = getopt.getopt(argv, 'hv:', ['video='])
    except getopt.GetoptError:
        print_usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit()
        elif opt in ('-v', '--video'):
            idVideo = arg
            retrieveData(idVideo)

if __name__ == "__main__":
    dailydata(sys.argv[1:])
