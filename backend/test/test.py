import requests

URL = "http://127.0.0.1:5000/"

def test_query_productos():
    query= """
    query{
        productos{
            id
            nombre
            precio
            stock
            disponible
        }
    }
    """
    respuesta = requests.post(URL, json={'query': query})
    print("\nListar productos: ")
    print(respuesta.json())

def test_vender_producto(producto_id):
    mutation = f"""
    mutation{{
        venderProducto(id: {producto_id}) {{
        producto{{
            id
            nombre
            precio
            stock
            disponible
        }}
        }}
    }}
    """
    respuesta = requests.post(URL, json={'query': mutation})
    print(f"\nVenta de producto con id {producto_id}")
    print(respuesta.json())

def test_reponer_producto(producto_id):
    mutation = f"""
    mutation{{
        reponerProducto(id: {producto_id}) {{
            producto{{
            id
            nombre
            precio
            stock
            disponible
            }}
        }}
    }}
    """
    respuesta = requests.post(URL, json={'query': mutation})
    print(f"\nReponer producto con id {producto_id}")
    print(respuesta.json())

if __name__== "__main__":
    
    test_query_productos()

    test_vender_producto(1)
    test_query_productos()

    test_reponer_producto(2)
    test_query_productos()