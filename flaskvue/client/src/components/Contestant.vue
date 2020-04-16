<template>
  <div>
    <h5>{{ contname }}</h5>
    <img :src=photolink>
    <p>{{ bglink }}</p>
  </div>
</template>

<script lang="ts">
export default {
  name: 'Contestant',
  data() {
    return {
      contname: '',
      photolink: '',
      bglink: '',
    };
  },
  methods: {
    async getData() {
      const response = await fetch('http://localhost:5000/api?command=find_contestants&contestid=1');
      const namedict = await response.json();
      console.log(namedict);
      this.contname = (namedict.data[0].name);
      this.photolink = (namedict.data[0].graphic);
      this.bglink = (namedict.data[0].backgroundinfo);
    },
  },
  mounted() {
    this.getData();
  },
};

</script>
