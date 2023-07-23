from pexels_python._user import Photographer

class Actions:
    # Implement this class in future
    pass

class Photo_Files:
    def __init__(self,photo_files_src:dict) -> None:
        self.__photo_files_src = photo_files_src
    
    @property
    def orginal(self)->Actions:
        """"""
        try:
            return Actions(self.__photo_files_src['orginal'])
        except KeyError:
            raise Exception("KeyError: The 'orginal' field not available.")
    
    @property
    def extra_large(self)->Actions:
        try:
            return Actions(self.__photo_files_src['large2x'])
        except KeyError:
            raise Exception("KeyError: The 'large2x' field not available.")

    @property
    def large(self)->Actions:
        try:
            return Actions(self.__photo_files_src['large'])
        except KeyError:
            raise Exception("KeyError: The 'large' field not available.")
    
    @property
    def medium(self)->Actions:
        try:
            return Actions(self.__photo_files_src['medium'])
        except KeyError:
            raise Exception("KeyError: The 'medium' field not available.")

    @property
    def small(self)->Actions:
        try:
            return Actions(self.__photo_files_src['small'])
        except KeyError:
            raise Exception("KeyError: The 'small' field not available.")

    @property
    def portrait(self)->Actions:
        try:
            return Actions(self.__photo_files_src['portrait'])
        except KeyError:
            raise Exception("KeyError: The 'portrait' field not available.")
    
    @property
    def landscape(self)->Actions:
        try:
            return Actions(self.__photo_files_src['landscape'])
        except KeyError:
            raise Exception("KeyError: The 'landscape' field not available.")

    @property
    def tiny(self)->Actions:
        try:
            return Actions(self.__photo_files_src['tiny'])
        except KeyError:
            raise Exception("KeyError: The 'tiny' field not available.")

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