export default({
	state: {
		 todos: JSON.parse(window.localStorage.getItem(STORAGE_KEY) || '[]')
	},
	actions,
	mutations,
	plugins
})