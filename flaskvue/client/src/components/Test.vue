<template>
  <div>
    <h1>{{ name }}</h1>
    <h3>{{ description }}</h3>
    <!--<input v-model="url" type="text" id="info" name="info">
    <h1 v-on:click="getMessage()">Click Here</h1>-->
  </div>
</template>

<script>
export default {
  name: 'Test',
  data() {
    return {
      name: '',
      description: '',
      url: '',
    };
  },
  methods: {
    async getName() {
      const response = await fetch('http://localhost:5000/api?command=find_contest&id=1');
      const namedict = await response.json();
      this.name = (namedict.data[0].name);
    },
    async getDescription() {
      const response = await fetch('http://localhost:5000/api?command=find_contest&id=1');
      const namedict = await response.json();
      console.log(namedict);
      this.description = (namedict.data[0].description);
      /*
      const fullist = JSON.parse(namedict);
      console.log(fullist);
      console.log(typeof fullist);
      const listing = (fullist.data);
      console.log(listing);
      const [tmp] = namedict;
      const [thing1, thing2, thing3] = tmp;
      console.log(thing1);
      console.log(thing2);
      console.log(thing3);
      this.name = thing3;
      */
    },
  },
  mounted() {
    this.getName();
    this.getDescription();
  },
};

</script>
