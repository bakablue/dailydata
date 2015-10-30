#! /usr/bin/env python3

from db_manager import *

import os.path
import sys
import getopt
import dailymotion

def print_usage():
    print("Usage: ./dailydata -v <idVideo>")

def retrieveData(idVideo):
    """
        Retrieve information about the video corresponding to `idVideo`,
        insert it in the database and print it. If the information of the
        video are already in the database, it doesn't query the dailymotion
        api.
    """
    # Create database if it doesn't exists
    if not os.path.exists('videos_data.db'):
        create_db()

    video_data = get_video_infos(idVideo)

    if video_data is None:
        # Query the dailymotion api
        try:
            d = dailymotion.Dailymotion()
            data = d.get('/video/' + idVideo,
                    {
                        'fields' :
                        'title,description,thumbnail_url,duration,views_total'
                    }
                    )
            video_data = (idVideo, data['title'], data['description'],
                    data['duration'], data['views_total'], data['thumbnail_url'],)
            insert_data(video_data)
        except dailymotion.DailymotionApiError as e:
            print("Dailymotion Error: ", e)
            sys.exit(2)

    print_data(video_data)

def dailydata(argv):
    """
        Parse the arguments of the program and call the right function.
    """
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
            try:
                retrieveData(idVideo)
            except sqlite3.Error as e:
                print("Sqlite Error: ", e)
                sys.exit(2)

if __name__ == "__main__":
    dailydata(sys.argv[1:])
