from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from shop.views import CategoryViewset, ProductViewset, ArticleViewset,\
    AdminCategoryViewset, AdminArticleViewset, AdminProductViewset

schema_view = get_schema_view(
    openapi.Info(
        title="Documentation API",
        default_version='v1',
        description="Ceci est une documentation de l'api pour notre boutique",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.SimpleRouter()
router.register('category', CategoryViewset, basename='category')
router.register('product', ProductViewset, basename='product')
router.register('article', ArticleViewset, basename='article')

router.register('admin/category', AdminCategoryViewset, basename='admin-category')
router.register('admin/product', AdminProductViewset, basename='admin-product')
router.register('admin/article', AdminArticleViewset, basename='admin-article')

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api/', include(router.urls))
]
