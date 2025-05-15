import graphene
from .producto import Producto  
from .inventario import inventario

class Query(graphene.ObjectType):

    productos = graphene.List(Producto)

    def resolve_productos(self, info):
        return [Producto(**producto) for producto in inventario]
    
class VenderProducto(graphene.Mutation):

    class Arguments:
        id = graphene.Int(required=True)

    producto = graphene.Field(Producto)

    def mutate(self, info, id):
        for producto in inventario:
            if producto['id'] == id and producto['stock'] > 0:
                producto['stock'] -= 1
                producto['disponible'] = producto['stock'] > 0
                return VenderProducto(producto = Producto(**producto))
        return VenderProducto(producto=None)

class ReponerProducto(graphene.Mutation):

    class Arguments:
        id = graphene.Int(required=True)

    producto = graphene.Field(Producto)

    def mutate(self, info, id):
        for producto in inventario:
            if producto['id'] == id:
                producto['stock'] += 1
                producto['disponible'] = producto['stock'] > 0
                return ReponerProducto(producto = Producto(**producto))
        return ReponerProducto(producto=None)

class Mutation(graphene.ObjectType):

    vender_producto = VenderProducto.Field()
    reponer_producto = ReponerProducto.Field()

schema = graphene.Schema(query = Query, mutation = Mutation)