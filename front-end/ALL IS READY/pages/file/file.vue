<template>
	
	<view>
		
		
		<view>
		   <u-navbar
		        title="文件资料管理"
		        @rightClick="rightClick"
		        :autoBack="true"
		    >
				<view
				    class="u-nav-slot"
				    slot="right">
				    <u-icon
				        name="../../static/upload_icon.png"
				        size="24"
				        ></u-icon>
				</view>
		    </u-navbar>
		</view>
		
		<view class="col">
			
			<view class="card_theme">
				<scroll-view scroll-y="true" class="scroll">
					 <view class="folderItem" v-for="(item,index) in folderList"  @click="show(index)">
						 <view class="tag"></view>
						 <text class="theme_text">{{textFix(item.FolderName,5)}}</text>
					 </view>
				</scroll-view>
			</view>
			
			<view class="card_file">
				<scroll-view scroll-y="true">
					<view class="col_right" v-for="(item,index) in fileList"  @click="read(index)">
							<image src="../../static/pdf_icon.png" class="file_img"></image>
							<view class="row">
								<view class="col_right_text">
									<text class="fname_text">{{textFix(item.FileName,9)}}</text>
									<text class="renewal_text">1天前</text>
								</view>
							</view>
					</view>
				</scroll-view>
			</view>
		</view>
	</view>
	
</template>

<script>
	export default {
		data() {
			return {
				//fileType
				file_list: [{
					"FID" : "asaasdas",
					"Fname" : "aaaaaaaa",
					"Uri" : "asdasda",
					"Theme" : "PDF",
					"Renewal" : "1"
					
				},{
					"FID" : "aa",
					"Fname" : "bbbbbbbbbbbb",
					"Uri" : "asdasda",
					"Theme" : "PDF",
					"Renewal" : "2"
					
				},{
					"FID" : "bbb",
					"Fname" : "cccccccccccccc",
					"Uri" : "asdasda",
					"Theme" : "PDF",
					"Renewal" : "3"
					
				},{
					"FID" : "cccc",
					"Fname" : "DDDDDDDDDDDDDD",
					"Uri" : "asdasda",
					"Theme" : "PDF",
					"Renewal" : "4"
					
				},],
				
				fileList : [],
				
				
				folderList : [], 
				folderSelecter : 0,
				
				Url : "http://101.37.175.115/api/",
				
				userMsg : {},
				
				tmp: "http://all-is-ready-file-storage.oss-cn-hangzhou.aliyuncs.com/userPDF/1/%E7%BC%96%E8%AF%91%E5%8E%9F%E7%90%86/%E7%AC%AC1%E8%AE%B2%20%E7%BB%AA%E8%AE%BA.pdf?OSSAccessKeyId=LTAI5tGWHb9WqaX55jRKoPyv&Expires=1654356557&Signature=bcYPh6gi8ybaUUdyZeawtns3ZBU%3D",
			}
		},
		methods: {
			async show(select){
	//			console.log(select)
				this.fileList = await this.getFileList(this.folderList[select].FolderName)
//				console.log(this.fileList[0].FileName)
			},
			
			read(index){
				console.log("打开PDF文件+++++++"+this.fileList[index].ID)
				uni.navigateTo({
					url:"./file_detial?ID="+this.fileList[index].ID,
					fail(err) {
						console.log(err)
					}
				})
			},
			
			showDetial(){
				uni.navigateTo({
					url:'./file_detial'
				})
			},
			
			//修改过长字体
			textFix(text,length){
				if(text.length <= length){
					return text
				}else{
					return (text.slice(0,length)+'...')
				}
			},
			
			getFolerLsit(){
				let that = this
				return new Promise((req,rej)=>{
					uni.request({
						 url:that.Url + 'Files/FolderList?token=' + that.userMsg.token,
						//url:"http://hcl.free.svipss.top/api/Files/Detail/FolderList/?token=" + that.userMsg.token,
						success: (res) => {
							req(res.data.list)
						}
					})
				})
			},
			
			getFileList(folderName){
				let that = this
				// console.log(folderName)
				// console.log("http://hcl.free.svipss.top/Files/Detail/FileList/?token=" + that.userMsg.token)
				return new Promise((req,rej)=>{
					uni.request({
						url:that.Url + "Files/FileList?token=" + that.userMsg.token + "&Folder=" + folderName,
						//url:"http://hcl.free.svipss.top/api/Files/FileList?token=" + that.userMsg.token  + "&Folder=" + folderName,
						method:"GET",
						header:{
							'content-type':'application/x-www-form-urlencoded'
						},	
						// data:{
						// 	Folder : "申请",
						// 	OrgID : -1
						// },
						success: (res) => {
							// console.log(res.data.list)
							req(res.data.list)
						},
						fail: (err) => {
							console.log(err)
						}
					})
				})
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
		},
		async onLoad() {
			await this.getUserMsg()
			this.folderList = await this.getFolerLsit()
			// console.log(this.folderList)
			// this.folderList.forEach((item) =>{
			// 	console.log(item.FolderName)
			// })
			
			this.fileList = await this.getFileList(this.folderList[0].FolderName)
			// console.log(this.fileList)
			// this.fileList.forEach((item)=>{
			// 	console.log(item.FileName)
			// })
			
		}
	}
</script>

<style>
	.card_theme{
		width: 250rpx;
		height: 1400rpx;
		margin: 5px;
		margin-top: 80rpx;
		background-color: rgba(241, 238, 236, 0.8);
		border-radius: 15px;
	}
	.card_file{
		width: 450rpx;
		height: 1400rpx;
		margin-top: 80rpx;
		background-color: rgba(241, 238, 236, 0.8);
		border-radius: 15px;
	}
	.scroll{
		display: ;
	}
	
	
	.folderItem{
		display: flex;
		flex-direction: row;
		background-color: #FFFFFF;
		margin: 15rpx;
		border-radius: 15rpx;
	}
	.tag{
		background-color: #3C9CFF;
		height: 20px;
		width: 20px;
		margin: 8px;
		margin-left: 3px;
		border-radius: 90%;
		border: 3px solid #F1F1F1;	
	}
	.col{
		display: flex;
		flex-direction: row;
	}
	.col_right{
		display: flex;
		flex-direction: row;

		background-color: #ffffff;
		height: 170rpx;
		border-radius: 15rpx;
		align-items: center;
		margin: 20rpx;
	}
	.col_right_text{
		margin-left: 15rpx;
		display: flex;
		align-items: flex-start;
		flex-direction: column;
		justify-content: flex-end;
		height: 80rpx;
		margin-top: 10rpx;
		/* background-color: #398ADE */
	}
	.row{
		display: flex;
		flex-direction: column;
	}
	.theme_text{
		margin: 8px;
		margin-top: 17rpx;
		margin-left: 3rpx;
	}
	.file_img{
		height: 70rpx;
		width: 70rpx;
		margin-left: 20rpx;
	}
	.fname_text{
		font-weight: bolder;
		margin-top: 25rpx;
		font-size: 30rpx;
	}
	.renewal_text{
		font-size: 10rpx;
		color: rgba(131, 131, 131, 1.0);
	}
</style>
