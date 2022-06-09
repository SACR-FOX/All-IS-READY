<template>
	<view style="background-color: #F1F1F1">
		<u-navbar
		    title="学习排行榜"
		    @rightClick="rightClick"
		    :autoBack="true"
		>
		</u-navbar>
		
		<view class="col" style=" margin-top: 150rpx;">
			
			<view class="top" style="margin-left: 60rpx;">
				<u-avatar :src="data.data[1].header"
					size="90" 
					shape="circle"></u-avatar>
				<cover-view class="rank">
					<text class="top_rank_text">2</text>
				</cover-view>
			</view>
				
			<view class="top" style="margin-top: -10rpx;">
				<u-avatar :src="data.data[0].header"
					size="100" 
					shape="circle" 
					></u-avatar>
				<cover-view class="rank">
					<text class="top_rank_text">1</text>
				</cover-view>
			</view>
				
			<view class="top" style="margin-top: 50rpx;">
				<u-avatar :src="data.data[2].header"
					size="80" 
					shape="circle"></u-avatar>
				<cover-view class="rank">
					<text class="top_rank_text">3</text>
				</cover-view>
			</view>
			
		</view>
		
		<view class="rank2">
			<view class="rank_item" v-for="(item,index) in data.data.slice(0,6)" >
				<text class="rank_text">{{index+4}}</text>
				<u-avatar :src="data.data[index+3].header"
					size="40" 
					shape="circle"
					style="margin-top: 20rpx;
					margin-left: 20rpx;"></u-avatar>
				<text class="name_text">{{data.data[index+3].Uname}}</text>
				<text class="exp_text">{{data.data[index+3].Accumulation}}</text>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				list2:[{
					"rank":"4",
					"Header":"../../static/avatar.jpg",
					"Uname":"David",
					"EXP":"100"
				},
				{
					"rank":"5",
					"Header":"../../static/avatar.jpg",
					"Uname":"Lili",
					"EXP":"90"
				},
				{
					"rank":"6",
					"Header":"../../static/avatar.jpg",
					"Uname":"Suan",
					"EXP":"85"
				},
				{
					"rank":"7",
					"Header":"../../static/avatar.jpg",
					"Uname":"Johnson",
					"EXP":"70"
				},
				{
					"rank":"8",
					"Header":"../../static/avatar.jpg",
					"Uname":"Ella",
					"EXP":"63"
				},
				{
					"rank":"9",
					"Header":"../../static/avatar.jpg",
					"Uname":"Steven",
					"EXP":"59"
				},
				{
					"rank":"10",
					"Header":"../../static/avatar.jpg",
					"Uname":"Bob",
					"EXP":"36"
				}],
				
				data:'',
			}
		},
		methods: {
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
			getleaderBoard(){
				let that = this
				return new Promise((req,rej)=>{
					uni.request({
						url:'http://101.37.175.115/api/Reward/Rank?token='+that.useMsg.token,
						methods:'GET',
						
						success: (res) => {
							req(res.data)
							console.log('http://101.37.175.115/api/Reward/Rank?token='+that.useMsg.token)
						},
						fail: (err) => {
							req(err)
						}
					})
				})
			}
		},
		
		async onLoad(){
			this.useMsg = await this.getToken()	//获取用户数据
			
			this.data = await this.getleaderBoard()
			// console.log(this.data.data[0].Uname)
		}
	}
</script>

<style>
	.col{
		display: flex;
		flex-direction: row;
	}
	.top{
		display: flex;
		flex-direction: column;
		margin: 35rpx;
	}
	.rank{
		background-color: #3C9CFF;
		height: 30px;
		width: 30px;
		margin-left: 50rpx;
		border-radius: 90%;
		border: 3px solid #F1F1F1;
	}
	.rank2{
		display: flex;
		flex-direction: column;
		background-color: #ffffff;
		height: 1000rpx;
		margin-left: 20rpx;
		margin-right: 20rpx;
		border-radius: 15rpx;
	}
	.rank_item{
		height: 100rpx;
		display: flex;
		flex-direction: row;
		white-space: nowrap;
		background-color: #d7ff99;
		margin-top: 20rpx;
		margin-left: 10rpx;
		margin-right: 10rpx;
		border-radius: 15rpx;
	}
	.rank_text{
		width: 40rpx;
		margin-left: 30rpx;
		margin-top: 30rpx;
		font-size: 40rpx;
		font-weight: bold;
		align-items: center;
		text-shadow: 0 0 5px #000000,0 0 5px #000000;
		color: #ffffff;
	}
	.name_text{
		width: 300rpx;
		margin-left: 150rpx;
		margin-top: 30rpx;
		font-size: 40rpx;
		font-weight: bold;
		align-items: center;
		text-shadow: 0 0 5px #000000,0 0 5px #000000;
		color: #ffffff;
	}
	.exp_text{
		text-align: right;
		margin-top: 30rpx;
		font-size: 40rpx;
		font-weight: bold;
		align-items: center;
		text-shadow: 0 0 5px #000000,0 0 5px #000000;
		color: #ffffff;
	}
	.top_rank_text{
		margin-left: 17rpx;
		font-size: 40rpx;
		color: #ffffff;
	}
</style>
