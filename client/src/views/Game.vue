<script>
import Vue from 'vue'
import Briscola from '@/games/Briscola'
import Daihinmin from '@/games/Daihinmin'

const gameMap = {
    Briscola,
    Daihinmin
}

export default Vue.component('Game', {
  render: function (createElement) {
    return createElement(
        'div',
        [
            createElement(gameMap[this.$route.params.game])
        ]
    )
  }
})
</script>