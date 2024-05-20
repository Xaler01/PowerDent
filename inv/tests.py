from django.contrib.auth.models import User
from django.test import TestCase
from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from datetime import date

class CategoriaModelTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(descripcion="Categoria de Prueba")

    def test_categoria_creacion(self):
        self.assertEqual(self.categoria.descripcion, "CATEGORIA DE PRUEBA")

    def test_categoria_str(self):
        self.assertEqual(str(self.categoria), "CATEGORIA DE PRUEBA")


class SubCategoriaModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.categoria = Categoria.objects.create(descripcion="Categoria de Prueba",uc_id=self.user.id)
        self.subcategoria = SubCategoria.objects.create(categoria=self.categoria, descripcion="Subcategoria de Prueba")

    def test_subcategoria_creacion(self):
        self.assertEqual(self.subcategoria.descripcion, "SUBCATEGORIA DE PRUEBA")
        self.assertEqual(self.subcategoria.categoria.descripcion, "CATEGORIA DE PRUEBA")

    def test_subcategoria_str(self):
        subcategoria = SubCategoria.objects.create(
            descripcion="Subcategoria de Prueba",
            categoria=self.categoria,
            uc_id=self.user.id
        )
        self.assertEqual(str(subcategoria), "Subcategoria de Prueba")



class MarcaModelTest(TestCase):
    def setUp(self):
        self.marca = Marca.objects.create(descripcion="Marca de Prueba")

    def test_marca_creacion(self):
        self.assertEqual(self.marca.descripcion, "MARCA DE PRUEBA")

    def test_marca_str(self):
        self.assertEqual(str(self.marca), "MARCA DE PRUEBA")

class UnidadMedidaModelTest(TestCase):
    def setUp(self):
        self.unidad_medida = UnidadMedida.objects.create(descripcion="Unidad de Prueba")

    def test_unidad_medida_creacion(self):
        self.assertEqual(self.unidad_medida.descripcion, "UNIDAD DE PRUEBA")

    def test_unidad_medida_str(self):
        self.assertEqual(str(self.unidad_medida), "UNIDAD DE PRUEBA")

class ProductoModelTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(descripcion="Categoria de Prueba")
        self.subcategoria = SubCategoria.objects.create(categoria=self.categoria, descripcion="Subcategoria de Prueba")
        self.marca = Marca.objects.create(descripcion="Marca de Prueba")
        self.unidad_medida = UnidadMedida.objects.create(descripcion="Unidad de Prueba")
        self.producto = Producto.objects.create(
            codigo="PRD001",
            codigo_barra="1234567890123",
            descripcion="Producto de Prueba",
            precio=100.0,
            existencia=50,
            ultima_compra=date.today(),
            cantidad_minima=10,
            marca=self.marca,
            unidad_medida=self.unidad_medida,
            subcategoria=self.subcategoria
        )

    def test_producto_creacion(self):
        self.assertEqual(self.producto.descripcion, "PRODUCTO DE PRUEBA")
        self.assertEqual(self.producto.marca.descripcion, "MARCA DE PRUEBA")
        self.assertEqual(self.producto.unidad_medida.descripcion, "UNIDAD DE PRUEBA")
        self.assertEqual(self.producto.subcategoria.descripcion, "SUBCATEGORIA DE PRUEBA")
        self.assertEqual(self.producto.precio, 100.0)
        self.assertEqual(self.producto.existencia, 50)
        self.assertEqual(self.producto.cantidad_minima, 10)

    def test_producto_str(self):
        self.assertEqual(str(self.producto), "PRODUCTO DE PRUEBA")


