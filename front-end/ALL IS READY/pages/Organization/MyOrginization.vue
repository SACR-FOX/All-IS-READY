<template>
		<view>
			
				
			<view class="orgName">
				<text>{{OrgInfo.OrgName}} 组织信息</text>
			</view>
			
	
				
				<tm-grouplist title="基础信息" title-theme="blue text" :shadow="24" :round="10" :padding="[42, 42]">
							<tm-listitem title="组织ID" left-icon="icon-QQ" show-left-icon :show-right-icon=false :value="OrgInfo.OrgID.toString()"></tm-listitem>
							<tm-listitem title="组织名称" left-icon="icon-collection-fill" show-left-icon left-icon-color="pink" :show-right-icon=false :value="OrgInfo.OrgName"></tm-listitem>
							<tm-listitem title="负责人" left-icon="icon-user-fill" show-left-icon left-icon-color="green" :show-right-icon=false :value="OrgInfo.Monitor"></tm-listitem>
							
							<tm-listitem group title="组织描述" left-icon="icon-QQ" show-left-icon :show-right-icon=false>
							<template v-slot:group>
								<tm-sheet :margin="[0, 0]" :shadow="0" color="blue text"><view>{{OrgInfo.Description}}</view></tm-sheet>
							</template>
						</tm-listitem>
							<tm-listitem title="成员数" left-icon="icon-user-fill" show-left-icon :show-right-icon=false :value="OrgInfo.aggregate.toString()"></tm-listitem>
						</tm-grouplist>
				
				<view class="qrCode">
				  <canvas class='canvas' canvas-id='canvas'></canvas>
				  
				</view>
		</view>
	
</template>

<script>
	import tmListitem from '@/tm-vuetify/components/tm-listitem/tm-listitem.vue';
	import tmGrouplist from '@/tm-vuetify/components/tm-grouplist/tm-grouplist.vue';
	import tmSheet from '@/tm-vuetify/components/tm-sheet/tm-sheet.vue';
	
	
	var qr;
	var QRCode = require('../../utils/weapp-qrcode.js')
	export default {
		components: {tmListitem,tmGrouplist,tmSheet},
		data() {
			return {
				imgUrl:"",
				OrgInfo:{
					"Monitor":"",
					"aggregate":-1,
					"OrgName":"",
					"OrgID":-1,
					"Description":"",
				},
				color:"#45aaf2",
				usrInfo:{
					
				},
				prefix:"http://101.37.175.115/api/"
			}
		},
		methods: {
			leftClick() {
			    uni.navigateTo({
			    	url:"./Organization"
			    })
			},
			genCode(){
				var that=this
				
				qr = new QRCode('canvas', {
				      // usingIn: this,
					  
				      text:   String(that.$data.OrgInfo.OrgID) ,
				      width: 150,
				      height: 150,
				      colorDark: this.$data.color,
				      colorLight: "white",
				      correctLevel: QRCode.CorrectLevel.H,
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
			getOrgInfo(){
				var that=this
				
				return new Promise((req,rej)=>{
				uni.request({
					url: that.prefix + 'Organization/Info' + '?token=' + that.usrInfo.token+'&OrgID='+that.usrInfo.OrgID,
					method:'GET',
					data:{
						OrgID:String(that.usrInfo.OrgID)
					},
					success: (res) => {
						console.log(res.data)
						that.$data.OrgInfo=res.data
						that.genCode()
					},
					
					
				})
				})

				
			}
		},
		async onLoad() {
			this.usrInfo = await this.getUserInfo()
			console.log(this.usrInfo.token)
			await this.getOrgInfo()
			
		},
		
		onReady(){
			
		}
	}
	
	
	
</script>

<style>
	.orgName{
		height: 100rpx;
		width: 100%;
		background-color: #0984e3;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 40rpx;
		color:#ecf0f1 ;
		font-weight: 600;
		margin-bottom: 80rpx;
	}
	.item{
		background-color: #0984e3;
	}
	.cell-hover-class {
		background-color: rgb(235, 237, 238);
	}
	
	/* 或者单是设置透明度 */
	.cell-hover-class {
		opacity: 0.5;
	}
	.block{
		height: 100rpx;
	}
	.qrCode{
		position: relative;
		top: 160rpx;
		left: 29%;
		
	}
</style>