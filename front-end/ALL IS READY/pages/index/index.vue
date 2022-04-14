<template>
	<view>
		<view class="card_top" style="display: flex; margin-top: 40rpx;">
			<u-avatar src="../../static/avatar.jpg" style="margin-left: 50rpx; margin-top: 30rpx;"></u-avatar>
			<view style="">
				<view style="text-align: right; margin-left: 170px;display: flex;">
					<view style="margin-top: 30rpx;">今天学习了:</view>
					<view style="font-size: 60rpx;">6</view>
					<view style="margin-top: 30rpx;">小时</view>
				</view>
				<view style="text-align: right;">TOP:10%</view>
			</view>
		</view>
		
		<view class="content">
			<view class="col">
				<view class="card" @click="toTodolist()">
					<view style="color: #E456z56;">星期四</view>
					<view style="font-size: 50px;">10</view>
					<view style="">今天有一项待做</view>
				</view>
				
				<view class="card" @click="toClassSche()"> 
					<view>下一节</view>
					<view style="font-size: 40rpx; font-weight: bold; margin-top: 30rpx;">操作系统</view>
					<view style="font-weight: bold; margin-top: 30rpx;">C308 13:40</view>
				</view>
				
			</view>
		</view>
		
		<view class="content">
			<view class="col">
				
				<view class="card" @click="toTimer()">
					<view style="margin-top: 30rpx;">
						<circle-progress-bar :pro="pro" :size="230" :border_width="20" :animate="true">
							<view style="font-size: 46upx;">
								{{pro * 100}}%
							</view>
						</circle-progress-bar>
					</view>
				</view>
				
				<view class="card" @click="toLeaderB()">
					<view style="margin-top: 30rpx;">班级动态</view>
					<view style="margin-top: 60rpx; font-size: 50rpx; font-weight: bold;">无事发生</view>
				</view>
				
			</view>
		</view>
		
		<view class="card_bottom" @click="toFile()">
			<scroll-view scroll-x="true" style="flex-direction: row; white-space: nowrap;">
				<view class="card_doc">
					<image src="../../static/pdf_icon.png" 
					style="width: 170rpx; height: 170rpx;"
					mode="scaleToFill"></image>
					<view style="font-weight: bolder;">编译原理原书</view>
					<view style="font-weight: bolder;">1.0M</view>
				</view>
				<view class="card_doc">
					<image src="../../static/pdf_icon.png" 
					style="width: 170rpx; height: 170rpx;"
					mode="scaleToFill"></image>
					<view style="font-weight: bolder;">编译原理原书</view>
					<view style="font-weight: bolder;">1.0M</view>
				</view>
				<view class="card_doc">
					<image src="../../static/pdf_icon.png" 
					style="width: 170rpx; height: 170rpx;"
					mode="scaleToFill"></image>
					<view style="font-weight: bolder;">编译原理原书</view>
					<view style="font-weight: bolder;">1.0M</view>
				</view>
				<view class="card_doc">
					<image src="../../static/pdf_icon.png" 
					style="width: 170rpx; height: 170rpx;"
					mode="scaleToFill"></image>
					<view style="font-weight: bolder;">编译原理原书</view>
					<view style="font-weight: bolder;">1.0M</view>
				</view>
				<view class="card_doc">
					<image src="../../static/pdf_icon.png" 
					style="width: 170rpx; height: 170rpx;"
					mode="scaleToFill"></image>
					<view style="font-weight: bolder;">编译原理原书</view>
					<view style="font-weight: bolder;">1.0M</view>
				</view>
			</scroll-view>
		</view>
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
					pro:0.6
				}
		},
		methods: {
			toTodolist(){
				uni.navigateTo({
					url:"../todo_list/todo_list"
				})
			},
			toClassSche(){
				uni.navigateTo({
					url:"../classSchedule/classSchedule"
				})
			},
			toTimer(){
				uni.navigateTo({
					url:"../timer/timer"
				})
			},
			toLeaderB(){
				uni.navigateTo({
					url:"../leaderBoard/leaderBoard"
				})
			},
			toFile(){
				uni.navigateTo({
					url:"../file/file"
				})
			}
		},
		onLoad() {
			uni.getSystemInfo({
				success: (res) => {
					console.log(res.deviceId)
				}
			})
		}
	}
</script>

<style lang="scss">
	.content{
		width: 100%;
		height: auto;
		display: flex;
		align-items: center;
		flex-direction: row;
		flex-wrap: wrap;
		justify-content: center;
		margin: 0;
		padding: 0 20rpx;
		box-sizing: border-box;
		
	}
	.col{
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
		margin-top: 30px;
	}
	.card {
		width: 300rpx;
		height: 300rpx;
		margin: 15px;
		background-color: rgba(241, 238, 236, 0.8);
		border-radius: 15px;
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.card_top{
		background-color: rgba(241, 238, 236, 0.8);
		border-radius: 30rpx;
	}
	.card_bottom{
		width: 700rpx;
		height: 300rpx;
		margin: 10px;
		background-color: rgba(241, 238, 236, 0.8);
		border-radius: 15px;
	}
	.card_doc{
		width: 260rpx;
		height: 260rpx;
		margin-top: 25rpx;
		margin-left: 25rpx;
		display: inline-block;
		background-color: rgba(255, 255, 255, 0.8);
		border-radius: 30rpx;
	}
	
	
	// .circleprogress{
	// 	width: 100%;
	// 	height: 200px;
	// 	display: flex;
	// 	justify-content: center;
		
	// }
	// .circleprogress .progresstext{
	// 	position: absolute;
	// 	font-size: 40px;
	// 	width: 200px;
	// 	height: 200px; 
	// 	display: flex;
	// 	justify-content: center;
	// 	align-items: center;
	// 	z-index: 10;
	// 	color: #008000;
	// }
	// .circleprogress .wrapper{
	// 	width: 100px;
	// 	height: 200px;
	// 	overflow: hidden;
	// }
	// .circleprogress .leftprogress,.rightprogress{
	// 	width: 160px;
	// 	height: 160px;
	// 	border:20px solid green;
	// 	border-bottom:20px solid #7ef22e;
	// 	border-radius: 50%;
		
	// }
	// .circleprogress .leftprogress{
	// 	border-right:20px solid #7ef22e;
	// }
	// .circleprogress .rightprogress{
	// 	border-left:20px solid #7ef22e;
	// 	margin-left: -100px;
	// }
</style>
