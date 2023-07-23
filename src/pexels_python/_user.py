from abc import ABC, abstractmethod

class __PexelsUser(ABC):
    """Abstract class for pexels contributor"""
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def user_id(self):
        pass

    @abstractmethod
    def profile_url(self):
        pass

class Photographer(__PexelsUser):
    """
        Create a new photographer user
    """
    def __init__(self,photo_resource_data:dict) -> None:
        super().__init__()
        self.__photo_resource_data = photo_resource_data
    
    @property
    def name(self)->str:
        """
            Returns the name of the photographer
        """
        try:
            return self.__photo_resource_data['photographer']
        except KeyError:
            raise Exception("KeyError: The 'photographer' field not available.")
    
    @property
    def user_id(self)->int:
        """
            Returns the id of the photographer
        """
        try:
            return self.__photo_resource_data['photographer_id']
        except KeyError:
            raise Exception("KeyError: The 'photographer_id' field not available.")
    
    @property
    def profile_url(self)->str:
        """
            Returns the Pexels profile URL of the photographer
        """
        try:
            return self.__photo_resource_data['photographer_url']
        except KeyError:
            raise Exception("KeyError: The 'photographer_url' field not available.")

class Videographer(__PexelsUser):
    """
        Create a new videographer user
    """
    def __init__(self,video_resource_data:dict) -> None:
        super().__init__()
        self.__video_resource_data = video_resource_data
    
    @property
    def name(self)->str:
        """
            Returns the name of the videographer
        """
        try:
            return self.__video_resource_data['user']['name']
        except KeyError:
            raise Exception("KeyError: The ['user']['name'] field not available.")
    
    @property
    def user_id(self)->int:
        """
            Returns the id of the videographer
        """
        try:
            return self.__video_resource_data['user']['id']
        except KeyError:
            raise Exception("KeyError: The ['user']['id'] field not available.")
    
    @property
    def profile_url(self)->str:
        """
            Returns the Pexels profile URL of the videographer
        """
        try:
            return self.__video_resource_data['user']['url']
        except KeyError:
            raise Exception("KeyError: The ['user']['url'] field not available.")