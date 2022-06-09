<template>
	<view >
		<u-navbar
		           title="创建课程表项"
		           @leftClick="leftClick()"
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
									<tm-input name="title"  title="课程名称" v-model="newCur.CurName"></tm-input>
									<tm-input name="title"  title="课程地点" v-model="newCur.Location"></tm-input>
									<tm-pickers :list="['周一','周二','周三','周四','周五','周六','周日']" @confirm='daySe'>
										<tm-listitem title="课程日期" left-icon="../../static/classDay.png" show-left-icon :show-right-icon=false :value="showDay"></tm-listitem>
									</tm-pickers>
									
									
									<tm-pickersDate start="2019-1-1" end="2023-12-31" @confirm="dateSe_1" :show-detail="{year:false,month:false,day:false,hour:true,min:true,sec:false}">
										<tm-listitem title="课程开始时间" left-icon="../../static/TimeStart.png"  :value=tmpTimeShowStart  show-left-icon :show-right-icon=false ></tm-listitem>
									</tm-pickersDate>
										
								<tm-pickersDate  start="2019-1-1" end="2023-12-31" @confirm="dateSe_2" :show-detail="{year:false,month:false,day:false,hour:true,min:true,sec:false}">
									<tm-listitem title="课程结束时间" left-icon="../../static/TimeDue.png" show-left-icon :value=tmpTimeShowDue  show-left-icon :show-right-icon=false></tm-listitem>
								</tm-pickersDate>
								<tm-pickers :list="['专业','选修','通识','体育','其他','公共']" @confirm='classSe'>
									<tm-listitem title="标签分组" left-icon="../../static/classTag.png" show-left-icon :show-right-icon=false :value="showTag"></tm-listitem>
								</tm-pickers>
								
								
									<!-- <tm-input :vertical="true" :height="120" title="任务描述" :maxlength="100"  :border-bottom="false" :required="false" placeholder="请输入关于此次任务的说明"  input-type="textarea" v-model="newCur.Description" bg-color="grey-lighten-5" clear></tm-input> -->
								
								</tm-form>
								<view class="submit" style="display: flex; height: 90rpx; margin-top: 40rpx;justify-content: center;">
									<tm-button theme="bg-gradient-red-accent" size="g" @click="addCourse">创 建</tm-button>
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
	import tmPickers from '@/tm-vuetify/components/tm-pickers/tm-pickers.vue'
	export default {
		components: {tmForm,tmInput,tmButton,tmListitem,tmPickersDate,tmPickers},
		data() {
			return {
				showTimePicker:false,
				turn:0,
				showDay:"",
				showTag:"",
				tmpTimeShowStart:"",
				tmpTimeShowDue:"",
				useMsg:'',
				newCur:{
					Day:'',
					Tag:'',
					OrgID:-1,
					DurationStart:Number(new Date()) ,
					DurationEnd:Number(new Date())+3600,
					CurName:'',
					Location:'',
					UID:'',
					UUID:'',
				}

					
				
			}
		},
		methods: {
			uuid() {
			    var s = [];
			    var hexDigits = "0123456789abcdef";
			    for (var i = 0; i < 36; i++) {
			        s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
			    }
			    s[14] = "4"; // bits 12-15 of the time_hi_and_version field to 0010
			    s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1); // bits 6-7 of the clock_seq_hi_and_reserved to 01
			    s[8] = s[13] = s[18] = s[23] = "-";
			
			    var uuid = s.join("");
				// console.log(uuid)
			    return uuid;
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
			daySe(e){
				
				this.$data.newCur.Day=e[0].index+1
				this.$data.showDay=e[0].data
				
			},
			classSe(e){
				// console.log(e[0].data)
				this.$data.newCur.Tag = e[0].index
				this.$data.showTag=e[0].data
			},
			leftClick(){
				uni.navigateTo({
					url:"./classSchedule"
				})
			},
			timeFormat(val){
	
				var date = new Date(val);
				var result=date.getTime()
				console
				return result;
			},
			dateSe_1(e){
				// console.log(e)
				var time = e.hour*3600 + e.min*60
				var tmp=e.hour+':'+e.min;
				this.tmpTimeShowStart =tmp;
				this.$data.newCur.DurationStart=time
				console.log(this.$data.newCur.DurationStart)
			},
			dateSe_2(e){
				var time = e.hour*3600 + e.min*60
				var tmp= e.hour+':'+e.min;
				this.tmpTimeShowDue =tmp;
				this.$data.newCur.DurationEnd=time
				console.log(this.$data.newCur.DurationEnd)
			},
			
			addCourse(){
				let that = this
				return new Promise((req,rej)=>{
					uni.request({
						url:'http://101.37.175.115/api/Schedule/Action/?token=' + that.useMsg.token,
						method:'POST',
						data:this.newCur,
						
						success: (res) => {
							console.log(res.data)
							console.log(this.newCur.DurationStart)
							req(res.data)
							console.log('http://101.37.175.115/api/Schedule/Action/?token=' + that.useMsg.token)
							// console.log(res.data.content[0].Tag)
							uni.navigateTo({
								url:'./classSchedule'
							})
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
			this.newCur.UID = this.useMsg.UID
			this.newCur.UUID = await this.uuid()
			console.log(this.UUID)
			// console.log(this.uuid)
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
