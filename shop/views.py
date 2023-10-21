from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.generics import get_object_or_404

from shop.permissions import IsAdminAuthenticated, IsStaffAuthenticated
from shop.models import Category, Product, Article
from shop.serializers import CategoryDetailSerializer, CategoryListSerializer,\
    ProductDetailSerializer, ProductListSerializer, ArticleSerializer


class MultipleSerializerMixin:

    detail_serializer_class = None
    

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


# Classe Admin pour les operations CRUD sur la CategoryViewset 
class AdminCategoryViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminAuthenticated, IsStaffAuthenticated]

    # Méthode pour créer une nouvelle catégorie
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Méthode pour mettre à jour une catégorie
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Méthode pour supprimer une catégorie
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Méthode pour désactiver une catégorie
    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        instance = self.get_object()
        instance.disable()
        return Response()


# La classe pour restreindre l'acces aux utilisateurs que pour la lecture
class CategoryViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):

    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        return Category.objects.filter(active=True)

    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()


# Classe Admin pour les operations CRUD sur la ProductViewset
class AdminProductViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = ProductListSerializer
    detail_serializer_class = ProductDetailSerializer
    queryset = Product.objects.filter(active=True)
    permission_classes = [IsAdminAuthenticated, IsStaffAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.is_staff or request.user.is_superuser:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = get_object_or_404(Product, pk=product_id)

        serializer = self.detail_serializer_class(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        if request.user.is_staff or request.user.is_superuser:
            product = self.get_object()
            serializer = self.serializer_class(product, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff or request.user.is_superuser:
            product = self.get_object()
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        if request.user.is_staff or request.user.is_superuser:
            product = self.get_object()
            product.disable()
            return Response()
        else:
            return Response({"message": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)


# La classe pour restreindre l'acces aux utilisateurs que pour la lecture
class ProductViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):

    serializer_class = ProductListSerializer
    detail_serializer_class = ProductDetailSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()


# Classe Admin pour les operations CRUD sur la classe ArticleViewset
class AdminArticleViewset(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [IsAdminAuthenticated, IsStaffAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.is_staff or request.user.is_superuser:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, *args, **kwargs):
        article_id = kwargs.get('pk')
        article = self.get_object()
        serializer = self.serializer_class(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        if request.user.is_staff or request.user.is_superuser:
            article = self.get_object()
            serializer = self.serializer_class(article, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff or request.user.is_superuser:
            article = self.get_object()
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)


# La classe pour restreindre l'acces aux utilisateurs que pour la lecture
class ArticleViewset(ReadOnlyModelViewSet):

    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.filter(active=True)
        product_id = self.request.GET.get('product_id')
        if product_id is not None:
            queryset = queryset.filter(product_id=product_id)
        return queryset

