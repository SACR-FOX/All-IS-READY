<template>
	<view>
		<u-navbar
		    title="社区"
		    @rightClick="rightClick"
		    :autoBack="true">
		</u-navbar>
		
		<view class="head">
			<!-- <view class="bg-colore"></view> -->
			<view class="row">
				<image :src="ImageUri" class="community_image"></image>
				<view class="col">
					<text class="communityName">{{CommunityName}}</text>
					<view class="row">
						<text class="postCount">{{PostCount+'帖子'}}</text>
						<text class="shu">|</text>
						<text class="renewal">{{Renewal}}</text>
					</view>
				</view>
				
			</view>
			<view class="description">{{Description}}</view>
		</view>
		
		<view style="margin-top: 30rpx;"></view>
		
		<view class="topic">
			<view class="card" @click="jump">
				<text class=" title">官方：波多尔斯基与波兰超球队扎布热矿工续约一个赛季</text>
				<view class="row">
					<view v-if="HasImage">
						<image src="../../static/logo.png" class="img"></image>
					</view>
					<text class="content">
						波兰超扎布热矿工官方宣布，俱乐部与36岁的波多尔斯基续约至2022-23赛季结束。
					</text>
				</view>
				<view class="bor"></view>
				<view class="row">
					<text class="creator">张三</text>
					<text class="time">5天前</text>
				</view>
			</view>
			
			<view class="card" @click="jump">
				<text class=" title">曼晚：亨德森加盟纽卡99%完成，在讨论是转会还是租借一年</text>
				<view class="row">
					<view v-if="HasImage">
						<image src="../../static/logo.png" class="img"></image>
					</view>
					<text class="content">
						虎扑05月19日讯 根据曼彻斯特晚报曼联方面主编Samuel Luckhurst的最新报道，消息人士称，25岁的曼联门将迪恩-亨德森周三在纽卡斯尔进行谈判，交易“99%完成”。
					</text>
				</view>
				<view class="bor"></view>
				<view class="row">
					<text class="creator">张三</text>
					<text class="time">5天前</text>
				</view>
			</view>
			
			<view class="card" @click="jump">
				<text class=" title">六台：巴黎愿意把球队交给姆巴佩，想换教练换队友都行</text>
				<view class="row">
					<view v-if="HasImage">
						<image src="../../static/logo.png" class="img"></image>
					</view>
					<text class="content">
						虎扑05月19日讯 根据西班牙六台记者Edu Aguirre透露称，在最近几个月，巴黎圣日尔曼方面为了能够留住姆巴佩，向姆巴佩提出极为宽厚的条件。
					</text>
				</view>
				<view class="bor"></view>
				<view class="row">
					<text class="creator">张三</text>
					<text class="time">5天前</text>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	
	export default {
		data() {
			return {
				HasImage : true,
				ImageUri:'../../static/logo.png',
				CommunityName:'操作系统',
				PostCount:'158',
				Renewal:'2天前',
				Description:'操作系统（operating system，简称OS）是管理计算机硬件与软件资源的计算机程序。'
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
	.col{
		display: flex;
		flex-direction: column;
	}
	.head{
		padding: 10rpx;
		margin-top: 90rpx;
		
		background-color: #badc58;
		.community_image{
			width: 120rpx;
			height: 120rpx;
			border-radius: 30rpx;
			margin-left: 25rpx;
		}
		.communityName{
			margin-left: 50rpx;
			font-size: 35rpx;
		}
		.postCount{
			margin-left: 50rpx;
			margin-top: 35rpx;
			font-size: 25rpx;
		}
		.shu{
			margin-left: 20rpx;
			margin-right: 20rpx;
			margin-top: 35rpx;
			font-size: 25rpx;
		}
		.renewal{
			margin-top: 35rpx;
			font-size: 25rpx;
		}
		.description{
			margin-top: 20rpx;
			margin-left: 25rpx;
			font-size: 25rpx;
		}
	}
	.topic{
		background-color: #F1F1F1;
		border-radius: 25rpx;
	}
	.card{
		padding: 10rpx;
		margin-top: 10rpx;
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

