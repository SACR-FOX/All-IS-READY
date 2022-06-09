<template>
	<view>
		
		   
		
		
		<view class="radius">
			
			  <view class="icons">
			        <view class="icon_g1" @click="toOrgInfo">
			           <view id="g1_img" > 
			             <image src="../../static/Class.png"></image> 
			           </view>
			           <view id="g1_text">
			              <text>我的组织</text>
			           </view>
			        </view>
			        <view class="icon_g2" @click="toTask">
			           <view id="g2_img">
			             <image src="../../static/Task.png"></image> 
			           </view>
			           <view id="g2_text">
			             <text>组织任务</text>
			           </view>
			        </view>
			
			        <view class="icon_g3" @click="CreateClass">
			          <view id="g3_img">
			            <image src="../../static/CreateClass.png"></image>
			          </view>
			          <view id="g3_text">
			            <text>创建组织</text>
			          </view>
			        </view>
			
			        <view class="icon_g4" @click="CreateTask">
			          <view id="g4_img">
			            <image src="../../static/CreateTask.png"></image>
			          </view>
			          <view id="g4_text">
			            <text>发布任务</text>
			          </view>
			        </view>
			  </view>
		</view>
	
	<view class="block1">
	   <text class="inner_text">最近任务</text>
	   
	   <view class="Record_field" >
	          <view class="record" v-for="(item, index) in TaskList.slice(0,4)">
	            <text >{{item.TaskName}}</text>
	          </view>
	         
	   </view>
	</view>
	
	<view class="block2">
	  <text class="inner_text">组织通知</text>
	  
	  <view class="Record_field">
	            <view class="record">
	              <text>暂无事项</text>
	            </view>
	           
	  </view>
	  
	</view>
		<view class="scan" style=" position: absolute;bottom: 80rpx; left: 38%; display: flex;flex-direction: column;justify-content: center;align-items: center;
		" @click="scan">
			
			<u-icon name="scan" size=120rpx></u-icon>
			<text>扫码更换组织</text>
		</view>
			
	<tm-dialog title="提 示" :showCancel=false v-model="scanSuccess" content="重新登陆以切换组织" @confirm="logout()"></tm-dialog>
	</view>
        
	
</template>

<script>
	export default {
		data() {
			return {
				codeInfo:0,
				scanSuccess:false,
				TaskList:[],
				userInfo:{},
				prefix:"http://101.37.175.115/api/",
			}
		},
		methods: {
			switchOrg(){
				var that=this;
				uni.request({
					url: that.prefix + 'User/Detail/InfoModify/' + '?token=' + that.usrInfo.token,
					method:'PUT',
					data:{
						OrgID:that.$data.codeInfo,
						
					},
					success: (res) => {
						console.log(res.data)
						that.scanSuccess=true
					},		
					
				}) 
				uni.navigateTo({
					url:"../Login/Login"
				})
			},
			logout(){
				uni.removeStorage({
					key:"userMsg",
					success: (res) => {
						console.log(res)
						uni.navigateTo({
							url:"../Login/Login"
						})
					}
				})
			},
			
			leftClick(){
				uni.navigateTo({
					url:'../index/index'
				})
			},
			toOrgInfo(){
				uni.navigateTo({
					url:"./MyOrginization"
				})
			},
			CreateTask(){
				uni.navigateTo({
					url:'./CreateTask'
				})
			},
			CreateClass(){
				uni.navigateTo({
					url:'./CreateOrg'
				})
			},
			toTask(){
				uni.navigateTo({
					url:'./TaskList'
				})
			},
			getTaskList(){
				var that=this;
				return new Promise((req,rej)=>{
					uni.request({
						url: that.prefix + 'Organization/Task/All' + '?token=' + that.usrInfo.token+'&page=1',
						method:'GET',
						
						success: (res) => {
							
							that.$data.TaskList=res.data.data
							
							
							
						},		
						
					})
					
				})
			},
			getUserInfo(){
				return new Promise((req,rej)=>{
					uni.getStorage({
						key: 'userMsg',
						success: function (res) {
								req(res.data)
							},
					})
				})
			},
			scan(){
				var that=this
				uni.scanCode({
					success: function (res) {
						console.log('条码内容：' + res.result);
						that.codeInfo=res.result
						that.switchOrg()
					}
				});
			}
		},
		async onLoad() {
			this.usrInfo = await this.getUserInfo()
			console.log(this.usrInfo.token)
			await this.getTaskList()
			
		},
		
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
	margin-top: 13%;
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

.block1{
	height: 30%; 
	width:92%;
	background: #ffeaa7;
	border-width: 0px 0px 0px 0px;	
	border-style: solid;
	border-radius: 25px 25px 25px 25px;	
	position: absolute;
	top:20%; left:4%;
	display: flex;
	flex-direction: row;
	justify-content: space-evenly;
}
.block2{
	height: 30%; 
	width:92%;
	background:#dfe6e9;
	border-width: 0px 0px 0px 0px;	
	border-style: solid;
	border-radius: 25px 25px 25px 25px;	
	position: absolute;
	top:52%; left:4%;
	display: flex;
	flex-direction: row;
	justify-content: space-evenly;
}

.Record_field{
	 /* background-color: pink; */
	 width: 85%;
	 height: 70%;
	 margin-top: 15%;
	 display: flex;
	 flex-direction: column;
	justify-content: space-evenly;
}
.inner_text{
	 position: absolute;
	 top:10%; left: 7%;	 
	 font-size:20px;
	 font-family:'Times New Roman', 'Times, serif';
	 font-weight: 800;
}


</style>
