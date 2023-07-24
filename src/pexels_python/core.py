class Pexels:
    def __init__(self, api_key:str) -> None:
        self.__api_key = api_key
        self.__headers = {
            'Authorization': self.__api_key
        }
    
    # method for search photos
    # method for recieve curated photos
    # method for get photo with specific ID

    # method for search videos
    # method for recieve current popular videos
    # method for get video with specific ID

    # method for view my collections
    # method for view all media in a collection