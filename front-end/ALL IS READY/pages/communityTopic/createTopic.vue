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
		
		<u-upload
			:fileList="fileList1"
			@afterRead="afterRead"
			@delete="deletePic"
			name="1"
			multiple
			:maxCount="1"
						style="margin-left: 300rpx;margin-top: 150rpx;"
		></u-upload>
		
		<view class="row">
			<u--input
				v-model="c1"
			    placeholder="请输入话题名字"
			    border="bottom"
			    clearable
				autoHeight
				style="width: 700rpx;"
			  ></u--input>
			  
		</view>
		  
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				fileList1: [],
				c1:'',
				c2:'',
				CommunityID:'',
				tempimage:[],
				
			}
		},
		methods: {
			rightClick(){
				console.log(1)
				let that = this
				return new Promise((resolve, reject) => {
					let a = uni.uploadFile({
						url: 'http://101.37.175.115/api/Community/Topic/Create/?token=' + this.useMsg.token, // 仅为示例，非真实的接口地址
						filePath: this.tempimage,
						name: 'TopicPic',
						formData: {
							CommunityID : this.Community.CommunityID,
							HasImage : "True",
							Title : that.c1,
							TopicPic : this.tempimage
						},
						success: (res) => {
							setTimeout(() => {
								resolve(res.data.data)
							}, 1000)

							uni.navigateTo({
								url:'./communityTopic'
							})
						}
					});
				})
			},
			getToken(){	//获取token
				return new Promise((req,rej)=>{
					uni.getStorage({
						key: 'userMsg',
						success: function (res) {
							req(res.data)
						},
					})
				})
			},
			getCommunityID(){
				return new Promise((req,rej)=>{
					uni.getStorage({
						key:'create',
						success:function(res){
							req(res.data)
							console.log(res.data)
						}
					})
				})
			},
			// 删除图片
			deletePic(event) {
				this[`fileList${event.name}`].splice(event.index, 1)
			},
			//新增图片
			async afterRead(event) {
				let lists = [].concat(event.file)
				lists.map((item) => {
					this[`fileList${event.name}`].push({
						...item,
					})
				})
				// this.tempimage = event.file.url
				this.tempimage = lists[0].url
				// console.log(this.tempimage)
			},
		},
		async onLoad(){
			this.useMsg = await this.getToken()

			this.Community = await this.getCommunityID()
			console.log(this.Community)
		},
	}
</script>

<style>
	.row{
		display: flex;
		flex-direction: row;
		
	}
</style>
