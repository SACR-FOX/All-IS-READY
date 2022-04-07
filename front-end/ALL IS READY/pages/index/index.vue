<template>
	<view>
		<u-search placeholder="日照香炉生紫烟" v-model="keyword"></u-search>
		<button @click="click()" >aaaaaaaa</button>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				title: 'Hello',
				keyword: '遥看瀑布挂前川'
				}
		},
		onLoad() {
			
		},
		methods: {
			click(){
				uni.navigateTo({
					url:"../todo_list/todo_list"
				})
			}
			
		}
	}
</script>

<style lang="scss">

</style>
