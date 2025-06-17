from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import yt_dlp
import threading

class YTDownloader(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.link_input = TextInput(hint_text='Enter YouTube URL', multiline=False, size_hint_y=0.2)
        self.add_widget(self.link_input)

        self.status = Label(text="Paste a link and press download", size_hint_y=0.2)
        self.add_widget(self.status)

        self.download_button = Button(text='Download', size_hint_y=0.2)
        self.download_button.bind(on_press=self.download_video)
        self.add_widget(self.download_button)

    def download_video(self, instance):
        link = self.link_input.text.strip()
        if not link:
            self.status.text = "❌ Please enter a link!"
            return

        self.status.text = "⬇️ Downloading..."
        threading.Thread(target=self._download_thread, args=(link,), daemon=True).start()

    def _download_thread(self, link):
        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': '%(title)s.%(ext)s'
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            self.status.text = "✅ Download completed!"
        except Exception as e:
            self.status.text = f"❌ Error: {str(e)}"

class MyApp(App):
    def build(self):
        return YTDownloader()

if __name__ == '__main__':
    MyApp().run()
