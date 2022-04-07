<template>
	<view>
		<u-sticky bgColor="#feffdd">
			<u-tabs :list="list1"></u-tabs>
		</u-sticky>
	</view>
</template>

<script>
	export default {
		data() {
			return {
					list1: [{
                    name: '星期天',
                }, {
                    name: '星期一',
                }, {
                    name: '星期二'
                }, {
                    name: '星期三'
                }, {
                    name: '星期四'
                }, {
                    name: '星期五'
                }, {
                    name: '星期六'
                }]
				}
		},
		methods: {
	
		}
	}
</script>

<style>
	.card_day{
		background-color: #b5c8b7;
	}
</style>
