import Vue from 'vue';
import VueRouter from 'vue-router';
import ContestView from '../views/ContestView.vue';
import Test from '../components/Test.vue';
import Contestant from '../components/Contestant.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: ContestView,
  },
  {
    path: '/ping',
    name: 'Ping',
    component: Test,
    Contestant,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
