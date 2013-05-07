# -*- coding: utf-8 -*-

__author__ = 'Mario Cares <mcares@puertosolutions.cl>'

import tweepy, itertools

class Class_UsuarioDAO:

    def getNombreUsuario(self):
        return self.API.me().screen_name

    def getID(self):
        return  self.API.me().id

    def getScreenUserName(self):
        return self.API.me().screen_name

    def getID(self):
        return self.API.me().id

    def getFollowers(self):
        followers = self.API.followers_ids(screen_name=self.getScreenUserName())
        for page in self.paginate(followers, 100):
            results = self.API.lookup_users(user_ids=page)
            dict = {}
            for result in results:
                dict[result.id] = {
                    "Avatar":result.profile_image_url,
                    "ScreenName":result.screen_name,
                }
            return dict

    def paginate(self, iterable, page_size):
        while True:
            i1, i2 = itertools.tee(iterable)
            iterable, page = (itertools.islice(i1, page_size, None),
                              list(itertools.islice(i2, page_size)))
            if len(page) == 0:
                break
            yield page

    def __init__(self, API):
        self.API = API