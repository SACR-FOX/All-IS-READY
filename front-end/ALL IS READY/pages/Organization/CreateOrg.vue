<template>
	<view>
		<u-navbar
		           title="创建组织"
		           @leftClick="leftClick"
		     
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
									<tm-input name="title" required title="组织名称" v-model="newOrg.OrgName"></tm-input>
								
									<tm-listitem title="组织负责人" left-icon="icon-collection-fill" show-left-icon left-icon-color="red" :show-right-icon=false :value="usrInfo.Uname"
									
									></tm-listitem>
									<tm-input :vertical="true" :height="120" title="组织简介" :maxlength="100"  :border-bottom="false" :required="false" placeholder="请输入组织介绍"  input-type="textarea" v-model="newOrg.Description" bg-color="grey-lighten-5" clear></tm-input>
								
								</tm-form>
								<view class="submit" style="display: flex; height: 90rpx; margin-top: 80rpx;justify-content: center;">
									<tm-button theme="bg-gradient-red-accent" size="g" @click="submit">创 建</tm-button>
								</view>
									
								<tm-dialog title="创建结果" :showCancel=true v-model="success" content="是否重新登陆以切换组织" @confirm="switchOrg()" @cancel="success=false"></tm-dialog>
								<tm-dialog title="创建结果" :showCancel=false v-model="failed" content="创建失败:组织名已存在" ></tm-dialog>

					</view>
				</view>
				<view class="qrCode">
				  <canvas class='canvas' canvas-id='canvas'></canvas>
				  
				</view>
								
	</view>
</template>

<script>
	import tmForm from '@/tm-vuetify/components/tm-form/tm-form.vue';
	import tmInput from '@/tm-vuetify/components/tm-input/tm-input.vue';
	import tmButton from '@/tm-vuetify/components/tm-button/tm-button.vue';
	import tmListitem from '@/tm-vuetify/components/tm-listitem/tm-listitem.vue';
	import tmDialog from '@/tm-vuetify/components/tm-dialog/tm-dialog.vue';
	var qr;
	var QRCode = require('../../utils/weapp-qrcode.js')
	export default {
		components: {tmForm,tmInput,tmButton,tmListitem,tmDialog},
		data() {
			return {
				newOrg:{
					OrgName:"",
					Description:"",
					Monitor:-1,
					},
					prefix:"http://101.37.175.115/api/",					
					usrInfo:{},
					success:false,
					failed:false,
					newID:-1,
					color:"#45aaf2",
					
			}
		},
		methods: {
			leftClick(){
				uni.navigateTo({
					url:"./Organization"
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
			getUserInfo(){
				var that=this
				uni.getStorage({
					key: 'userMsg',
					success: function (res) {
							that.$data.usrInfo =res.data
							that.$data.newOrg.Monitor=that.$data.usrInfo.UID						
						},
				})
			},
			genCode(){
				var that=this
				
				qr = new QRCode('canvas', {
				      // usingIn: this,
					  
				      text:   String(that.$data.newID) ,
				      width: 150,
				      height: 150,
				      colorDark: this.$data.color,
				      colorLight: "white",
				      correctLevel: QRCode.CorrectLevel.H,
				  })
			},
			submit(){
				var that=this;
				uni.request({
					url: that.prefix + 'Organization/Action/' + '?token=' + that.usrInfo.token,
					method:'POST',
					data:{
						
						OrgName:that.$data.newOrg.OrgName,
						Description:that.$data.newOrg.Description,
						MonitorID:that.$data.newOrg.Monitor,
						
					},
					success: (res) => {
						console.log(res.data)
						if(res.data.OrgID!=null){
							that.$data.newID=res.data.OrgID
							that.genCode()
							that.$data.success=true
							
						}else{
							that.$data.failed=true
						}
						
					},		
					
				}) 
				
			},
			switchOrg(){
				var that=this;
				uni.request({
					url: that.prefix + 'User/Detail/InfoModify/' + '?token=' + that.usrInfo.token,
					method:'PUT',
					data:{
						OrgID:that.$data.newID,
						
					},
					success: (res) => {
						console.log(res.data)
						that.$data.success=false
						that.logout()

					},		
					
				}) 
				uni.navigateTo({
					url:"../Login/Login"
				})
			}
		},
		onLoad(options) {
			
			this.getUserInfo()
			
			
		},
	}
</script>

<style>
	.topBlock{
		height: 300rpx;
	}
	.inputArea{
		display: flex;
		align-items: center;
		justify-content:fl;
	}
	.bottomLayer{
		width: 90%;
		height: 800rpx;
		background-color: #ffffff;
		border-radius: 60rpx 60rpx 60rpx 60rpx;
		padding-top: 60rpx;
	}
	.qrCode{
		position: relative;
		top: 80rpx;
		left: 29%;
		
	}
page{
		background-color: #f7f1e3;
	}
</style>
