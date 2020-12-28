<template>
  <div class="customer-list">
    <div class="data">
      <table class="ui celled table">
        <thead>
          <tr>
            <th style="width: 50px; text-align: center;">#</th>
            <th>Club</th>
            <th>Country</th>
            <th>Points</th>
            <th style="width: 50px; text-align: center;">Select</th>
          </tr>
        </thead>

        <tbody>
          <FootballItem v-for="club in club" :key="club.id" :club="club" />
        </tbody>

      </table>
       
    </div>
     

  </div>
</template>

<script>

import FootballItem from './FootballItem.vue';

export default {
  name: "FootballList",
  components: {
      FootballItem
  },
  props:["club"],
  data() {   
    return {
      Itemchecked:[]
    }
  }, 
methods: {
   check: function() {

      if(this.Itemchecked != "")
        alert("Checked")
      else
        alert("Unchecked")

    }

    }

};
</script>

<style scoped>
.add {
    background: #ff0000;
    color: #fff;
    border: none;
    padding: 5px 9px;
    border-radius: 50%;
    cursor: pointer;
    float: right;
  }

</style>