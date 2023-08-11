import uuid
import numpy as np
from PIL import Image
import cv2

from .logo_detection import logodetection

model = logodetection()

def redact_logo(file):
    image = Image.open(file)
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    result = redact_logo_from_image(image_cv)
    filename = str(uuid.uuid4())
    cv2.imwrite(f'uploads/{filename}.png', result)

    return filename

def redact_logo_from_image(image):
    boxes = model.predict(image)

    for box in boxes:
        result = cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), -1)

    return result