<template>
	<view>
		<text>{{list_id}}</text>
		<button @click="click()">{{list_id}}</button>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				"list_id" : -1,
			}
		},
		methods: {
			click(){
				uni.vibrateLong({
					success: (res) => {
						console.log("success")
					}
				})
			}
		},
		onLoad(obj){
			this.list_id = obj.id
			console.log(obj.id)
		}
	}
</script>

<style>

</style>
