<template>
  <div class="ui main container">

    <modal v-if="showModal"> 
      <h3 slot="header" class="modal-title" style="text-align: center;">
        Mark the winner
      </h3>
      
      <div slot="body">
        <table class="ui celled table">
        <thead>
          <tr>
            <th style="text-align: center;">Club</th>
            <th>Winner</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="(item,index) in winner" :key="`item-${index}`"> 
            <td style="text-align: center;">{{ item.club}}</td>  
            <td>
                <label>
                  <input type="checkbox" v-model="winner" :disabled="winner.length > 1 && winner.indexOf(item) === -1" 
                  number> <!-- Item {{ index }} -- {{ winner.indexOf(item) }} --> 
                </label>
            </td>
          </tr>
        </tbody>
      </table>
    
      </div>

      <div slot="footer">
      <button type="button" class="btn btn-outline-info" @click="closeModal()"> Close </button>
      <button type="button" class="btn btn-primary" data-dismiss="modal" @click="submitAndClose()">
        Submit
      </button>
      </div>
    </modal>


      <div class="customer-list">
      <table class="ui celled table">
        <thead>
          <tr>
            <th style="width: 50px; text-align: center;">#</th>
            <th style="text-align: center;">Name of the Club</th>
            <th>Choose</th>
          </tr>
        </thead>

        <tbody>

          <tr v-for="(item,index) in clubs.clubs" :key="`item-${index}`">
            <th scope="row"> {{ item.id}}</th>  
            <td style="text-align: center;">{{ item.club}}</td>  
            <td><label>
                <input type="checkbox" v-model="selected" :value="item" @change="check()"> 
            </label></td>
          </tr>
        </tbody>
      </table>
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
  
  computed :{     
       
  },
  methods: {
    
    check: function() {

      //only when the second item is checked
      if(this.selected.length == 2)
      {
        this.addNew(this.selected);
        this.openModal();  
      }
    },
    addNew: function (item) {

      let result=[];
      item.forEach(function (arrayItem) {
                     const item={   
                        id: arrayItem.id,
                        club: arrayItem.club,
                        point:1}
                     result.push(item);
          });
          //
          this.winner.push(result[0]);
          this.winner.push(result[1]);
    },
    openModal() { 
        this.showModal = true; 
    } ,
    closeModal() {
        this.showModal = false;
        this.winner=[];
      },
    submitAndClose() {
      var obj= { }
      this.winner.forEach(function (array,i){
        i=i+1;
        obj["id"+i]=array.id;
        obj["point"+i]=array.point;
      });

      this.addClubsPoints(obj);
    },
    getClubs(){
      axios.get('http://localhost:8000/clubs')
    .then(res => this.clubs = res.data)
    .catch(err => console.log(err));
    },
    addClubsPoints(obj){
       axios.post('http://localhost:8000/clubs',obj)
      .then(() => {
          //Message of Sucessfull
          //this.showModal = false;
          //this.getClubs();
          //console.log("Sucessful");
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          //this.getBooks();
        });
    },

  },
  created(){
    this.getClubs();
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
</style>
