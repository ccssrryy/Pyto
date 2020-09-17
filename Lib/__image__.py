import base64
from UIKit import UIImage
from io import BytesIO

try:
    from rubicon.objc import ObjCClass
except ValueError:
    def ObjCClass(name):
        return None

NSData = ObjCClass("NSData")

def __ui_image_from_pil_image__(image):

    if image is None:
        return None

    with BytesIO() as buffered:
        image.save(buffered, format='PNG')
        img_str = base64.b64encode(buffered.getvalue())

    data = NSData.alloc().initWithBase64EncodedString(img_str, options=0)
    image = UIImage.alloc().initWithData(data)
    data.release()
    return image
