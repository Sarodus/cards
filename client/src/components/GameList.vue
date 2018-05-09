<template>
  <div>
      <ul>
        <li v-bind:key="game.id" v-for="game in games">
          <router-link :to="{ name: 'game', params: { game: game.name }}">
            {{game.name}}
          </router-link>
        </li>
      </ul>
  </div>
</template>

<script>
export default {
  name: 'GameList',
  data() {
    return {
      games: [
        {id: 1, name: 'Briscola'},
        {id: 2, name: 'Daihinmin'},
      ]
    }
  }
} 
</script>