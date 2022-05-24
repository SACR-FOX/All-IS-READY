<template>
	<view>
		<view class="card_top" style="display: flex; ">
			<view style="display: flex;flex-direction: row;margin-top: 50rpx;">
				<u-avatar src="../../static/avatar.jpg" :src="user.Header" style="margin-left: 50rpx; margin-top: 15rpx;" size="50"></u-avatar>
				<view style="">
					<view style="text-align: right; margin-left: 170px;display: flex;">
						<text style="margin-top: 30rpx;">今天学习了:</text>
						<text style="font-size: 60rpx; 
									margin-left: 15rpx;margin-right: 15rpx;
									font-weight: bold;">{{timeChange(user.Accumulation)}}</text>
						<text style="margin-top: 30rpx;">{{timeList[timeFlag]}}</text>
					</view>
					<view style="text-align: right;">TOP:{{Situation.percent}}%</view>
				</view>
			</view>
		</view>
		
		<view class="content">
			<view class="col">
				<view class="card" @click="toTodolist()">
					<view style="display: flex; flex-direction: column; margin-left: 55rpx;margin-top: 50rpx;">
						<text style="font-size: 30rpx; font-weight: bold; color: #E43D33;margin-left: 10rpx;">{{week[0]}}</text>
						<text style="font-size: 75rpx; font-weight: bold; margin-top: 10rpx;">10</text>
						<text style="font-size: 50rpx; font-weight: bold; margin-top: 30rpx;margin-left: 10rpx;">{{textFix(todoList,6)}}</text>
					</view>
				</view>
				
				<view class="card" @click="toClassSche()"> 
					<view  style="display: flex; flex-direction: column; margin-left: 55rpx;margin-top: 50rpx;">
						<text style="font-weight: bold;">下一节</text>
						<text style="font-size: 60rpx; font-weight: bold; margin-top: 10rpx;">{{textFix(classSch.curName,3)}}</text>
						<text style="font-weight: bold; margin-top: 20rpx;">{{classSch.room}}</text>
						<text style="font-weight: bold;">{{classSch.Time}}</text>
					</view>
				</view>
				
			</view>
		</view>
		
		<view class="content">
			<view class="col">
				
				<view class="card" style="align-items: center;justify-content: center;" @click="toTimer()">
					<view>
						<circle-progress-bar :pro="pro" :size="230" 
						:border_width="20" :animate="true"
						>
							<text style="font-size: 46rpx;">
								{{pro * 100}}%
							</text>
						</circle-progress-bar>
					</view>
				</view>
				
				<view class="card" @click="toLeaderB()">
					<view style="display: flex; flex-direction: column; margin-left: 55rpx;margin-top: 50rpx;">
						<text style="font-weight: bold; font-size: 30rpx;">班级动态</text>
						<text style="font-weight: bold; font-size: 60rpx; margin-top: 60rpx;">{{textFix(classAct,4)}}</text>
					</view>
				</view>
				
			</view>
		</view>
		
		<view class="card_bottom" @click="toFile()">
			<scroll-view scroll-x="true" style="flex-direction: row; white-space: nowrap;">
				<view v-for="(item,index) in fileList" class="card_doc">
					<view style="display: flex; flex-direction: column;">
						<image src="../../static/pdf_icon.png"
						style="width: 150rpx; height: 150rpx; margin: 10rpx;"
						mode="scaleToFill"></image>
						<text style="font-weight: bolder;margin-left: 15rpx;">{{textFix(item.name,6)}}</text>
						<text style="font-weight: bolder;margin-left: 15rpx;">{{item.size}}M</text>
					</view>
				</view>
			</scroll-view>
		</view>
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
						//token
						token  : "eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJVSUQiOjIsIlVuYW1lIjoieHljZiIsIk9yZ0lEIjoxLCJleHAiOjE2NTMwOTczNDF9.UBTeUJOApg6Kd9rzKTDQKghsV8S0WA0aMGwYqt6Xk9E",
						UID : "2",
						Url : "http://101.37.175.115/api/",
						
						
						//用户信息
						user : {},
					
						//排名信息
						Situation : {},
						
						pro:0.6 ,//计时器
						
						//分钟为0，小时为1
						timeFlag : 0,
						timeList : ["分钟","小时"],
						
						//todoList
						week : ["星期一","星期二","星期三","星期四","星期五","星期六","星期日",],
						week_id : -1,
						days : -1,
						todoList : "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
						
						//学习时间
						learnTime : 6,
						
						//classSchedule
						classSch : {
							"curName" :"移动软件开发",
							"Time" : "9:40",
							"room" : "信息实验室4",
							"Tag" : "rgba(255, 190, 118,1.0)"
						},
						//班级动态
						classAct: "无事发生",
						
						//file
						fileList : [
							{
								'type' : 0,
								"name" : '编译原理白俄爱看啊阿斯顿阿萨原版书',
								'size' : 1.0
							},
							{
								'type' : 0,
								"name" : '编译原理原版书',
								'size' : 0.8
							},
							{
								'type' : 0,
								"name" : '编译原理原版书',
								'size' : 1.0
							},
							{
								'type' : 0,
								"name" : '编译原理原版书',
								'size' : 1.0
							},
						]
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
			},
			
			//修改过长字体
			textFix(text,length){
				if(text.length <= length){
					return text
				}else{
					return (text.slice(0,length)+'...')
				}
			},
			
			timeChange(time){
				let that = this
				if(time<60){
					that.timeFlag = 0
					return 0
					
				}else if(time < 3600){
					that.timeFlag = 0
					return Math.floor(time/60)
					
				}else{
					that.timeFlag = 1
					return Math.floor(time/3600)
				}
			}
		},
		onLoad() {
			let that = this
			
			uni.getSystemInfo({
				success: (res) => {
					console.log(res.deviceId)
				}
			})
			
			uni.request({
				url: that.Url + "User/Detail/"+"2/"+"?token="+that.token,
				method: "GET",
				success: (res) => {
					that.user = res.data
					console.log(that.user.Header)
				}
			})
			
			uni.request({
				url:that.Url + "Reward/Situation/" + "?token="+that.token,
				success: (res) => {
					that.Situation = res.data
					console.log(that.Situation.percent)
				}
			})
			console.log(Math.floor(this.timeChange(3666)))
			console.log(this.textFix("aaaaaa",3))
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
		margin-top: 8px;
	}
	.card {
		width: 350rpx;
		height:350rpx;
		margin: 5px;
		background-color: rgba(241, 238, 236, 0.8);
		border-radius: 15px;
		display: flex;
		flex-direction: column;

	}
	.card_top{
		
		background-color: rgba(241, 238, 236, 0.8);
		border-radius: 30rpx;
		height: 200rpx;
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
