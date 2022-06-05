<template>
	<view>
		<view>
		        <u-navbar
		            title="创建话题"
		            @rightClick="rightClick"
		            :autoBack="true"
					rightText="发布"
		        >
		        </u-navbar>
			</view>
		
		<view class="row">
			<u--input
				v-model="c1"
			    placeholder="请输入社区名字"
			    border="bottom"
			    clearable
				autoHeight
				style=""
			  ></u--input>
			  <u-upload
			  		:fileList="fileList1"
			  		@afterRead="afterRead"
			  		@delete="deletePic"
			  		name="1"
			  		multiple
			  		:maxCount="1"
					style="margin-left: 300rpx;"
			  	></u-upload>
		</view>
		  
		  <u--textarea v-model="c2" placeholder="请输入社区描述" autoHeight style="height: 300rpx;"></u--textarea>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				fileList1: [],
				c1:'',
				c2:''
			}
		},
		methods: {
			rightClick(){
				uni.showToast({
					
				})
			},
			create(){
				let that = this
				return new Promise((req,rej)=>{
					uni.request({
						url: '1',
						method:'POST',
						
						success: (res) => {
							req(res.data)
							console.log(that.Url + 'Community/Post/' + PostID + '/Star/' + "?token=" + that.useMsg.token)
						},
						fail: (err) => {
							req(err)
						}
					})
				})
			}
		}
	}
</script>

<style>
	.row{
		display: flex;
		flex-direction: row;
		margin-top: 100rpx;
	}
</style>
