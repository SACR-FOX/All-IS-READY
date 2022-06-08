<template>
	<view>
<!-- 		<u-navbar
		    title="帖子"
		    @rightClick="rightClick"
		    :autoBack="true">
		</u-navbar> -->
		<!-- <web-view :src="Url" ></web-view> -->
<!-- 		<button style="margin-top: 500rpx;" @click="">aaaa</button> -->
	</view>
</template>

<script>
	export default {
		data() {
			return {
				fileUrl:"",
				Url : "http://101.37.175.115/api/",
				userMsg : {},
				id : ''
			}
		},
		methods: {
			loadFile(url){
				console.log(url)
				uni.downloadFile({
					url: url,
					success: (res) => {
						console.log(res.tempFilePath)
						if (res.statusCode === 200) {
							uni.openDocument({
								filePath: encodeURI(res.tempFilePath), 
				                    // 如果文件名包含中文，建议使用escape(res.tempFilePath)转码，防止ios和安卓客户端导致的差异
									success: function(res) {
										console.log(res)
										console.log('打开文档成功');
									},
									fail: (err) => {
										console.log(err)
									}
							});
						}
					},
					fail: (err) => {
						console.log(err)
					}
				});
			},
			
			getUserMsg(){
							return new Promise((req,rej) =>{
								uni.getStorage({
									key:"userMsg",
									success:(res)=>{
			//							console.log("success")
										this.userMsg = res.data
										req("success")
									},
									fail: (err) => {
										console.log("err")
										uni.reLaunch({
											url:"../Login/Login"
										})
									}
								})
							})
						},
			
			getFileInfo(){
				console.log(this.id)
				console.log(this.Url + 'Files/OnlinePreview?token=' + this.userMsg.token + "&FileID=" + this.id)
				return new Promise((req,rej)=>{
					uni.request({
						url: this.Url + 'Files/OnlinePreview?token=' + this.userMsg.token + "&FileID=" + this.id,
						success: (res) => {
							console.log(res.data.url)
							req(res.data.url)
						}
					})
				})
			}
		},
		async onLoad (option) {
			this.id = option.ID
			await this.getUserMsg()
			this.fileUrl = await this.getFileInfo()
			console.log(this.fileUrl)
			this.loadFile(this.fileUrl)
			// console.log(await this.getFileInfo().url)
			
		   
		   
		}
	}
</script>

<style>

</style>
