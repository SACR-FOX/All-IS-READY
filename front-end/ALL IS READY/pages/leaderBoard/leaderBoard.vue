<template>
	<view>
		<u-navbar
		    title="学习排行榜"
		    @rightClick="rightClick"
		    :autoBack="true"
		>
		</u-navbar>
		
		<view class="col" style=" margin-top: 150rpx;">
			
			<view class="top" style="margin-left: 60rpx;">
				<u-avatar src="../../static/avatar.jpg"
					size="90" 
					shape="circle"></u-avatar>
				<cover-view class="rank">
					<text class="top_rank_text">2</text>
				</cover-view>
			</view>
				
			<view class="top" style="margin-top: -10rpx;">
				<u-avatar src="../../static/avatar.jpg"
					size="100" 
					shape="circle" 
					></u-avatar>
				<cover-view class="rank">
					<text class="top_rank_text">1</text>
				</cover-view>
			</view>
				
			<view class="top" style="margin-top: 50rpx;">
				<u-avatar src="../../static/avatar.jpg"
					size="80" 
					shape="circle"></u-avatar>
				<cover-view class="rank">
					<text class="top_rank_text">3</text>
				</cover-view>
			</view>
			
		</view>
		
		<view class="rank2">
			<view class="rank_item" v-for="(item,index) in list2">
				<text class="rank_text">{{item.rank}}</text>
				<u-avatar :src=item.Header
					size="30" 
					shape="circle"
					style="margin-top: 20rpx;
					margin-left: 20rpx;"></u-avatar>
				<text class="name_text">{{item.Uname}}</text>
				<text class="exp_text">{{item.EXP}}</text>
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
				}]
			}
		},
		methods: {

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
	}
	.rank_item{
		height: 100rpx;
		display: flex;
		flex-direction: row;
		white-space: nowrap;
		background-color: #9bff29;
		margin-top: 10rpx;
	}
	.rank_text{
		width: 40rpx;
		margin-left: 30rpx;
		margin-top: 30rpx;
	}
	.name_text{
		width: 300rpx;
		margin-left: 190rpx;
		margin-top: 30rpx;
	}
	.exp_text{
		text-align: right;
		margin-top: 30rpx;
	}
	.top_rank_text{
		margin-left: 17rpx;
		font-size: 40rpx;
		color: #ffffff;
	}
</style>
