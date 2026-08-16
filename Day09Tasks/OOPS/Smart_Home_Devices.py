# Smart Home Devices (Multiple Inheritance)


class WiFiDevice:
    def wifi(self):
        print("WiFi Connected")
class VoiceAssistant:
    def voice(self):
        print("Voice Assistant Activated")

class SmartSpeaker(WiFiDevice,VoiceAssistant):
    def display(self):
        self.wifi()
        self.voice()

s=SmartSpeaker()
s.display()
        
