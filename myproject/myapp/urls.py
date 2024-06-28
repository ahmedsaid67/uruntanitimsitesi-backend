from django.urls import path, include
from .views import  MenuViewSet, MenuItemListCreateView, MenuItemByMenuView, \
    MenuItemDetailView, MenuSelectedItemViewSet,SlidersViewSet,UrunKategoriViewSet,UrunKategoriListView, CheckToken,CustomAuthToken,Logout,\
    UserInfoView,UrunVitrinListView,UrunlerViewSet,UrunVitrinViewSet,\
    ImageViewSet,SosyalMedyaViewSet,ReferencesViewSet,HizliLinklerViewSet
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

#menu
router = DefaultRouter()
router.register(r'menus', MenuViewSet)
router_selectedmenuitems = DefaultRouter()
router_selectedmenuitems.register(r'menuitems/menu/selected', MenuSelectedItemViewSet)

#slider
router_sliders = DefaultRouter()
router_sliders.register(r'sliders', SlidersViewSet)

# ürün kategori
router_urunkategori = DefaultRouter()
router_urunkategori.register(r'urunkategori', UrunKategoriViewSet)

# ürün vitrin
router_vitrin = DefaultRouter()
router_vitrin.register(r'urunvitrin', UrunVitrinViewSet)

# ürünler
router_urunler = DefaultRouter()
router_urunler.register(r'urunler', UrunlerViewSet)

# Image
router_image = DefaultRouter()
router_image.register(r'image', ImageViewSet)

#sosyalmedya
router_sosyalmedya = DefaultRouter()
router_sosyalmedya.register(r'sosyalmedya', SosyalMedyaViewSet)

#referanslar
router_references = DefaultRouter()
router_references.register(r'references', ReferencesViewSet)

#hızlılinkler
router_hizlilinkler = DefaultRouter()
router_hizlilinkler.register(r'hizlilinkler', HizliLinklerViewSet)



urlpatterns = [

    # selectedmenuitems
    path('', include(router_selectedmenuitems.urls)),

    # menu apileri
    path('menu/', include(router.urls)),

    # menu apileri
    path('menu/', include(router.urls)),
    path('menuitems/', MenuItemListCreateView.as_view(), name='menuitem-list'),
    # Tüm nesneleri sunma için ve yeni öge üretmek
    path('menuitems/menu/<int:menu_id>/', MenuItemByMenuView.as_view(), name='menuitem-by-menu'),
    #sliders
    path('', include(router_sliders.urls)),

    #### ürün
    #ürün kategori
    path('', include(router_urunkategori.urls)),
    path('urunkategori-list/', UrunKategoriListView.as_view(), name='urunkategori-list'),

    ##vitrim
    path('', include(router_vitrin.urls)),
    path('urunvitrin-list/', UrunVitrinListView.as_view(), name='urunvitrin-list'),

    # ürünler
    path('', include(router_urunler.urls)),

    # image
    path('', include(router_image.urls)),

    #sosyalmedya
    path('', include(router_sosyalmedya.urls)),

    #sosyalmedya
    path('', include(router_references.urls)),

    #hızlılinkler
    path('', include(router_hizlilinkler.urls)),



    # auth apileri
    path('token/', CustomAuthToken.as_view(), name='api-token'),
    path('check-token/', CheckToken.as_view(), name='check-token'),
    path('user-info/', UserInfoView.as_view(), name='user-info'),
    path('logout/', Logout.as_view(), name='logout'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)