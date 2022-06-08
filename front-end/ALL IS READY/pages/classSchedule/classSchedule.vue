<template>
	<view>
		<view>
		    <u-navbar
		        title="课程表"
		        @rightClick="rightClick"
		        :autoBack="true"
		    >
				<view
				    class="u-nav-slot"
				    slot="right">
				    <u-icon
				        name="../../static/add_icon.png"
				        size="24"
				        ></u-icon>
				</view>
		    </u-navbar>
		</view>
		
		<u-tabs :list="list1"
			style="margin-top: 70rpx;"
			@click="change":current="0"
			>
		</u-tabs>
	
		<view v-if="currentIndex==7">
			<view v-if="this.class.content!=undefined" >
				<view v-for="(item,index) in this.content" class="course" :style="{backgroundColor:'rgba(246, 229, 141,1.0)'}">
					<view >
						<text class="time">{{item.Start}}</text>
						<text class="curName">{{item.CurName}}</text>
						<text class="room">{{item.Location}}</text>		
					</view>
				</view>
			</view>
		</view>
		
		<view v-if="currentIndex==1">
			<view v-if="this.content!=undefined" >
				<view v-for="(item,index) in this.content" class="course" :style="{backgroundColor:'rgba(246, 229, 141,1.0)'}">
					<view >
						<text class="time">{{item.Start}}</text>
						<text class="curName">{{item.CurName}}</text>
						<text class="room">{{item.Location}}</text>		
					</view>
				</view>
			</view>
		</view>
		
		<view v-if="currentIndex==2">
			<view v-if="this.content!=undefined" >
				<view v-for="(item,index) in this.content" class="course" :style="{backgroundColor:'rgba(246, 229, 141,1.0)'}">
					<view >
						<text class="time">{{item.Start}}</text>
						<text class="curName">{{item.CurName}}</text>
						<text class="room">{{item.Location}}</text>		
					</view>
				</view>
			</view>
		</view>
		
		<view v-if="currentIndex==3">
			<view v-if="this.content!=undefined" >
				<view v-for="(item,index) in this.content" class="course" :style="{backgroundColor:'rgba(246, 229, 141,1.0)'}">
					<view >
						<text class="time">{{item.Start}}</text>
						<text class="curName">{{item.CurName}}</text>
						<text class="room">{{item.Location}}</text>		
					</view>
				</view>
			</view>
		</view>
		
		<view v-if="currentIndex==4">
			<view v-if="this.content!=undefined" >
				<view v-for="(item,index) in this.content" class="course" :style="{backgroundColor:'rgba(246, 229, 141,1.0)'}">
					<view >
						<text class="time">{{item.Start}}</text>
						<text class="curName">{{item.CurName}}</text>
						<text class="room">{{item.Location}}</text>		
					</view>
				</view>
			</view>
		</view>
		
		<view v-if="currentIndex==5">
			<view v-if="this.content!=undefined" >
				<view v-for="(item,index) in this.content" class="course" :style="{backgroundColor:'rgba(246, 229, 141,1.0)'}">
					<view >
						<text class="time">{{item.Start}}</text>
						<text class="curName">{{item.CurName}}</text>
						<text class="room">{{item.Location}}</text>		
					</view>
				</view>
			</view>
		</view>
		
		<view v-if="currentIndex==6">
			<view v-if="this.content!=undefined" >
				<view v-for="(item,index) in this.content" class="course" :style="{backgroundColor:'rgba(246, 229, 141,1.0)'}">
					<view >
						<text class="time">{{item.Start}}</text>
						<text class="curName">{{item.CurName}}</text>
						<text class="room">{{item.Location}}</text>		
					</view>
				</view>
			</view>
		</view>
		
		<button @click="addCourse">11</button>
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				list1: [{
                    name: '星期天',
					currentIndex:7,
                }, {
                    name: '星期一',
					currentIndex:1,
                }, {
                    name: '星期二',
					currentIndex:2,
                }, {
                    name: '星期三',
					currentIndex:3,
                }, {
                    name: '星期四',
					currentIndex:4,
                }, {
                    name: '星期五',
					currentIndex:5,
                }, {
                    name: '星期六',
					currentIndex:6,
                }],
				
					// list2: [{
					// 	"curName" :"编译原理",
					// 	"Time" : "8:05",
					// 	"room" : "E413",
					// 	"Tag" : "rgba(246, 229, 141,1.0)"
					// },
					// {
					// 	"curName" :"移动软件开发",
					// 	"Time" : "9:40",
					// 	"room" : "信息实验室4",
					// 	"Tag" : "rgba(255, 190, 118,1.0)"
					// },
					// {
					// 	"curName" :"操作系统",
					// 	"Time" : "13:40",
					// 	"room" : "E317",
					// 	"Tag" : "rgba(186, 220, 88,1.0)"
					// },
					// {
					// 	"curName" :"操作系统实验",
					// 	"Time" : "18:30",
					// 	"room" : "信息实验室5",
					// 	"Tag" : "rgba(255, 121, 121,1.0)"
					// }
					// ],
					
					Tags:["rgba(246, 229, 141,1.0)","rgba(255, 190, 118,1.0)","rgba(186, 220, 88,1.0)","rgba(255, 121, 121,1.0)"],
					
					class:'',
					currentIndex:'7',
					Day:'7',
					Tag:'',
					content:'',
				}
				
				
		},
		methods: {
			async change(item){
				this.currentIndex = item.currentIndex
				this.class = await this.getClass()
				if(this.class.content[0]!=undefined){
					this.content = this.class.content
				}else{
					console.log('今日无课表')
				}
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
			getClass(){
				let that = this
				return new Promise((req,rej)=>{
					uni.request({
						url:'http://101.37.175.115/api/Schedule/byDay/?token=' + that.useMsg.token + '&Day=' + this.currentIndex,
						method:"GET",
						success: (res) => {
							
							req(res.data)
							console.log('http://101.37.175.115/api/Schedule/byDay/?token=' + that.useMsg.token + '&Day=' + this.currentIndex)
							// console.log(res.data.content[0].Tag)
						},
						fail: (err) => {
							rej(err)
							// console.log(1)
						},
					})
				})
			},
			addCourse(){
				let that = this
				return new Promise((req,rej)=>{
					uni.request({
						url:'http://101.37.175.115/api/Schedule/Action/?token=' + that.useMsg.token,
						method:'POST',
						data:{
							Day:'3',
							DurationStart:69500,
							DurationEnd:71000,
							Location:'E302',
							CurName:'数学111',
							Tag:'0',
							UUID:24,
							UID:that.useMsg.UID
						},
						success: (res) => {
							console.log(res.data)
							req(res.data)
							console.log('http://101.37.175.115/api/Schedule/Action/?token=' + that.useMsg.token)
							// console.log(res.data.content[0].Tag)
						},
						fail: (err) => {
							console.log(err)
							rej(err)
						}
					})
				}).catch((e)=>{});
			}
		},
		async onLoad(){ 
			this.useMsg = await this.getToken()
			// console.log(this.useMsg.token)
			
			this.class = await this.getClass()
			if(this.class.content[0]!=undefined){
				this.content = this.class.content
				// console.log(this.content[0].Tag)
				// console.log(this.class.content[0].Tag)
				// console.log(item.currentIndex)
				// console.log(this.content[item.currentIndex-1].Tag)
			}else{
				console.log('今日无课表')
			}
		}
	}
</script>

<style>
	.course{
		height: 100rpx;
		flex-direction: row;
		white-space: nowrap;
		background-color: #55ff7f;
		margin-top: 10rpx;
		align-items: center;
		height: 100rpx;

	}
	.time{
		margin-left: 30rpx;
		font-size: 40rpx;
		font-weight: bold;
		align-items: center;
		text-shadow: 0 0 5px #000000,0 0 5px #000000;
		color: #ffffff;
	}
	.curName{
		margin-left: 50rpx;
		font-size: 40rpx;
		font-weight: bold;
		align-items: center;
		text-shadow: 0 0 5px #000000,0 0 5px #000000;
		color: #ffffff;
	}
	.room{
		margin-left: 50rpx;
		font-size: 40rpx;
		font-weight: bold;
		color: #ffffff;
		text-shadow: 0 0 5px #000000,0 0 5px #000000;
	}
</style>
