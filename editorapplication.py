import wx
from panityframe import PanityFrame

class EditorApplication(object):

    @staticmethod
    def run():
        app = wx.App()
        app.SetAppName("PandaEditor")
        app.SetClassName("PandaEditor")
        frame = PanityFrame(None)
        frame.Show()
        app.MainLoop()