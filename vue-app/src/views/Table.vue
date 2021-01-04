<template>
  <div class="ui main container">

    <modal v-if="showModal"> 
      <h3 slot="header" class="modal-title">
        Mark the winner
      </h3>
      
      <div slot="body">
      
       <ul class="list-group">
          <li class="list-group-item" v-for="(item,index) in selected" :key="`item-${index}`">
             {{ item}}
             <label>
              <input type="checkbox" v-model="winner" :value="item" :disabled="winner.length > 0 && winner.indexOf(index) === -1" 
                number> Item {{ index }} -- {{ winner.indexOf(index) }} 
              </label>
          </li>
        </ul>
      </div>

      <div slot="footer">
      <button type="button" class="btn btn-outline-info" @click="closeModal()"> Close </button>
      <button type="button" class="btn btn-primary" data-dismiss="modal" @click="submitAndClose()">
        Submit
      </button>
      </div>
    </modal>


      <div class="customer-list">
        
        <ul class="list-group" >
          <li class="list-group-item" v-for="(item,index) in clubs.clubs" :key="`item-${index}`">
             {{ item}}
             <label>
                <input type="checkbox" v-model="selected" :value="item" @change="check()"> 
            </label>
          </li>
          
        </ul>
      </div>
      
    </div>
</template>

<script>


import Modal from '@/components/Modal.vue';
import axios from 'axios'

export default {
  name: 'App',
  components: { 
    Modal
  },
  data(){
    return {
      clubs:[{}],
      selected: [],
      winner:[],
      showModal: false 
    }
  },
  
  
  methods: {
    
    check: function() {

      //only when the second item is checked
      if(this.selected.length == 2)
      {
          this.openModal();
         
      }
    },
    openModal() { 
        this.showModal = true; 
    } ,
    closeModal() {
        this.showModal = false;
        this.winner=[];
      },
    submitAndClose() {
      console.log(this.winner);
    },

  },
  created(){
    axios.get('http://localhost:8000/clubs')
    .then(res => this.clubs = res.data)
    .catch(err => console.log(err));
  } 

}
</script>
<style>
#image {
  line-height: 1.5em;
  list-style-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/4621/treehouse-marker.png);
}
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
</style>
