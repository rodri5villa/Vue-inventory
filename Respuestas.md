## 1. ¿Qué ventajas ofrece GraphQL sobre REST en este contexto?

  - Permite obtener solo los campos que realmente necesitamos, sin recibir información innecesaria.

  - Reduce la cantidad de llamadas al servidor, ya que 
    permite consultar todo en una única petición.

  - Mejora la eficiencia en el consumo de datos entre backend y frontend, sobre todo para interfaces dinámicas.

## 2. ¿Cómo se definen los tipos y resolvers en una API con GraphQL?

  - Los tipos se definen creando clases que heredan `graphene.ObjectType`, especificando sus campos y tipos de datos.
    - Ejemplo: el tipo `Producto` tiene campos `id`, `nombre`, `stock` y `disponible`.

  - Los resolvers son métodos que permiten obtener o modificar datos:
    - Para consultas (`Query`), se crean métodos como `resolve_productos`.
    - Para mutaciones (`Mutation`), se crean clases como `VenderProducto` y `ReponerProducto`, donde se define el comportamiento mediante `mutate`.

## 3. ¿Por qué es importante que el backend también actualice disponible y no depender solo del frontend?

  - Para mantener coherencia y fiabilidad de los datos, no puede depender de la lógica del cliente.
  - El backend es el responsable final de la integridad de los datos.
  - De esta manera, aunque cambie el frontend o haya varios clientes, las reglas de negocio se siguen respetando.

## 4. ¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?

  - En las mutaciones (`venderProducto` y `reponerProducto`), cada vez que cambia el stock, se actualiza automáticamente el campo disponible en el backend, de tal forma que:

    - Si el stock baja a 0, disponible se pone false.
    - Si el stock sube desde 0, disponible se pone true.

  - Esta lógica está implementada directamente en el backend, no depende del frontend.