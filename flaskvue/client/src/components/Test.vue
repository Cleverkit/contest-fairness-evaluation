<template>
  <div>
    <p>{{ msg }}</p>
    <input v-model="url" type="text" id="info" name="info">
    <h1 v-on:click="getMessage()">Click Here</h1>
  </div>
</template>

<script>

export default {
  name: 'Test',
  data() {
    return {
      msg: '',
      url: '',
    };
  },
  methods: {
    async getMessage() {
      const response = await fetch(this.url);
      const json = await response.json();
      this.msg = json;
    },
  },
};
</script>
