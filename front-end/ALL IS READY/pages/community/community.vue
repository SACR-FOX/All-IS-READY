<template>
	<view>
		<view class="card" @click="jump">
			<text class=" title">标题标题标题标题标题标题标题</text>
			<view class="row">
				<view v-if="HasImage">
					<image src="../../static/logo.png" class="img"></image>
				</view>
				<text class="content">
					内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容
				</text>
			</view>
			<view class="bor"></view>
			<view class="row">
				<text class="creator">张三</text>
				<text class="time">5天前</text>
			</view>
		</view>
	</view>
</template>

<script>
	
	export default {
		data() {
			return {
				HasImage : true,
			}
		},
		methods: {
			jump(){
				uni.navigateTo({
					url:'../topic/topic'
				})
			}
		}
	}
</script>

<style lang="scss">
	.row{
		display: flex;
		flex-direction: row;
	}
	.card{
		padding: 10rpx;
		.title{
			font-weight: bold;
			font-size: 30rpx;
			margin-bottom: 10rpx;
		}
		.img{
			width: 90rpx;
			height: 90rpx;
		}
		.content{
			font-size: 30rpx;
			margin-left: 10rpx;
		}
		.bor{
			border: 1rpx solid #c7ecee;
		}
		.creator{
			font-size: 25rpx;
			width: 100rpx;
		}
		.time{
			font-size: 25rpx;
			
		}
	}
</style>
