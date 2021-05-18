from .models import ServerData




class Client():
    def __init__(self, request: dict) -> None:
        self.request = ServerData(**request)


    def process_sound(self) -> str:
        return 'sound'
    
    def process_image(self) -> str:
        return 'image'
    
    def process_video(self) -> str:
        return 'video'
    
    def process_text(self) -> str:
        return 'text'



    def process_data(self) -> str:
        if self.request.type == self.request.type.sound:
            return self.process_sound()
        elif self.request.type == self.request.type.text:
            return self.process_text()
        elif self.request.type == self.request.type.image:
            return self.process_image()
        elif self.request.type == self.request.type.video:
            return self.process_video()
        else:
            raise TypeError('Unsupported data type')
