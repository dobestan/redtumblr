from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

import requests


class ImageCrawler(object):

    def run(image_url):
        """Crawl image from image_url, and return a File instance."""

        response = requests.get(image_url)

        image_file_temp = NamedTemporaryFile(delete=True)
        image_file_temp.write(response.content)
        image_file_temp.flush()
        image = File(image_file_temp)
        image.name = "{filename}.{extension}".format(
            filename='temp_image',
            extension=image_url.split('.')[-1],
        )

        return image
