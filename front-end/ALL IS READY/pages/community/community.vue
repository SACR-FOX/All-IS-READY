<template>
	<view>
		<view class="communityItem" @click="jump">
			<view class="row">
				<view v-if="HasImage">
					<image :src='Poster' class="image"></image>
				</view>
				<view class="col">
					<view class="row">
						<text class="communityName">{{CommunityName}}</text>
						<text class="postCount">{{PostCount}}</text>
					</view>
					<view class="row">
						<text class="description">{{textFix(Description,30)}}</text>
						<text class="renewal">{{Renewal}}</text>
					</view>
				</view>
			</view>
		</view>
		
		<view class="communityItem">
			<view class="row">
				<view v-if="HasImage">
					<image :src='Poster' class="image"></image>
				</view>
				<view class="col">
					<view class="row">
						<text class="communityName">{{CommunityName}}</text>
						<text class="postCount">{{PostCount}}</text>
					</view>
					<view class="row">
						<text class="description">{{textFix(Description,30)}}</text>
						<text class="renewal">{{Renewal}}</text>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				HasImage:true,
				Poster:'../../static/logo.png',
				CommunityName:'操作系统',
				Description:'操作系统（operating system，简称OS）是管理计算机硬件与软件资源的计算机程序。',
				PostCount:'158',
				Renewal:'2天前',
				Renewal:'2天前',
			}
		},
		methods: {
			textFix(text,length){
				if(text.length <= length){
					return text
				}else{
					return (text.slice(0,length)+'...')
				}
			},
			jump(){
				uni.navigateTo({
					url:'../communityTopic/communityTopic'
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
	 .communityItem{
		 padding: 10rpx;
		 
		 .image{
			 height: 90rpx;
			 width: 90rpx;
			 border-radius: 180rpx;
		 }
		 .communityName{
			 padding: 5rpx;
		 }
		 .description{
			 width: 560rpx;
			 padding: 5rpx;
			 font-size: 18rpx;
			 color: #95afc0;
		 }
		 .renewal{
			 padding: 5rpx;
			 font-size: 18rpx;
			 color: #95afc0;
		 }
		 .postCount{
			 margin-top: 7rpx;
			 font-size: 12rpx;
			 color: #686de0;
		 }
	 }
</style>