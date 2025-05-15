<script setup>
import { ref, onMounted } from "vue";

const inventario = ref([]);
const API_URL = "http://127.0.0.1:5000/"

const cargarInventario = async () => {
  const query = `
    query {
      productos {
        id
        nombre
        precio
        stock
        disponible
      }
    }
  `;

  const response = await fetch(API_URL, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({query}),
  });

  const result = await response.json();
  inventario.value = result.data.productos;
};

const venderProducto = async (producto) => {
  if (producto.stock > 0) {
    const mutation = `
      mutation {
        venderProducto(id: ${producto.id}) {
          producto {
            id
            stock
            disponible
          }
        }
      }
    `;
    await fetch(API_URL, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({query: mutation}),
  });
  await cargarInventario();
  }
};

const reponerProducto = async (producto) => {
  const mutation = `
    mutation {
      reponerProducto(id: ${producto.id}) {
        producto {
          id
          stock
          disponible
        }
      }
    }
  `;
  await fetch(API_URL, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({query: mutation}),
  });
  await cargarInventario();
};

onMounted(() => {
  cargarInventario();
});
</script>

<template>
  <div class="min-h-screen bg-gray-100 text-gray-900 flex flex-col">
    <header class="bg-white shadow-md px-6 py-4">
      <h1 class="text-2xl font-semibold">Gestión de inventario</h1>
    </header>

    <main class="flex-grow container mx-auto px-6 py-8">
      <h2 class="text-xl font-semibold mb-4">Lista de productos</h2>

      <div class="overflow-x-auto bg-white shadow-md rounded-lg">
        <table class="w-full text-left border-collapse">
          <thead>
            <tr class="bg-gray-200 text-gray-700 text-sm uppercase tracking-wide">
              <th class="px-4 py-3">Producto</th>
              <th class="px-4 py-3 text-right">Precio</th>
              <th class="px-4 py-3 text-right">Stock</th>
              <th class="px-4 py-3 text-center">Estado</th>
              <th class="px-4 py-3 text-center">Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="producto in inventario"
              :key="producto.nombre"
              class="border-t transition"
              :class="{
                'bg-red-100 text-red-800': producto.stock === 0,  
                'hover:bg-gray-100': producto.stock > 0           
              }"
            >
              <td class="px-4 py-3">{{ producto.nombre }}</td>
              <td class="px-4 py-3 text-right">{{ producto.precio }} €</td>
              <td class="px-4 py-3 text-right">{{ producto.stock }}</td>
              <td class="px-4 py-3 text-center">
                <span
                  class="px-2 py-1 rounded text-xs font-semibold"
                  :class="producto.disponible ? 'bg-green-200 text-green-800' : 'bg-red-300 text-red-900'"
                >
                  {{ producto.disponible ? "Disponible" : "Agotado" }}
                </span>
              </td>
              <td class="px-4 py-3 flex justify-center gap-2">
                <button
                  @click="venderProducto(producto)"
                  class="px-3 py-1 text-white text-xs rounded shadow-md transition"
                  :class="producto.stock > 0 ? 'bg-blue-500 hover:bg-blue-600' : 'bg-gray-400 cursor-not-allowed'"
                  :disabled="producto.stock === 0"
                >
                  Vender
                </button>
                <button
                  @click="reponerProducto(producto)"
                  class="px-3 py-1 bg-green-500 text-white text-xs rounded shadow-md hover:bg-green-600 transition"
                >
                  Reponer
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>
  </div>
</template>
