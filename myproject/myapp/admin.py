from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Menu,MenuItem,Sliders,UrunKategori,UrunVitrin,Urunler,Image,SosyalMedya,References,HizliLinkler,Contact,Hakkimizda


admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Sliders)
admin.site.register(UrunKategori)
admin.site.register(UrunVitrin)
admin.site.register(Urunler)
admin.site.register(Image)
admin.site.register(SosyalMedya)
admin.site.register(References)
admin.site.register(HizliLinkler)
admin.site.register(Contact)
admin.site.register(Hakkimizda)
