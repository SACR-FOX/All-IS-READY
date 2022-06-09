<template>
	<view>

		
		<view class="head">
			<!-- <view class="bg-colore"></view> -->
			<view class="row">
				<image :src="ImageUri" class="community_image"></image>
				<view class="col">
					<text class="communityName">{{CommunityName}}</text>
					<view class="row">
						<text class="postCount">{{count+'帖子'}}</text>
						<text class="shu">|</text>
						<text class="renewal">{{Renewal}}</text>
					</view>
				</view>
			</view>
			<view class="description">{{Description}}</view>
		</view>
		
		<view style="margin-top: 30rpx;"></view>
		
		<view v-for="i in count" style="margin-top: 20rpx;">
			<view style="display: flex;justify-content: center;">
				<view class="topic">
					<view class="card" @click="jump(results[i-1].TopicID,results[i-1].Title,results[i-1].header,results[i-1].Creator,timeToStr(results[i-1].Time))">
						<view class="row">
							<view v-if="results[i-1].HasImage">
								<image :src='results[i-1].ImageUri' class="img"></image>
							</view>
							<text class=" title">{{results[i-1].Title}}</text>
						</view>
						<view class="bor"></view>
						<view class="row">
							<text class="creator">{{results[i-1].Creator}}</text>
							<text class="time">{{timeToStr(results[i-1].Time)}}</text>
						</view>
					</view>
				</view>
			</view>
			
		</view>
	
		<uni-fab ref="fab" :content="content" @trigger="trigger" />

	</view>
</template>

<script>
	
	export default {
		data() {
			return {
				Url:'http://101.37.175.115/api/',
				results:{},
				Community:{},
				CommunityID:'1',
				page:'1',
				HasImage : true,
				ImageUri:'../../static/logo.png',
				CommunityName:{},
				// PostCount:'158',
				count:'',
				Renewal:'2天前',
				Description:'操作系统（operating system，简称OS）是管理计算机硬件与软件资源的计算机程序。',
				UID:'',
				Creator:'',
				
				content: [
					{
						iconPath: '../../static/huati.png',
						selectedIconPath: '../../static/huati.png',
						text: '创建话题',
						active: false
					},
				]
			}
		},
		methods: {
			trigger(e) {	//点击悬浮按钮
				this.content[e.index].active = !e.item.active
				this.setCommunityID()
				uni.navigateTo({
								url:'./createTopic'
							})
			},
			setStorage(TopicID,Title,header,Creator,Time){	//跳转到话题内部，存储本地数据
				// console.log(name)
				uni.setStorage({
					key : 'TopicID',
					data : {
						TopicID : TopicID,
						Title : Title,
						header:header,
						Creator:Creator,
						Time : Time
					}
				})
			},
			setCommunityID(){	//跳转创建话题，存储社区ID
				console.log(this.CommunityID)
				uni.setStorage({
					key:'create',
					data:{
						CommunityID : this.CommunityID
					}
				})
			},
			jump(TopicID,Title,header,Creator,Time){
				this.setStorage(TopicID,Title,header,Creator,Time)
				console.log(Title)
				uni.navigateTo({
					url:'../topic/topic'
				})
			},
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
			getCommnunityID(){	//获取当前社区ID，用于get请求
				return new Promise((req,rej)=>{
					uni.getStorage({
						key: 'communityID',
						success: function (res) {
							req(res.data)
						},
					})
				})
			},
			getCommunityTopic(){	//获取当前页面数据
				let that = this
				return new Promise((req,rej)=>{
					uni.request({
						url: that.Url + 'Community/Topic_All' + '?token=' + that.useMsg.token + '&CommunityID=' + that.CommunityID +'&page=' +that.page,
						method:'GET',
						
						success: (res) => {
							req(res.data)
							console.log(that.Url + 'Community/Topic_All' + '?token=' + that.useMsg.token + '&CommunityID=' + that.CommunityID +'&page=' +that.page)
							this.results = res.data.data
							this.count = res.data.count
						},
						fail: (err) => {
							req(err)
						}
					})
				})
			},
			timeToStr(time){
				var now=new Date()
				var sec=now.getTime()/1000
				if(time <= 10){
					return "刚刚"
				}
				time = sec - time
				let that = this;
				 // console.log(time)
				if(time >= 3600){
					var hour = Math.floor((time/3600))
					// console.log(hour)
					var min = Math.floor(((time - hour * 3600))/60)
					// console.log(min)
				}else{
					var hour = 0 
					var min = Math.floor(((time - hour * 3600))/60)
				}
				
				if(hour.toString().length < 2)
				{
					hour = "0"+hour
				}
				if(min.toString().length < 2)
				{
					min = "0"+min
				}
				// console.log(hour)
				if(hour==0){
					return min+ "分钟前"
				}else if(hour>=24){
					var day = 0
					day = Math.floor(hour/24)
					return day + "天前"
				}else{
					return hour + "小时前"
				}
			},
		},
		async onLoad() {
			this.useMsg = await this.getToken()
			this.Community = await this.getCommnunityID() //获取传参
			this.CommunityName=this.Community.CommunityName
			this.CommunityID = this.Community.CommunityID
			this.Description = this.Community.Description
			this.Renewal = this.Community.Renewal
			console.log(this.Renewal)
			this.ImageUri = this.Community.Poster
			
			
			this.data = await this.getCommunityTopic() //获取get数据

		},
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
			border-radius: 100rpx;
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
		
		width: 95%;
	}
	.card{
		padding: 10rpx;
		margin-top: 15rpx;
		.title{
			font-weight: bold;
			font-size: 30rpx;
			margin-bottom: 10rpx;
			margin-left: 20rpx;
		}
		.img{
			width: 90rpx;
			height: 90rpx;
			margin-left: 10rpx;
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
			margin-left: 10rpx;
		}
		.time{
			font-size: 25rpx;
			margin-left: 400rpx;
		}
	}
</style>

