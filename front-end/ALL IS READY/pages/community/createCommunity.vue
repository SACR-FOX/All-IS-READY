<template>
	<view>
		<view>
		      
				<!-- <u-icon name="checkbox-mark" size="19"></u-icon> -->
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
		  
		  <u--textarea v-model="c2" placeholder="请输入社区描述" autoHeight style="height: 150rpx;"></u--textarea>
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				fileList1: [],
				c1:'',
				c2:'',
				result:'',
				imgSrc:'',
				tempimage:'',
			}
		},
		methods: {
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
			rightClick(){
				let that = this
				return new Promise((resolve, reject) => {
					uni.uploadFile({
						url: 'http://101.37.175.115/api/Community/Action/'+'?token='+that.useMsg.token, // 仅为示例，非真实的接口地址
						filePath: this.tempimage,
						name: 'Poster',
						formData: {
							CommunityName:that.c1,
							AdministratorID:that.useMsg.UID,
							Description:that.c2,
						},
						success: (res) => {
							setTimeout(() => {
								resolve(res.data.data)
							}, 1000)
							console.log(res.data)
							uni.navigateTo({
								url:'./community'
							})
						},
						fail: (rej) => {
							console.log('fail')
						}
					});
				})
			},
			
			// 删除图片
			deletePic(event) {
				this[`fileList${event.name}`].splice(event.index, 1)
			},
			// 新增图片
			async afterRead(event) {
				let lists = [].concat(event.file)
				lists.map((item) => {
					this[`fileList${event.name}`].push({
						...item,
					})
				})
				// this.tempimage = event.file.url	//文件路径
				this.tempimage = lists[0].url
				// console.log(lists[0].url)
				// console.log(this.useMsg.UID)
			},
			// uploadFilePromise() {
			// 	let that = this
			// 	return new Promise((resolve, reject) => {
			// 		uni.uploadFile({
			// 			url: 'http://101.37.175.115/api/Community/Action/'+'?token='+that.useMsg.token, // 仅为示例，非真实的接口地址
			// 			filePath: this.tempimage,
			// 			name: 'Poster',
			// 			formData: {
			// 				CommunityName:that.c1,
			// 				AdministratorID:that.useMsg.UID,
			// 				Description:that.c2,
			// 			},
			// 			success: (res) => {
			// 				setTimeout(() => {
			// 					resolve(res.data.data)
			// 				}, 1000)
			// 				console.log(res.data)
			// 				uni.navigateTo({
			// 					url:'./community'
			// 				})
			// 			},
			// 			fail: (rej) => {
			// 				console.log('fail')
			// 			}
			// 		});
			// 	})
			// },
			
			// uploadFilePromise() {
			// 	let that = this
			// 	return new Promise((resolve, reject) => {
			// 		uni.uploadFile({
			// 			url: 'http://hcl.free.svipss.top/api/Community/Action/'+'?token='+that.useMsg.token, // 仅为示例，非真实的接口地址
			// 			filePath: this.tempimage,
			// 			name: 'Poster',
			// 			formData: {
			// 				CommunityName:that.c1,
			// 				AdministratorID:that.useMsg.UID,
			// 				Description:that.c2,
			// 			},
			// 			success: (res) => {
			// 				setTimeout(() => {
			// 					resolve(res.data.data)
			// 				}, 1000)
			// 				console.log(res.data)
			// 			},
			// 			fail: (rej) => {
			// 				console.log('fail')
			// 			}
			// 		});
			// 	})
			// },
		},
			
			async onLoad() {
				this.useMsg = await this.getToken()
				// console.log(this.useMsg.UID)
			}
		}
	
</script>

<style lang="scss">
	.row{
		display: flex;
		flex-direction: row;
		margin-top: 100rpx;
	}
</style>
