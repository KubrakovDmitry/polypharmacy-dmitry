"""Модуль конвертера на основе dedoc."""

from tempfile import NamedTemporaryFile

import cv2
import numpy as np
from PIL import Image
from pdf2image import convert_from_path
from dedoc import DedocManager

from ocr_converter import OCRConverter


class DedocConverter(OCRConverter):
    """Конвертер на основе Dedoc."""

    def __init__(self):
        self.dedoc_manager = DedocManager()

    def remove_red_blue_stamps(self, image):
        """Метод удаления красного и синего цвета."""
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # диапазоны для красного
        lower_red1 = np.array([0, 70, 50])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([170, 70, 50])
        upper_red2 = np.array([180, 255, 255])

        # диапазон для синего
        lower_blue = np.array([100, 50, 50])
        upper_blue = np.array([140, 255, 255])

        # маски
        mask_red = cv2.inRange(hsv, lower_red1, upper_red1) | cv2.inRange(
            hsv,
            lower_red2,
            upper_red2)
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        mask = mask_red | mask_blue

        # закрашиваем цветные области белым
        image[mask > 0] = 255
        return image

    def preprocess_pdf(self, path):
        """Метод обработки pdf."""
        images = convert_from_path(path)
        processed_images = []

        for img in images:
            img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            cleaned = self.remove_red_blue_stamps(img_cv)
            processed_images.append(Image.fromarray(
                cv2.cvtColor(cleaned, cv2.COLOR_BGR2RGB)))

        temp_file = NamedTemporaryFile(delete=False, suffix=".pdf")
        processed_images[0].save(temp_file.name,
                                 save_all=True,
                                 append_images=processed_images[1:])
        return temp_file.name

    def convert(self, path):
        """Метод преобразования содержания файла."""
        try:
            return self.dedoc_manager.parse(self.preprocess_pdf(path)
                                            ).to_api_schema().model_dump()
        except FileNotFoundError:
            raise Exception(("Проблема открытия файла!"
                             "Убедитеcь в его наличии."))
        except ValueError as error:
            raise Exception((f"Ошибка фортама файла! {error}"
                             "Убедитеcь, что файл правильного формата."))
        except PermissionError:
            raise Exception(("Ошибка доступа!"
                             "Убедитеcь, что есть разрешение"
                             "на доступ к файлу."))
        except Exception as error:
            raise Exception(f"Не предвиденная ошибка! {error}")
