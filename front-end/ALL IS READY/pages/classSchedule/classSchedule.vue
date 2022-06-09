<template>
	<view>
	
		
		<u-tabs :list="list1"
			style="margin-top: 10rpx;"
			@click="change"
			:current="today"
			>
		</u-tabs>
	
		<view v-if="currentIndex==7">
			<view v-if="this.class.content!=undefined" >
				<view v-for="(item,index) in this.content" class="course" :style="{backgroundColor: Tags[content[index].Tag] }">
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
				<view v-for="(item,index) in this.content" class="course" :style="{backgroundColor: Tags[content[index].Tag] }">
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
				<view v-for="(item,index) in this.content" class="course" :style="{backgroundColor: Tags[content[index].Tag] }">
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
				<view v-for="(item,index) in this.content" class="course" :style="{backgroundColor: Tags[content[index].Tag] }">
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
				<view v-for="(item,index) in this.content" class="course" :style="{backgroundColor: Tags[content[index].Tag] }">
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
				<view v-for="(item,index) in this.content" class="course" :style="{backgroundColor: Tags[content[index].Tag] }">
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
				<view v-for="(item,index) in this.content" class="course" :style="{backgroundColor: Tags[content[index].Tag] }">
					<view >
						<text class="time">{{item.Start}}</text>
						<text class="curName">{{item.CurName}}</text>
						<text class="room">{{item.Location}}</text>		
					</view>
				</view>
			</view>
		</view>
		
		<uni-fab ref="fab" :content="content1" @trigger="trigger"/>
		
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


				today:0,
					
				Tags:["rgba(246, 229, 141,1.0)","rgba(255, 190, 118,1.0)","rgba(186, 220, 88,1.0)","rgba(255, 121, 121,1.0)","rgba(255, 121, 121,1.0)","rgba(106, 176, 76,1.0)"],
					
				class:'',
				currentIndex:'7',
				Day:'7',
				Tag:'',
				content:'',
				
				content1: [{
						iconPath: '../../static/add1.png',
						selectedIconPath: '../../static/add1.png',
						text: '导入课程',
						active: false
					},
					{
						iconPath: '../../static/add2.png',
						selectedIconPath: '../../static/add2.png',
						text: '创建课程',
						active: false
					},
				]
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
			trigger(e) {	//悬浮按钮点击事件
				// console.log(e)
				let that = this
				this.content[e.index].active = !e.item.active
				console.log(e.index)
				if(e.index==0){
					uni.showModal({
						title: '提示',
						content:'确认要组织批量导入课程吗',
						success: function(res) {
							
							if (res.confirm) {
								// console.log('用户点击确定')
								
								return new Promise((req,rej)=>{
									uni.request({
										url:'http://101.37.175.115/api/Schedule/GroupImport/?token=' + that.useMsg.token,
										method:'POST',
										data:{
											OrgID:that.useMsg.OrgID
										},
										
										success: (res) => {
											req(res.data)
											console.log('http://101.37.175.115/api/Schedule/GroupImport/?token=' + that.useMsg.token)
										},
										fail: (err) => {
											console.log(err)
											rej(err)
										}
									})
								})
							} else if (res.cancel) {
								// console.log('用户点击取消')
							}
						}
					})
				}else if(e.index==1){
					uni.showModal({
						title: '提示',
						content:'确认要创建课程吗',
						
						success: function(res) {
							if(res.confirm){
								uni.navigateTo({
									url:'./addCourse'
								})
							}
						}
						
					})
					
					
				}
				
			},
			leftClick(){
				uni.navigateTo({
					url:'../index/index'
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
		rightClick(){
				uni.navigateTo({
					url:"./addCourse"
				})
			},
		},
		async onLoad(){ 
			
			let dat = new Date
			this.today = dat.getDay()
			
			this.useMsg = await this.getToken()
			console.log(this.useMsg.token)
			
			this.class = await this.getClass()
			if(this.class.content[0]!=undefined){
				this.content = this.class.content
				// console.log(this.content[0].Tag)
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
