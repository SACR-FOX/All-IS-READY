<template>
	<view>
		
		    <u-navbar
		            title="我的班级"
		            @rightClick="rightClick"
		            :autoBack="true"
		        >
		        </u-navbar>
		
		
		<view class="radius">
			
			  <view class="icons">
			        <view class="icon_g1" bindtap="toMyClass">
			           <view id="g1_img" > 
			             <image src="../../static/Class.png"></image> 
			           </view>
			           <view id="g1_text">
			              <text>我的班级</text>
			           </view>
			        </view>
			        <view class="icon_g2" bindtap="toTask">
			           <view id="g2_img">
			             <image src="../../static/Task.png"></image> 
			           </view>
			           <view id="g2_text">
			             <text>我的任务</text>
			           </view>
			        </view>
			
			        <view class="icon_g3" bindtap="CreateClass">
			          <view id="g3_img">
			            <image src="../../static/CreateClass.png"></image>
			          </view>
			          <view id="g3_text">
			            <text>创建班级</text>
			          </view>
			        </view>
			
			        <view class="icon_g4" bindtap="CreateTask">
			          <view id="g4_img">
			            <image src="../../static/CreateTask.png"></image>
			          </view>
			          <view id="g4_text">
			            <text>创建任务</text>
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
				
			}
		},
		methods: {
			
		}
	}
</script>

<style>
.radius{
	height: 25%; 
	width: 100%;
	background: #74b9ff;
	border-width: 0rpx 0rpx 0rpx 0rpx;	
	border-style: solid;
	border-radius: 0px 0px 60rpx 60rpx;
	 position: absolute;
	 top: 0rpx;left: 0rpx;
}
.icons{
	margin-top: 20%;
	height:140rpx;
	display: flex;
	flex-direction: row;
	align-items: center;
	justify-items: center;
	justify-content: space-evenly;
	/* background-color: pink; */
}
#g1_img image{
		width: 30px;
		height: 30px;
}
.icon_g2{
	width:70px;
	height:75px;
	display:flex;
	flex-direction: column;
	justify-content: space-evenly;
	align-items: center;
	color:#fff;
}
#g2_img image{
		width: 30px;
		height: 30px;
}
.icon_g3{
	width:70px;
	height:75px;
	display:flex;
	flex-direction: column;
	justify-content: space-evenly;
	align-items: center;
	color:#fff;
}
#g3_img image{
		width: 30px;
		height: 30px;
}
.icon_g4{
	width:70px;
	height:75px;
	display:flex;
	flex-direction: column;
	justify-content: space-evenly;
	align-items: center;
	color:#fff;
}
#g4_img image{
		width: 30px;
		height: 30px;
}
.icon_g1{
	width:70px;
	height:75px;
	display:flex;
	flex-direction: column;
	justify-content: space-evenly;
	align-items: center;
	color:#fff;
}
</style>
