import Vue from 'vue';
import App from './App.vue';
import router from './router'; // 路由设置
import store from './store'; // 状态管理

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app'); 