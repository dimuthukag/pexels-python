import requests
import pexels_python._validation as _validation
from pexels_python._resource import Photo

class Pexels:
    def __init__(self, api_key:str) -> None:
        self.__api_key = api_key
        self.__headers = {
            'Authorization': self.__api_key
        }
    
    def search_photos(self, query:str, orientation:str=None,size:str=None,color:str=None,locale:str=None,page:int=1,per_page:int=15)->list[Photo]:
        """
            Retrive a list of photos from given parameters
        """
        endpoint_url = f'https://api.pexels.com/v1/search'
        if _validation.validate_page(page):
            endpoint_url += f'?page={page}'
        if _validation.validate_per_page(per_page):
            endpoint_url += f'&per_page={per_page}'
        if _validation.validate_query(query):
            endpoint_url += f'&query={query.replace(" ","%20")}'
        if  orientation and _validation.validate_orientation(orientation):
            endpoint_url += f'&orientation={orientation}'
        if size and _validation.validate_photo_size(size):
            endpoint_url += f'$size={size}'
        if color and _validation.validate_color(color):
            endpoint_url += f'$color={color}'
        if locale and _validation.validate_locale(locale):
            endpoint_url += f'$locale={locale}'
        
        response = requests.get(endpoint_url,headers=self.__headers)
        if response.status_code == 200:
            return [Photo(resource_data) for resource_data in response.json()['photos']]
    
    def curated_photos(self,page:int=1,per_page:int=15)->list[Photo]:
        """
            Retrive a list of real time photos curated by the Pexels team
        """
        endpoint_url = 'https://api.pexels.com/v1/curated'
        if _validation.validate_page(page):
            endpoint_url += f'?page={page}'
        if _validation.validate_per_page(page):
            endpoint_url += f'&per_page={per_page}'

        response = requests.get(endpoint_url,headers=self.__headers)
        if response.status_code == 200:
            return [Photo(resource_data) for resource_data in response.json()['photos']]

    def get_photo(self, photo_id:int)->Photo:
        """
            Retrive a specific photo from its id.
        """
        endpoint_url = f'https://api.pexels.com/v1/photos/{photo_id}'
        response = requests.get(endpoint_url,headers=self.__headers)
        if response.status_code == 200:
            return Photo(response.json())

    # method for search videos
    # method for recieve current popular videos
    # method for get video with specific ID

    # method for view my collections
    # method for view all media in a collection