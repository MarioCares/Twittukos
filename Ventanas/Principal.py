# -*- coding: utf-8 -*-

__author__ = 'Mario Cares <mcares@puertosolutions.cl>'

try:
    from gi.repository import Gtk
    import tweepy
    import os.path
    from Modelos.Usuario import Class_Usuario
    from Controladores.UsuarioDAO import Class_UsuarioDAO
    from Controladores.WinPrincipalDAO import Class_WinPrincipalDAO
except:
    print 'GTK no disponible'

class Class_Principal:

    def putError(self, dic):
        dialog = Gtk.MessageDialog(self.window, 0,
            Gtk.MessageType.ERROR if dic["Tipo"]==0 else Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, dic["Mensaje"])
        dialog.format_secondary_text(dic["Detalle"])
        dialog.run()
        dialog.destroy()
        if(dic["Tipo"] == 0):
            import sys
            sys.exit()

    def mostrar(self):
        Gtk.main()

    def on_principal_window_delete_event(self, *args):
        Gtk.main_quit(*args)

    def on_item_cargar_followers_activate(self, *args):
        import json
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config/Seguidores.json")), 'w') as out:
            json.dump(self.UsuarioDao.getFollowers(), out)
        self.putError({"Tipo":1, "Mensaje":"Listado de Seguidores descargados", "Detalle":""})

    def on_item_historico_seguidores_activate(self):

        pass

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Glades/principal.glade")))
        self.builder.connect_signals(self)
        self.window = self.builder.get_object('principal_window')
        self.window.set_size_request(800,600)

        self.ventanaDAO = Class_WinPrincipalDAO()
        api = self.ventanaDAO.Conectar()
        if api.__class__.__name__ == "API" :
            self.UsuarioDao = Class_UsuarioDAO(self.ventanaDAO.getAPI())
            self.Usuario = Class_Usuario(
                self.UsuarioDao.getNombreUsuario(),
                self.UsuarioDao.getID(),
                self.UsuarioDao.getScreenUserName()
            )
        else:
            self.putError(api)


        self.window.show_all()