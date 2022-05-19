<template>
	
	<view>
		<u-navbar
		    title="帖子"
		    @rightClick="rightClick"
		    :autoBack="true">
		</u-navbar>
		
		<view class="page">
			<text class="title">官方：波多尔斯基与波兰超球队扎布热矿工续约一个赛季</text>
			<view class="row" style="margin-top: 20rpx; margin-bottom: 20rpx;">
				<u-avatar :src="src" size="30" style="width: 80rpx; margin-top:;"></u-avatar>
				<text class="creator">张三</text>
				<view class="time">发布于5天前</view>
			</view>
			<text class="content">
				斯基拉的报道宣称，国米的CEO马洛塔接下来将会再次和迪巴拉的经纪人安图恩会面，目前蓝黑军团为这位阿根廷国脚准备了一份为期3年并附带1年续约选择权，年薪约700万欧元的报价。
				
				这名意大利记者的报道进一步表示，虽然近期媒体上出现了穆里尼奥要求罗马引进迪巴拉的传闻，但双方之间并未进行接触。
			</text>
			
			<view v-if="HasImage">
				<image :src="topicSrc" class="topicSrc"></image>
			</view>
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
		margin-top: 70rpx;
	}
	.row{
		display: flex;
		flex-direction: row;
	}
	.title{
		
		font-size: 40rpx;
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
	.content{
		font-size: 30rpx;
	}
</style>
