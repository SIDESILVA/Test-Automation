import os
import requests
import tempfile
from data.image_data import IMAGES


class ImageProvider:

    def __init__(self):
        self.index_file = os.path.join(tempfile.gettempdir(), "image_rotation_index.txt")

    def _get_index(self):
        if os.path.exists(self.index_file):
            with open(self.index_file, "r") as f:
                return int(f.read().strip())
        return 0

    def _save_index(self, index):
        with open(self.index_file, "w") as f:
            f.write(str(index))

    def get_next_image_file(self):

        index = self._get_index()
        url = IMAGES[index % len(IMAGES)]

        next_index = index + 1
        self._save_index(next_index)

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except Exception as e:
            raise Exception(f"Image download failed: {url}") from e

        file_path = os.path.join(
            tempfile.gettempdir(),
            f"product_image_{next_index}.jpg"
        )

        with open(file_path, "wb") as f:
            f.write(response.content)

        return file_path