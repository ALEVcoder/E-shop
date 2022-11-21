from django.core.exceptions import ValidationError

def rasm_olchami(image):
    width = image.width
    height = image.height
    if width > 370:
        raise ValidationError("Maximum Uzunlik 370px")
    if height > 300:
        raise ValidationError("Maximum Balandlik 300px")
    
def image_size(image):
    width = image.width
    height = image.height
    if width > 600:
        raise ValidationError("Maximum Uzunlik 600px")
    if height > 370:
        raise ValidationError("Maximum Balandlik 370px")


def logo_size(logo):
    width = logo.width
    height = logo.height
    if width > 100:
        raise ValidationError("Maximum Uzunlik 100px")
    if height > 100:
        raise ValidationError("Maximum Balandlik 100px")