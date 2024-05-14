from pydantic import BaseModel


class Config(BaseModel):
    wttr_image_output: bool = False
