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
		
		<view class="course" v-for="(item,index) in list2" :style="{backgroundColor:item.Tag}">
				<text class="time">{{item.Time}}</text>
				<text class="curName">{{item.curName}}</text>
				<text class="room">{{item.room}}</text>
			</view>
		</view>
		
		
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				list1: [{
                    name: '星期天',
					currentIndex:0,
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
				
					list2: [{
						"curName" :"编译原理",
						"Time" : "8:05",
						"room" : "E413",
						"Tag" : "rgba(246, 229, 141,1.0)"
					},
					{
						"curName" :"移动软件开发",
						"Time" : "9:40",
						"room" : "信息实验室4",
						"Tag" : "rgba(255, 190, 118,1.0)"
					},
					{
						"curName" :"操作系统",
						"Time" : "13:40",
						"room" : "E317",
						"Tag" : "rgba(186, 220, 88,1.0)"
					},
					{
						"curName" :"操作系统实验",
						"Time" : "18:30",
						"room" : "信息实验室5",
						"Tag" : "rgba(255, 121, 121,1.0)"
					}
					]
				}
				
		},
		methods: {
			change(item){
				console.log('item',item)
				this.currentIndex = item
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
	}
	.time{
		margin-left: 30rpx;
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
