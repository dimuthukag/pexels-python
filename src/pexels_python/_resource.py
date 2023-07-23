from pexels_python._user import Photographer

class Photo_Files:
    # Implement this class in future
    pass

class Photo:
    """
        Create a new photo object
    """
    def __init__(self,resource_data:dict) -> None:
        self.__resource_data = resource_data
    
    @property
    def id(self)->int:
        """
            Returns the id of the photo
        """
        try:
            return self.__resource_data['id']
        except KeyError:
            raise Exception("KeyError: The 'id' field not available.")
    
    @property
    def width(self)->int:
        """
            Returns the width of the photo in pixels
        """
        try:
            return self.__resource_data['width']
        except KeyError:
            raise Exception("KeyError: The 'width' field not available.")

    @property
    def height(self)->int:
        """
            Returns the height of the photo in pixels
        """
        try:
            return self.__resource_data['height']
        except KeyError:
            raise Exception("KeyError: The 'height' field not available.")

    @property
    def url(self)->str:
        """
            Returns the Pexels URL of the photo
        """
        try:
            return self.__resource_data['url']
        except KeyError:
            raise Exception("KeyError: The 'url' field not available.")
    
    @property
    def photographer(self)->Photographer:
        return Photographer(self.__resource_data)

    @property
    def avg_color(self)->str:
        """
            Returns the average color of the photo
        """
        try:
            return self.__resource_data['avg_color']
        except KeyError:
            raise Exception("KeyError: The 'avg_color' field not available.")
    
    @property
    def resource(self)->Photo_Files:
        try:
            return Photo_Files(self.__resource_data['src'])
        except KeyError:
            raise Exception("KeyError: The 'src' field not available.")

    @property
    def text_description(self)->str:
        """
            Returns the text description of the photo
        """
        try:
            return self.__resource_data['alt']
        except KeyError:
            raise Exception("KeyError: The 'avg_color' field not available.")