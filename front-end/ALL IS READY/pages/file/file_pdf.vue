<template>
<!--直接在新页面打开预览 -->
<!-- 
  <view style="width: 100%;"  >
		     <web-view  :src="URL"></web-view>    				
	</view> -->
 
<!--如果是在已有的页面内插入 -->
<!-- 	<iframe
	      width="100%"
	      height="500"
	      scrolling="no"
	      :src="allUrl"
	    ></iframe> -->
</template>
 
<script>
	
 //    export default {
 //        data() {
 //            return {
	// 			src: '',
 //                allUrl:'',
	// 			viewerUrl: '../../hybrid/web/viewer.html', // 格式化文件流的一个js 文件 
				
	// 			URL : "http://all-is-ready-file-storage.oss-cn-hangzhou.aliyuncs.com/userPDF/1/%E7%94%B3%E8%AF%B7/invoice?OSSAccessKeyId=LTAI5tGWHb9WqaX55jRKoPyv&Expires=1654763947&Signature=Omu%2B5J9DCkiA5VOENkr7Xjgbz1w%3D",
				
	// 			Url : "http://101.37.175.115/api/",
	// 			userMsg : {},
	// 			id : '8',
	// 			file : '',
				
 //            }
 //        },
		
	// 	methods:{
			
	// 		loadFile(url){
	// 			console.log(url)
	// 			uni.downloadFile({
	// 				url: url,
	// 				success: (res) => {
						
	// 					if (res.statusCode === 200) {
	// 						// let blob = new BLOB
	// 						let fileUrl =  encodeURIComponent(res.tempFilePath) // encodeURIComponent 函数可把字符串作为 URI 组件进行编码。							
	// 						console.log(fileUrl)
	// 						// let fileUrl = plus.io.convertLocalFileSystemURL(res.tempFilePath)
	// 						this.allUrl = this.viewerUrl + '?file=' + fileUrl
	// 						console.log(this.allUrl)
	// 						uni.saveFile({
	// 							tempFilePath: res.tempFilePath,
	// 							success: (res) => {
	// 								console.log(res.savedFilePath)
	// 							}
	// 						})
							
	// 					}
	// 				},
	// 				fail: (err) => {
	// 					console.log(err)
	// 				}
	// 			});
	// 		},
			
			
	// 		getUserMsg(){
	// 						return new Promise((req,rej) =>{
	// 							uni.getStorage({
	// 								key:"userMsg",
	// 								success:(res)=>{
	// 		//							console.log("success")
	// 									this.userMsg = res.data
	// 									req("success")
	// 								},
	// 								fail: (err) => {
	// 									console.log("err")
	// 									uni.reLaunch({
	// 										url:"../Login/Login"
	// 									})
	// 								}
	// 							})
	// 						})
	// 					},
			
			
	// 		getFileInfo(){
	// 			// console.log(this.id)
	// 			// console.log(this.Url + 'Files/OnlinePreview?token=' + this.userMsg.token + "&FileID=" + this.id)
	// 			return new Promise((req,rej)=>{
	// 				uni.request({
	// 					url: this.Url + 'Files/OnlinePreview?token=' + this.userMsg.token + "&FileID=" + this.id,
	// 					success: (res) => {
	// 						console.log(res.data.url)
	// 						req(res.data.url)
	// 					}
	// 				})
	// 			})
	// 		},
	// 	},
 //        async onLoad(options) {
	// 			await this.getUserMsg()
	// 			this.file = await this.getFileInfo()
	// 			console.log(this.file)
	// 			this.loadFile(this.file)
                
 //          }
 //    }
</script>
 
<style>
 
</style>