import random
import string


class Codec:
    def __init__(self) -> None:
        self.url_map = {}
        self.base_url = "http://tinyurl.com/"

    def generate_short_key(self) -> str:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    
    def encode(self, longUrl:str) -> str:
        short_key = self.generate_short_key()

        while short_key in self.url_map:
            short_key = self.generate_short_key()

        short_url = self.base_url + short_key
        self.url_map[short_url] = longUrl

        return short_url
    
    def decode(self, shortUrl: str) -> str:
        return self.url_map.get(shortUrl, "")
    
# codec = Codec()
# codec.decode(codec.encode(url))