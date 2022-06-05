<template>
	<view>
		<view>
		        <u-navbar
		            title="创建社区"
		            @rightClick="rightClick"
		            :autoBack="true"
					rightText="发布"
		        >
		        </u-navbar>
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
		  
		  <u--textarea v-model="c2" placeholder="请输入社区描述" autoHeight style="height: 300rpx;"></u--textarea>
		  
	</view>
</template>

<script>
	export default {
		data() {
			return {
				fileList1: [],
				c1:'',
				c2:'',
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
			},
			// create(){
			// 	let that = this
			// 	return new Promise((req,rej)=>{
			// 		uni.request({
			// 			url: '',
			// 			method:'POST',
						
			// 			success: (res) => {
			// 				req(res.data)
			// 				console.log(that.Url + 'Community/Post/' + PostID + '/Star/' + "?token=" + that.useMsg.token)
			// 			},
			// 			fail: (err) => {
			// 				req(err)
			// 			}
			// 		})
			// 	})
			// },
			
			// 删除图片
			deletePic(event) {
				this[`fileList${event.name}`].splice(event.index, 1)
			},
			// 新增图片
			async afterRead(event) {
				// 当设置 mutiple 为 true 时, file 为数组格式，否则为对象格式
				let lists = [].concat(event.file)
				let fileListLen = this[`fileList${event.name}`].length
				lists.map((item) => {
					this[`fileList${event.name}`].push({
						...item,
						status: 'uploading',
						message: '上传中'
					})
				})
				// for (let i = 0; i < lists.length; i++) {
				// 	const result = await this.uploadFilePromise(lists[i].url)
				// 	let item = this[`fileList${event.name}`][fileListLen]
				// 	this[`fileList${event.name}`].splice(fileListLen, 1, Object.assign(item, {
				// 		status: 'success',
				// 		message: '',
				// 		url: result
				// 	}))
				// 	fileListLen++
				// }
			},
			uploadFilePromise(url) {
				let that = this
				console.log(url)
				return new Promise((resolve, reject) => {
					let a = uni.uploadFile({
						url: 'http://192.168.2.21:7001/upload', // 仅为示例，非真实的接口地址
						filePath: url,
						name: 'file',
						formData: {
							CommunityName:that.c1,
							AdministratorID:that.useMsg.UID,
							Poster:url,
							Description:that.c2,
						},
						success: (res) => {
							console.log('success')
							setTimeout(() => {
								resolve(res.data.data)
							}, 1000)
						}
					});
				})
			},
			async onLoad() {
				this.useMsg = await this.getToken()
				// console.log(this.useMsg.UID)
			}
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
