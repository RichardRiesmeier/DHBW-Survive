<template>
<nav class="bg-gray-900 h-24 flex items-center justify-between px-4">
  <div class="flex-shrink-0 px-1">
    <img class="h-48 pt-6" src="src/img/LOGO klein.png" alt="Logo">
  </div>
  <div class="hidden md:flex">
    <a href="#" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Link 1</a>
    <a href="#" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Link 2</a>
  </div>
  <div class="flex-shrink-0">
    <div class="relative">
      <button class="text-white rounded-full py-2 px-4 hover:bg-blue-500 hover:text-white" @click="showDropdown = !showDropdown">Anmelden</button>
      <div v-if="showDropdown" class="absolute right-0 mt-2 w-64 rounded-md shadow-lg bg-white">
        <form class="px-4 py-2">
          <div class="mb-2">
            <label for="email" class="block text-gray-700 font-bold mb-2">Email</label>
            <input type="email" id="email" name="email" class="border border-gray-400 py-2 px-3 rounded-md w-full" required>
          </div>
          <div class="mb-4">
            <label for="name" class="block text-gray-700 font-bold mb-2">Name</label>
            <input type="text" id="name" name="name" class="border border-gray-400 py-2 px-3 rounded-md w-full" required>
          </div>
          <button class="bg-blue-500 text-white rounded-full py-2 px-4">Anmelden</button>
        </form>
      </div>
    </div>
  </div>
</nav>
  </template>
  
  <script>
  export default {
    data() {
      return {
        showDropdown: false,
      }
    },
  }
  </script>
  