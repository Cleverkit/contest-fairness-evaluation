<template>
  <div>
    <test></test>
    <contestant></contestant>
  </div>
</template>

<script>
// @ is an alias to /src
import Test from '@/components/Test.vue';
import Contestant from '@/components/Contestant.vue';

export default {
  name: 'ContestView',
  components: {
    Test,
    Contestant,
  },
};
</script>
