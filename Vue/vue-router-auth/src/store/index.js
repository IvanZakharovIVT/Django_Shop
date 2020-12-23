import Vue from 'vue'
import Vuex from 'vuex'
import auth from './auth'
// eslint-disable-next-line
/* eslint-disable */
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  	token: '',
	user: null,
  },
  mutations: {

},
modules: {
	auth
},
  actions: {

}
})