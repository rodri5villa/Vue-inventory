# 1. Vue no detecta cambios dentro de objetos reactivos de la forma que esperarías. ¿Cómo podrías observar un cambio en una propiedad anidada?
Vue utiliza `reactive()` para crear objetos reactivos, pero no detecta cambios en propiedades anidadas de manera directa. Para observar cambios dentro de un objeto anidado, se debe utilizar `watch()` con la opción `{ deep: true }`. Esto permite detectar cualquier modificación en las propiedades internas del objeto.

### Ejemplo:
```vue
watch(
  () => objeto.anidado,
  (nuevoValor) => {
    console.log("Cambio detectado en objeto anidado:", nuevoValor);
  },
  { deep: true }
);
```
En este caso, cualquier cambio dentro de `objeto.anidado` será detectado.

---

# 2. `watch()` permite escuchar cambios en propiedades específicas dentro de `reactive()`, explica cómo funciona.
`watch()` es una función de Vue que permite reaccionar a cambios en variables o propiedades de un objeto reactivo. Funciona observando una propiedad o una función computada, ejecutando una función de callback cuando detecta un cambio.

### Sintaxis básica:
```vue
watch(
  () => objeto.propiedad,
  (nuevoValor, viejoValor) => {
    console.log("La propiedad ha cambiado de", viejoValor, "a", nuevoValor);
  }
);
```

**Parámetros de `watch()`:**
1. **Primer argumento**: Una función que devuelve la propiedad a observar.
2. **Segundo argumento**: Una función callback que recibe el nuevo y el viejo valor.
3. **Opcional: `{ deep: true }`**: Si queremos detectar cambios dentro de objetos anidados.

---

# 3. ¿Cómo harías que un `watch()` detecte cambios en `stock` dentro de un array de productos?
Si `productos` es un array reactivo donde cada producto tiene una propiedad `stock`, podemos usar `watch()` con la opción `{ deep: true }` para detectar cambios en cualquier `stock` dentro del array.

### Ejemplo:
```vue
watch(
  productos,
  (nuevosProductos) => {
    nuevosProductos.forEach((producto) => {
      producto.disponible = producto.stock > 0;
    });
  },
  { deep: true }
);
```

### Explicación:
- `watch()` observa el array `productos`.
- Cada vez que cambia el `stock` de cualquier producto, la función de callback se ejecuta.
- Se actualiza la propiedad `disponible` según el valor de `stock`.
- `{ deep: true }` permite detectar cambios dentro de los objetos dentro del array.

