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
			
			uni.getImageInfo({
				src : "https://s2.loli.net/2022/04/24/uGFO6zTxnAY39pE.png",
				success: (res) => {
					console.log(res.path)
					console.log("success")
				}
			})
		}
	}
</script>

<style>

</style>

 
 
