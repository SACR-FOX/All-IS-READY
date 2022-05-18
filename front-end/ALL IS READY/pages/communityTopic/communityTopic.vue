<template>
	<view>
		<u-navbar
		    title="社区"
		    @rightClick="rightClick"
		    :autoBack="true">
		</u-navbar>
		
		<view class="head">
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
		margin-left: 40rpx;
		.community_image{
			width: 120rpx;
			height: 120rpx;
		}
		.communityName{
			margin-left: 50rpx;
		}
		.postCount{
			margin-left: 50rpx;
			margin-top: 40rpx;
		}
		.shu{
			margin-left: 20rpx;
			margin-right: 20rpx;
			margin-top: 40rpx;
		}
		.renewal{
			margin-top: 40rpx;
		}
		.description{
			margin-top: 20rpx;
		}
	}
	.card{
		padding: 10rpx;
		margin-top: 50rpx;
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

