# Instrucciones para probar la API

1. **Instalar las dependencias necesarias para ejecutar el proyecto**

    - Recomendable instalarlas en un entorno independiente. En mi caso he utilizado un entorno de Anaconda llamado `backend-inventario`. Para crearlo de la misma manera que yo, sigue los siguientes pasos:

        1. Crear un entorno en Anaconda.

        ```bash
        conda create -n backend-inventario python=3.11
        ```

        2. Activar el entorno.

        ```bash
        conda activate backend-inventario
        ```

        3. Instalar las dependencias. Puedes hacerlo a través del archivo `requirements.txt`.

        ```bash
        pip install -r requirements.txt
        ```

2. **Arrancar el servidor Flask**

    - Ejecutaremos el servidor mediante el siguiente comando:

    ```bash
    python run.py
    ```

    - Una vez el servidor este corriendo podrás abrir el navegador en `http://127.0.0.1:5000/`

3. **Acceder al explorador GraphiQL**

    - Una vez dentro de la interfaz de GraphiQL, podrás probar las consultas y mutaciones realizadas:

        1. **Listar todos los productos**

        ```graphql
        query {
            productos {
                id
                nombre
                precio
                stock
                disponible
            }
        }
        ```

        2. **Vender un producto**

        ```graphql
        mutation {
            venderProducto(id: 1) {
                producto {
                    id
                    nombre
                    precio
                    stock
                    disponible
                }
            }
        }
        ```

        3. **Reponer un producto**

        ```graphql
        mutation {
            reponerProducto(id: 2) {
                producto{
                    id
                    nombre
                    precio
                    stock
                    disponible
                }
            }
        }
        ```

## Prueba de archivo test.py

Con el servidor arrancado, accede a la carpeta `test` y ejecuta el siguiente comando:

```bash
python test.py
```