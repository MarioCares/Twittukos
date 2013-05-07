# -*- coding: utf-8 -*-

__author__ = 'Mario Cares <mcares@puertosolutions.cl>'

import tweepy
import os.path

class Class_WinPrincipalDAO:

    def __init__(self):
        pass

    def getAPI(self):
        return self.API

    def Conectar(self):
        import json, base64
        try:
            json_data = open(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config/Variables.json")))
            data = json.load(json_data)
            ConsumerKey = str(data["Consumer_key"])
            ConsumerSecret = base64.decodestring(str(data["Consumer_secret"]))
            json_data.close()

            json_data = open(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config/Credenciales.json")))
            data = json.load(json_data)
            AccessKey = str(data["ACCESS_KEY"])
            #AccessKey = "asd"
            AccessSecret = base64.decodestring(str(data["ACCESS_SECRET"]))
            json_data.close()

            Auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
            Auth.set_access_token(AccessKey, AccessSecret)

            self.API = tweepy.API(Auth)

            if(self.API.verify_credentials()):
                return self.API
            else:
                return {"Tipo":0, "Mensaje":"Error al conectar", "Detalle":self.API.__dict__.__str__()}
        except tweepy.TweepError as e :
            print e.message
            print e.__str__()
            return {"Tipo":0, "Mensaje":"Error al leer Variables", "Detalle":e.__str__()}