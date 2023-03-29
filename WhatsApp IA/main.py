from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import MDTabsBase
from kivymd.theming import ThemeManager
from kivymd.uix.menu import MDDropdownMenu
from kivy.core.window import Window
from kivy.uix.videoplayer import VideoPlayer
from kivy.properties import DictProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder

class Tab(FloatLayout, MDTabsBase):
	pass

class Videos(VideoPlayer):
	pass

class MainApp(MDApp):
	
	data = DictProperty()


	def build(self):
		Window.size = (480,720)
		self.theme_cls.primary_palette = 'Teal'
		self.theme_cls.primary_hue = '800'
		self.data = {
    	'Como enviar un mensaje en WhatsApp': 	[
            'IA10.jpg', "on_press", lambda x: self.change_screen(
            	'Video_reproductor1'),
            ],
    	'Como entrar en un chat en WhatsApp': [
            'IA13.jpg', "on_press", lambda x: self.change_screen(
            	'Video_reproductor2'),
		],
    	
    	'Como enviar una foto en WhatsApp': [
		'IA8.jpg', "on_press", lambda x: self.change_screen('Video_reproductor4'),
		],
    	'Como grabar un audio en WhatsApp': [
		'IA12.jpg', "on_press", lambda x: self.change_screen('Video_reproductor5'),
		],
    	'Como grabar un video en WhatsApp': [
		'IA7.jpg', "on_press", lambda x: self.change_screen('Video_reproductor6'),
		],
		}

		return Builder.load_file('main.kv')



	#Creando la instancia del reproductor de video
		player = VideoPlayer(source = 'prueba.mp4')

		#Assign video player state
		player.state = 'play'

		#set options
		player.options = {'eos': 'loop'}
		
		

	def demo(self):
	        print(self.screen.ids.toolbar.right_action_items[1])

	
	def change_screen(self, screen_name, curr = None, title = None):
		self.root.ids.screen_manager.current = screen_name
		if curr is not None:
			self.root.ids.screen_manager.transition.direction = 'right'
		else:
			self.root.ids.screen_manager.transition.direction = 'left'
		if title is not None:
			self.set_title(title)

	def set_title(self, title):
		self.root.ids.toolbar_chat_screen.title = title

if __name__ == '__main__':
	MainApp().run()