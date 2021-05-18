from datetime import timedelta
from typing import Union

from .config import ALLOWEDVIDEOEXTWEEKEND, ALLOWEDVIDEOEXTWORKDAY, DELTATIMEFORIMAGE, JPGEXTENSION
from .models import AllowData, ServerData


class Client():
    def __init__(self, request: dict) -> None:
       self.request = ServerData(**request)

    def process_sound(self) -> str:
        first_unique_char = [
            char for char in self.request.content 
            if self.request.content.count(char) == 1
        ]
        if first_unique_char:
            return first_unique_char[0]

    def process_image(self) -> str:
        is_jpeg = self.is_jpeg(self.request.content)
        if is_jpeg:
            return is_jpeg
        else:
            return self.request.ts - timedelta(hours=DELTATIMEFORIMAGE)
   
    def process_video(self) -> str:
        if self.request.ts.isoweekday() > 5:
           return self.is_video_allow(self.request.content, ALLOWEDVIDEOEXTWEEKEND)
        return self.is_video_allow(self.request.content, ALLOWEDVIDEOEXTWORKDAY)
    
    def process_text(self) -> str:
        return 'text'
    
    @staticmethod
    def is_jpeg(filename: str) -> Union[bool, str]:
        file_ext = filename.rsplit('.', maxsplit=1)
        if (
            (file_ext[-1].lower() in JPGEXTENSION) 
            and (file_ext[0] != '') 
            and (len(file_ext) > 1)
        ):
            return file_ext[0]
        else:
            return False

    @staticmethod
    def is_video_allow(filename: str, lenght: int) -> AllowData:
        file_ext = filename.rsplit('.', maxsplit=1)
        if (
            (len(file_ext[-1]) == lenght)
            and (file_ext[0] != '') 
            and (len(file_ext) > 1)
        ):
            return AllowData.ok.value
        return AllowData.reject.value


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
