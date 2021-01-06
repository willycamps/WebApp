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
         
            <tr v-for="rows in winner" :key="rows.value"> 
            <td style="text-align: center;">{{rows.club}}</td>  
            <td>
                <label>
                  <input type="checkbox" v-model="winnerSelect" :value="rows.id" :disabled="winnerSelect.length > 0 && winner.indexOf(rows.value) === -1" number
                  @change="checkWinner(rows.id)"  > 

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
     <FlashMessage></FlashMessage>
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
                <input type="checkbox" v-model="selected" :value="item" @change="checkSelection()"> 
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
      winnerSelect:[],
      showModal: false 
    }
  },
  
  methods: {
    
    checkWinner:function(id){
      this.setWinner(id);
    },
    checkSelection: function() {
      
      //only when the second item is checked
      if(this.selected.length == 2)
      {
        this.addNew();
        this.openModal();  
      }
    },
    addNew: function () {
      var result=[];
      this.selected.forEach(function (arrayItem) {
                      result.push({id: arrayItem.id, club: arrayItem.club, point:1});
                    
          });
        this.winner = result;
    },
    setWinner(id){
      this.winner.forEach(function(array)
          {
            if (id == array.id)
              array.point = 3;
            else
              array.point = 0;
          }
      );
    },
    setEquals(){
      this.winner.forEach(function(array) { array.point = 1;});
    },
    openModal() { 
        this.showModal = true; 
        this.setEquals();
    },
    closeModal() {
        this.showModal = false;
        this.winner=[];
        this.selected=[];
        this.winnerSelect=[];
      },
      //create a Json Objects as API is waiting
    convertObject(){
      var obj={}
      this.winner.forEach(function (array,i){
        i=i+1;
        obj["id"+i]=array.id;
        obj["point"+i]=array.point;
      });
      return obj;
    },

    submitAndClose() {
      
      this.addClubsPoints(this.convertObject());
    },
    getClubs(){
      axios.get('http://localhost:8000/clubs')
    .then(res => this.clubs = res.data)
    .catch(err => console.log(err));
    },
    //add points to Clubs
    addClubsPoints(obj){
       axios.post('http://localhost:8000/clubs',obj)
      .then(() => {
          this.closeModal();
          this.flashMessage.success({title: 'Success',message: 'The points have been added!'});
          this.getClubs();
        })
        .catch((error) => {
          this.flashMessage.error({ title: 'Error',message: error});
          console.log(error);
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
