from dataclasses import dataclass


@dataclass
class Settings:
    end = '\033[0;0m'
    red = '\033[0;31m'

class Message():
    def danger(self, text: str) -> None:
        print(Settings.red + text + Settings.end)

