<template>
	<view >
		<u-navbar
		           title="创建组织任务"
		           @leftClick="leftClick"
		           :autoBack="true"
		       >
		       </u-navbar>
			
			   <view class="topBlock"></view>
			   
			   <view style="display: flex;justify-content: center;">
					<view class="bottomLayer">
						<tm-form
								@submit="submit"
								ref="formData"
								@request="success"
								method="post">
									<tm-input name="title" required title="任务名称" v-model="newTask.TaskName"></tm-input>
									<tm-input name="title" required title="任务负责人" v-model="newTask.Creator"></tm-input>
									
									
									<tm-pickersDate  @confirm="dateSe_1" :show-detail="{year:true,month:true,day:true,hour:true,min:true,sec:false}">
										<tm-listitem title="任务开始时间" left-icon="../../static/TimeStart.png" :value=tmpTimeShowStart  show-left-icon :show-right-icon=false ></tm-listitem>
									</tm-pickersDate>
										
								<tm-pickersDate   @confirm="dateSe_2" :show-detail="{year:true,month:true,day:true,hour:true,min:true,sec:false}">
									<tm-listitem title="任务结束时间" left-icon="../../static/TimeDue.png" show-left-icon :value=tmpTimeShowDue  show-left-icon :show-right-icon=false></tm-listitem>
								</tm-pickersDate>
			
									<tm-input :vertical="true" :height="120" title="任务描述" :maxlength="100"  :border-bottom="false" :required="false" placeholder="请输入关于此次任务的说明"  input-type="textarea" v-model="newTask.Description" bg-color="grey-lighten-5" clear></tm-input>
								
								</tm-form>
								<view class="submit" style="display: flex; height: 90rpx; margin-top: 40rpx;justify-content: center;">
									<tm-button theme="bg-gradient-red-accent" size="g">提 交</tm-button>
								</view>
									
								

					</view>
			   </view>
				
	
			   
			
			   
			   
	</view>
</template>

<script>
	import tmForm from '@/tm-vuetify/components/tm-form/tm-form.vue';
	import tmInput from '@/tm-vuetify/components/tm-input/tm-input.vue';
	import tmButton from '@/tm-vuetify/components/tm-button/tm-button.vue';
	import tmListitem from '@/tm-vuetify/components/tm-listitem/tm-listitem.vue';
	import tmPickersDate from '@/tm-vuetify/components/tm-pickersDate/tm-pickersDate.vue'
	
	export default {
		
		components: {tmForm,tmInput,tmButton,tmListitem,tmPickersDate},
		data() {
			return {
				showTimePicker:false,
				turn:0,
			
				tmpTimeShowStart:"",
				tmpTimeShowDue:"",
				newTask:{
					OrgID:-1,
					TimeStart:Number(new Date()) ,
					TimeDue:Number(new Date())+3600,
					Description:"",
					TaskName:"",
					Creator:"default",
					CID:0
				},
				
			}
		},
		methods: {
			leftClick(){
				uni.navigateTo({
					url:"./Organization"
				})
			},
			timeFormat(val){
	
				var date = new Date(val);
				var result=date.getTime()
				return result;
			},
			dateSe_1(e){
				
				var tmp= e.year+'-'+e.month + '-' + e.day+' '+e.hour+':'+e.min;
				this.tmpTimeShowStart =tmp;
				this.$data.newTask.TimeStart=this.timeFormat(tmp)
				console.log(this.$data.newTask.TimeStart)
			},
			dateSe_2(e){
				var tmp= e.year+'-'+e.month + '-' + e.day+' '+e.hour+':'+e.min;
				this.tmpTimeShowDue =tmp;
				this.$data.newTask.TimeDue=this.timeFormat(tmp)
				console.log(this.$data.newTask.TimeDue)
			},
			
			
			
		}
	}
</script>

<style>
	.topBlock{
		height: 120rpx;
	}
	.inputArea{
		display: flex;
		align-items: center;
		justify-content:fl;
	}
	.bottomLayer{
		width: 90%;
		height: 1000rpx;
		background-color: #ffffff;
		border-radius: 60rpx 60rpx 60rpx 60rpx;
		padding-top: 60rpx;
	}
	page{
		background-color: #f7f1e3;
	}
	
</style>
