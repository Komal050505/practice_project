"""
Developing Whatsapp code

"""

from whatsapp_method_overloading_overriding.app import WhatsAppFeatures


class WhatsApp(WhatsAppFeatures):
    """WhatsApp class is implemented here"""

    def get_person_details(self):
        return {"name": self.name, "mobile": self.mobile, "country": self.country}

    def chat(self, sender: int, receiver: int, message: str):
        return f"message has been sent to the receiver - {receiver}"

    def audio(self, sender: int, receiver: int, audio: bytes):
        return f"Audio has been sent to the receiver - {receiver}"

    def video(self, sender: int, receiver: int, video: bytes):
        return f"Video has been sent to the receiver - {receiver}"


#person details check
person1_whatsapp = WhatsApp(mobile=65651, name="komal", country="India")  # obj creation for WhatsApp class
print(f"person1_whatsapp details are - {person1_whatsapp.get_person_details()}")  # accessing method from WhatsApp class

#get person name
person_details = person1_whatsapp.get_person_details()  # obj.method of WhatsApp class
person_name = person_details["name"]  # accessing name from dictionary after creating obj
print(f"person_name is {person_name}")

#get person mobile
person_details = person1_whatsapp.get_person_details()
person_mobile = person_details["mobile"]
print(f"person_mobile is {person_mobile}")

#get person country
person_details = person1_whatsapp.get_person_details()
person_country = person_details["country"]
print(f"person_country is {person_country}")

# chat
chatting = person1_whatsapp.chat(sender=65651, receiver=65652, message="Hello")
print(f"Chatting {chatting} ")

# audio
audio_sent = person1_whatsapp.audio(sender=53, receiver=564574, audio=b'jdhsd.c,252')
print(f" {audio_sent}")

# video
video_sent = person1_whatsapp.video(sender=25, receiver=2554, video=b'jwdhclwkdwjclk25454511|//')
print(f"{video_sent}")
