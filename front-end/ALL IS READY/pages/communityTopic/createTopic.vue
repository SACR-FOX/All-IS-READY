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
				<!-- <u-icon name="checkbox-mark" size="19"></u-icon> -->
			</view>
		
		<u--input
		    placeholder="请输入话题名字"
		    border="bottom"
		    clearable style="margin-top: 100rpx;"
		  ></u--input>
		  
		  <u--textarea  placeholder="从这里开始分享..." style="height: 300rpx"></u--textarea>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
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

</style>
