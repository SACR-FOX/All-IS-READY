<template>
		<view>
			 <u-navbar
			            title="组织信息"
			            @leftClick="leftClick"
			            :autoBack="true"
			        >
			        </u-navbar>
					<view class="block"></view>
			<view class="orgName">
				<text>计科1902 组织信息</text>
			</view>
			
	
				
				<tm-grouplist title="基础信息" title-theme="blue text" :shadow="24" :round="10" :padding="[42, 42]">
							<tm-listitem title="组织ID" left-icon="icon-QQ" show-left-icon :show-right-icon=false value="xx"></tm-listitem>
							<tm-listitem title="组织名称" left-icon="icon-collection-fill" show-left-icon left-icon-color="pink" :show-right-icon=false></tm-listitem>
							<tm-listitem title="负责人" left-icon="icon-user-fill" show-left-icon left-icon-color="green" :show-right-icon=false></tm-listitem>
							
							<tm-listitem group title="组织描述" left-icon="icon-QQ" show-left-icon :show-right-icon=false>
							<template v-slot:group>
								<tm-sheet :margin="[0, 0]" :shadow="0" color="blue text"><view>这里面可以放任意内容、</view></tm-sheet>
							</template>
						</tm-listitem>
							<tm-listitem title="成员数" left-icon="icon-user-fill" show-left-icon :show-right-icon=false></tm-listitem>
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
				OrgID:1,
				color:"#45aaf2"
			}
		},
		methods: {
			leftClick() {
			    uni.navigateTo({
			    	url:"./Organization"
			    })
			},
			genCode(){
				qr = new QRCode('canvas', {
				      // usingIn: this,
				      text: this.$data.OrgID,
				      width: 150,
				      height: 150,
				      colorDark: this.$data.color,
				      colorLight: "white",
				      correctLevel: QRCode.CorrectLevel.H,
				  })
			}
		},
		
		onReady(){
			this.genCode()
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