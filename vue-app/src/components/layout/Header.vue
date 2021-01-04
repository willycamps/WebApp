<template>
  <header class="header">
    <h1>Vue JS with Flask API</h1>
    <div id="nav">
      <router-link to="/">Admin</router-link> |
      <router-link to="/table">Table</router-link>
    </div>
  </header>
</template>

<script>
export default {
  name: "Header"
}
</script>

<style scoped>
  .header {
    background: #41b883;
    color: #fff;
    text-align: center;
    padding: 10px;
  }
  .header a {
    color: #fff;
    padding-right: 5px;
    text-decoration: none;
  }
</style>