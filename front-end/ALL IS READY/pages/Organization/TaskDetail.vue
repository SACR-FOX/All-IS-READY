<template>
	<view>
		<u-navbar
		           title="任务详情"
		           @leftClick="leftClick"
		           :autoBack="true"
		       >
		       </u-navbar>
			    <view class="topBlock"></view>
				
			   <tm-grouplist title="任务信息" title-theme="blue text" :shadow="24" :round="10" :padding="[42, 42]">
			   			<tm-listitem title="任务名" left-icon="icon-QQ" show-left-icon :show-right-icon=false></tm-listitem>
			   			<tm-listitem title="创建者" left-icon="icon-user-fill" show-left-icon left-icon-color="pink" :show-right-icon=false></tm-listitem>
			   			
						<tm-listitem group title="任务描述" left-icon="icon-QQ" show-left-icon :show-right-icon=false>
							<template v-slot:group>
								<tm-sheet :margin="[0, 0]" :shadow="0" color="blue text"><view>这里面可以放任意内容、</view></tm-sheet>
							</template>
						</tm-listitem>
						<tm-listitem title="任务开始时间" left-icon="../../static/TimeStart.png" show-left-icon :show-right-icon=false></tm-listitem>
						<tm-listitem title="任务截止时间" left-icon="../../static/TimeDue.png" show-left-icon :show-right-icon=false></tm-listitem>
						<tm-listitem title="已完成人数" left-icon="icon-user-fill" show-left-icon left-icon-color="green" :show-right-icon=false></tm-listitem>
				
			   		</tm-grouplist>
					
					<view class="submit">
						<tm-button theme="bg-gradient-red-accent" size="g" >确认完成</tm-button>
					</view>
	</view>
</template>

<script>
	import tmListitem from '@/tm-vuetify/components/tm-listitem/tm-listitem.vue';
	import tmGrouplist from '@/tm-vuetify/components/tm-grouplist/tm-grouplist.vue';
	import tmSheet from '@/tm-vuetify/components/tm-sheet/tm-sheet.vue';
	import tmButton from '@/tm-vuetify/components/tm-button/tm-button.vue';
	
	export default {
		components: {tmListitem,tmGrouplist,tmSheet,tmButton},
		data() {
			return {
				
			}
		},
		methods: {
			leftClick(){
				uni.navigateTo({
					url:"../TaskList"
				})
			},
			timeFormat(val) {
				var date = new Date(val); //时间戳为10位需*1000，时间戳为13位的话不需乘1000
				var year = date.getFullYear();
				var month = ("0" + (date.getMonth() + 1)).slice(-2);
				var sdate = ("0" + date.getDate()).slice(-2);
				var hour = ("0" + date.getHours()).slice(-2);
				var minute = ("0" + date.getMinutes()).slice(-2);
				var result = year + "-" + month + "-" + sdate + " " + hour + ":" + minute ;
				return result;
			},
		}
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
