<template>
	<view class="page">
		<text class="title">标题标题标题标题标题</text>
		<view class="row">
			<u-avatar :src="src" size="30" style="width: 80rpx; margin-top:;"></u-avatar>
			<text class="creator">张三</text>
			<view class="time">发布于5天前</view>
		</view>
		<text class="content">
			内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容
		</text>
		<view v-if="HasImage">
			<image :src="topicSrc" class="topicSrc"></image>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				src:'../../static/logo.png',
				topicSrc:'../../static/logo.png',
				HasImage:true
				
			};
		}
	}
</script>

<style lang="scss">
	.page{
		padding: 10rpx;
	}
	.row{
		display: flex;
		flex-direction: row;
	}
	.title{
		font-size: 55rpx;
		font-weight: bold;
	}
	.creator{
		display: flex;
		align-items: center;
		width: 450rpx;
	}
	.time{
		display: flex;
		align-items: center;
		color: #95afc0;
	}
	.topicSrc{
		width: 400rpx;
		height: 400rpx;
		display: flex;
		flex-direction: row;
		justify-content: center;
	}
</style>
