from .models import (MySettings)
from online.models import (Category)
def extras(request):
    settings = MySettings.objects.last()
    categoriess = Category.objects.all()
    return {
            'setting':settings,
            'categoriess': categoriess,
        }