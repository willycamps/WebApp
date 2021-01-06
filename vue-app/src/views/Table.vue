<template>
  <div class="ui main container">
      <div class="customer-list">
        <FootballList v-for="club in clubs" :key="club.id" :club="club" />
      </div>
      
    </div>
</template>

<script>

import FootballList from '@/components/FootballList.vue';
import axios from 'axios'

export default {
  name: 'App',
  components: { 
    FootballList
  },
  data(){
    return {
      clubs:[{
      }]
    }

  },
  //get the list of CLubs
  created(){
    axios.get('http://localhost:8000/clubs')
    .then(res => this.clubs = res.data)
    .catch(err => console.log(err));
  } 

}
</script>
<style>

.vue-color {
  background: #41b883 !important;
}
.main.container {
  margin-top: 60px;
}
.submit-button {
  margin-top: 24px !important;
  float: right;
}
.data {
  margin-top: 15px;
}
thead tr th {
  background: #e0e0e0 !important;
}
.ui.inverted.dimmer {
  background-color: rgba(255, 255, 255, 0) !important;
}
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
