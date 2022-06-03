<template>
	
	<view>
		<u-navbar
		    title="话题帖子"
		    @rightClick="rightClick"
		    :autoBack="true">
		</u-navbar>
		
		<view class="page">
			<text class="title">{{Title}}</text>
			<view class="row" style="margin-top: 20rpx; margin-bottom: 20rpx;">
				<u-avatar :src="src" size="30" style="width: 80rpx; margin-top:;"></u-avatar>
				<text class="creator">张三</text>
				<view class="time">发布于5天前</view>
			</view>
			<text class="content">
				<!-- {{result[0].Content}} -->
			</text>
			
			<!-- <view v-if="HasImage">
				<image :src="topicSrc" class="topicSrc"></image>
			</view> -->
			
			<view>
				
			</view>
			
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				Url:'http://101.37.175.115/api/',
				page:'1',
				TopicID:'10',
				data:{},
				src:'../../static/logo.png',
				topicSrc:'../../static/logo.png',
				HasImage:true,
				Content:'',
				result:{},
				Title:''
				
			}
		},
		methods:{
			getToken(){
				return new Promise((req,rej)=>{
					uni.getStorage({
						key: 'userMsg',
						success: function (res) {
							req(res.data)
						},
					})
				})
			},
			getTopicID(){
				return new Promise((req,rej)=>{
					uni.getStorage({
						key: 'TopicID',
						success: function (res) {
							req(res.data)
						},
					})
				})
			},
			getTopic(){
				let that = this
				console.log(that.TopicID)
				return new Promise((req,rej)=>{
					uni.request({
						url: that.Url + 'Community/Post_All' + '?token=' + that.useMsg.token + '&page=' + that.page +'&TopicID=' + this.TopicID,
						method:'GET',
						
						success: (res) => {
							req(res.data)
							console.log(that.Url + 'Community/Post_All' + '?token=' + that.useMsg.token + '&page=' + that.page +'&TopicID=' + this.TopicID)
							this.result = res.data.result
							// console.log(this.TopicID)
							
							// console.log(res.data.result[0].Content)
						},
						fail: (err) => {
							req(err)
						}
					})
				})
			}
		},
		
		async onLoad() {
			this.useMsg = await this.getToken()
			
			this.TopicData = await this.getTopicID()
			this.TopicID = this.TopicData.TopicID
			this.Title = this.TopicData.Title
			
			this.data = await this.getTopic()
			
			
			
			console.log(this.TopicID)
			console.log(this.Title)
		},
		
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
