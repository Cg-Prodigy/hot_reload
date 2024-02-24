from kivy.core.window import Window
from kivy.factory import Factory
from kaki.app import App
from kivymd.app import MDApp
Window.size=(360,640)
class HotReload(App,MDApp):
    CLASSES={'EntryPoint':'app_files.templates'}
    KV_FILES=['kivy_files/kivy_lang.kv']
    AUTORELOADER_PATHS=[('app_files',{'recursive':True}),('kivy_files',{'recursive':True})]
    def build_app(self):
        return Factory.EntryPoint()

if __name__=='__main__':
    HotReload().run()
