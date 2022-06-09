<template>
	<view>
		<u-navbar
		           title="任务详情"
		           @leftClick="leftClick"
		         
		       >
		       </u-navbar>
			    <view class="topBlock"></view>
				
			   <tm-grouplist title="任务信息" title-theme="blue text" :shadow="24" :round="10" :padding="[42, 42]">
			   			<tm-listitem :value="TaskDetail.TaskName"  title="任务名" left-icon="../../static/task-list.png" show-left-icon :show-right-icon=false></tm-listitem>
			   			<tm-listitem :value="TaskDetail.Creator" title="创建者" left-icon="icon-user-fill" show-left-icon left-icon-color="pink" :show-right-icon=false></tm-listitem>
			   			
						<tm-listitem group title="任务描述" left-icon="icon-QQ" show-left-icon :show-right-icon=false>
							<template v-slot:group>
								<tm-sheet :margin="[0, 0]" :shadow="0" color="blue text"><view>{{TaskDetail.Description}}</view></tm-sheet>
							</template>
						</tm-listitem>
						<tm-listitem :value="TaskDetail.TimeStart" title="任务开始时间" left-icon="../../static/TimeStart.png" show-left-icon :show-right-icon=false></tm-listitem>
						<tm-listitem :value="TaskDetail.TimeDue" title="任务截止时间" left-icon="../../static/TimeDue.png" show-left-icon :show-right-icon=false></tm-listitem>
						<tm-listitem :value="String(TaskDetail.AckCount) " title="已完成人数" left-icon="icon-user-fill" show-left-icon left-icon-color="green" :show-right-icon=false></tm-listitem>
				
			   		</tm-grouplist>
					<tm-dialog title="确认结果" :showCancel=false v-model="ACKsuccess" content="确认成功!" @confirm="ackOK"></tm-dialog>
					<tm-dialog title="确认结果" :showCancel=false v-model="ACKfailed" content="任务已过期" @confitm="leftClick"></tm-dialog>
					
					<view class="submit">
						<tm-button :theme="buttonTheme" size="g" :disabled="buttonDisable" @click="ACK()">{{buttonText}} </tm-button>
					</view>
	</view>
</template>

<script>
	import tmListitem from '@/tm-vuetify/components/tm-listitem/tm-listitem.vue';
	import tmGrouplist from '@/tm-vuetify/components/tm-grouplist/tm-grouplist.vue';
	import tmSheet from '@/tm-vuetify/components/tm-sheet/tm-sheet.vue';
	import tmButton from '@/tm-vuetify/components/tm-button/tm-button.vue';
	import tmDialog from '@/tm-vuetify/components/tm-dialog/tm-dialog.vue';
	
	export default {
		components: {tmListitem,tmGrouplist,tmSheet,tmButton,tmDialog},
		data() {
			return {
				userInfo:{},
				TaskID:0,
				TaskDetail:{},
				prefix:"http://101.37.175.115/api/",
				buttonText:"确认完成",
				buttonTheme:"bg-gradient-red-accent",
				buttonDisable:false,
				ACKsuccess:false,
				ACKfailed:false,
			}
		},
		methods: {
			leftClick(){
				uni.navigateTo({
					url:"./TaskList"
				})
			},
			ackOK(){
				this.$data.ACKsuccess=false
				uni.navigateTo({
					url:"./TaskList"
				})
			},
			
			timeFormat(val) {
				
				var date = new Date(val*1000); //时间戳为10位需*1000，时间戳为13位的话不需乘1000
				var year = date.getFullYear();
				var month = ("0" + (date.getMonth() + 1)).slice(-2);
				var sdate = ("0" + date.getDate()).slice(-2);
				var hour = ("0" + date.getHours()).slice(-2);
				var minute = ("0" + date.getMinutes()).slice(-2);
				var result = year + "-" + month + "-" + sdate + " " + hour + ":" + minute ;
		
				return result;
			},
			ACK(){
				var that=this;
				uni.request({
					url: that.prefix + 'Organization/Task/ACK' + '?token=' + that.usrInfo.token+'&page='+that.page,
					method:'POST',
					data:{
						"TaskID":that.$data.TaskDetail.TaskID
					},
					success: (res) => {
						if(res.data.Status==true){
							that.$data.buttonDisable=true,
							that.$data.buttonTheme="grey",
							that.$data.buttonText="已确认"
							that.$data.ACKsuccess=true
							
						}else if(res.data.result=="Task Due"){
							that.$data.buttonDisable=true,
							that.$data.buttonTheme="grey",
							that.$data.buttonText="任务已截止"
							that.$data.ACKfailed=true
						}
						
					},		
					
				})
			},
			checkACK(){
				var that=this;
				uni.request({
					url: that.prefix + 'Organization/Task/ACK' + '?token=' + that.usrInfo.token+'&TaskID='+that.TaskDetail.TaskID,
					method:'GET',
	
					success: (res) => {
						if(res.data.Status==true){
							that.$data.buttonDisable=true,
							that.$data.buttonTheme="grey",
							that.$data.buttonText="已确认"
						}if(res.data.Status==false){
							that.$data.buttonDisable=false

						}
						
					},		
					
				})
			},
			getTaskDetail(){
				var that=this;
				return new Promise((req,rej)=>{
					uni.request({
						url: that.prefix + 'Organization/Task/Action/'+that.$data.TaskID+'/' + '?token=' + that.usrInfo.token,
						method:'GET',
						
						success: (res) => {
							that.$data.TaskDetail=res.data
							that.$data.TaskDetail.TimeStart=that.timeFormat(that.$data.TaskDetail.TimeStart)
							that.$data.TaskDetail.TimeDue=that.timeFormat(that.$data.TaskDetail.TimeDue)
							that.checkACK()
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
		},
		
		async onLoad(options) {
			
			this.usrInfo = await this.getUserInfo()
			this.TaskID=options.TaskID
			console.log(this.TaskID)
			await this.getTaskDetail()
			
			
		},
	}
</script>

<style>
.topBlock{
		height: 120rpx;
	}
	page{
		background-color: #f1f2f6;
	}
	.submit{
		position: relative;
		top: 90rpx;
	
		height: 120rpx;
		display: flex;
		justify-content: center;
		align-items: center;
	}
</style>
