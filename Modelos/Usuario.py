# -*- coding: utf-8 -*-

__author__ = 'Mario Cares <mcares@puertosolutions.cl>'


class Class_Usuario :

    def __init__(self, nombre, _id, screenname):
        self.NombreUsuario = nombre
        self.ID = _id
        self.ScreenName = screenname

"""
from pprint import pprint
from inspect import getmembers
pprint(getmembers(api.me()))
 {
   'contributors_enabled': False,
   'created_at': datetime.datetime(2009, 9, 12, 1, 7, 38),
   'default_profile': False,
   'default_profile_image': False,
   'description': u'Ingeniero Inform\xe1tico Titulado #Inacapino Fan\xe1tico del For:Each. PseudoBajista y hace boomerangs =D. Usuario #Linux Part Time || Imprimado con @Darkylicius_ :B',
   'entities': {'description': {'urls': []},
                'url': {'urls': [{'expanded_url': None,
                                  'indices': [0, 28],
                                  'url': 'http://danlaho.wordpress.com'}]}},
   'favourites_count': 11,
   'follow_request_sent': False,
   'followers_count': 145,
   'following': False,
   'friends_count': 75,
   'geo_enabled': True,
   'id': 73534029,
   'id_str': '73534029',
   'is_translator': False,
   'lang': 'es',
   'listed_count': 9,
   'location': '/home/Chile/Iquique',
   'name': 'Mario Cares',
   'notifications': False,
   'profile_background_color': '352726',
   'profile_background_image_url': 'http://a0.twimg.com/images/themes/theme5/bg.gif',
   'profile_background_image_url_https': 'https://si0.twimg.com/images/themes/theme5/bg.gif',
   'profile_background_tile': False,
   'profile_banner_url': 'https://si0.twimg.com/profile_banners/73534029/1348533218',
   'profile_image_url': 'http://a0.twimg.com/profile_images/1427935795/mario_normal.jpg',
   'profile_image_url_https': 'https://si0.twimg.com/profile_images/1427935795/mario_normal.jpg',
   'profile_link_color': 'D02B55',
   'profile_sidebar_border_color': '829D5E',
   'profile_sidebar_fill_color': '99CC33',
   'profile_text_color': '3E4415',
   'profile_use_background_image': True,
   'protected': False,
   'screen_name': 'Luk0s',
   'status': <tweepy.models.Status object at 0x27b3910>,
   'statuses_count': 9878,
   'time_zone': 'Santiago',
   'url': 'http://danlaho.wordpress.com',
   'utc_offset': -14400,
   'verified': False}),
"""