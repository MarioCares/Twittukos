# -*- coding: utf-8 -*-

__author__ = 'Mario Cares <mcares@puertosolutions.cl'

try:
    from gi.repository import Gtk
    from gi.repository import WebKit
    import tweepy
    import os.path
except:
    print 'GTK no disponible'

class Class_Autentificacion:

    def getURL(self):
        import json, base64
        try:
            json_data = open(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config/Variables.json")))
            data = json.load(json_data)
            self.auth = tweepy.OAuthHandler(str(data["Consumer_key"]),
                base64.decodestring(str(data["Consumer_secret"])))
            self.URL = self.auth.get_authorization_url()
            json_data.close()
        except Exception as e :
            print 'Error al leer Variables'
            print e.__str__()
            dialog = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.ERROR,
                Gtk.ButtonsType.OK, "Error al leer Variables")
            dialog.format_secondary_text(e.__str__())
            dialog.run()
            dialog.destroy()
            import sys
            sys.exit()

    def mostrar(self):
        Gtk.main()

    def on_autenti_window_delete_event(self, *args):
        Gtk.main_quit(*args)

    def on_btn_auth_pressed(self, *args):
        from tweepy import error
        import sys
        try:
            cod_auth = str(self.builder.get_object('txt_codigo').get_text()).strip()
            self.auth.get_access_token(cod_auth)
            import json, base64
            data = {"ACCESS_KEY": self.auth.access_token.key, "ACCESS_SECRET" : base64.encodestring(self.auth.access_token.secret)}
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config/Credenciales.json")), 'w') as out:
                json.dump(data, out)
                dialog = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Cliente Autenticado.\nPuedes iniciar sesión normalmente :)")
                dialog.format_secondary_text("Cierra la ventana para continuar")
                dialog.run()
                dialog.destroy()
        except error.TweepError as e:
            print e.__str__()
            dialog = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.ERROR,
                Gtk.ButtonsType.OK, "Error al autenticar :(")
            dialog.format_secondary_text(e.__str__())
            dialog.run()
            dialog.destroy()
            sys.exit()
        except IOError as e:
            print e.__str__()
            dialog = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.INFO,
                Gtk.ButtonsType.OK, "Error al autenticar :(")
            dialog.format_secondary_text(e.__str__())
            dialog.run()
            dialog.destroy()
            sys.exit()

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Glades/autenticar.glade")))
        self.builder.connect_signals(self)
        self.window = self.builder.get_object('autenti_window')
        self.window.set_size_request(800,600)
        self.webview = WebKit.WebView()
        self.scrolledwindow1 = self.builder.get_object('scrolledwindow1')
        self.scrolledwindow1.add(self.webview)
        self.URL = ""
        self.getURL()
        self.webview.open(self.URL)
        self.window.show_all()
