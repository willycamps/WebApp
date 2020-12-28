<template>
  <tr>
    
    <td>{{ club.id }}</td>
    <td>{{ club.club }}</td>
    <td>{{ club.club_country }} </td>
    <td>{{ club.club_points }}</td>
    <td> <input type="checkbox" :value="club" id="club.id" v-model="Itemchecked" @change="check($event)">
    </td> 
    
  </tr>
  
</template>

<script>
export default {
  name: 'FootballItem',
  props: ["club"],
  
   data() {   
    return {
      Itemchecked:[]
    }
  }, 
  
  methods: {
    
    check: function() {

      //0if(this.Itemchecked != "")
        //this.addItem();
      //else
        //this.removeItem(this.Itemchecked.id)
  
      //console.log(this.Items);
    },
    addItem() {
      let newObject = {
        id: this.club.id,
        club: this.club.club
      }
      this.Items.push(newObject); // Gives error.
    },
    removeItem(Id) {
         this.Items.remove(this.Items, (item) => { return item.id != Id });  
       },
    //build the Json selected
    markComplete() {
     
    },

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
