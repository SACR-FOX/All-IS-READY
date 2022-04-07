<template>
	<view>
		<text>{{list_id}}</text>
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
			
		},
		onLoad(obj){
			this.list_id = obj.id
			console.log(obj.id)
		}
	}
</script>

<style>

</style>
