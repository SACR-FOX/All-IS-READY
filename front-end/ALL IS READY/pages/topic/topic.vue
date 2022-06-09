<template>
	
	<view class="back">
		<u-navbar
		    title="话题帖子"
		    @rightClick="rightClick"
		    :autoBack="true">
		</u-navbar>
		
		<view class="page">
			<text class="title" @click="showToast()">{{Title}}</text>
			<view class="row" style="margin-top: 20rpx; margin-bottom: 20rpx;">
				<u-avatar :src="header" size="30" style="width: 80rpx; margin-top:;"></u-avatar>
				<text class="creator">{{Creator}}</text>
				<view class="time">{{Time}}</view>
			</view>
			<text class="content">
				<!-- {{result[0].Content}} -->
			</text>
			
		</view>
		
		<view v-for="i in count">
			<view class="card">
			    <view class="u-demo-block">
			      <view class="u-demo-block__content">
			        <view class="album">
			          <view class="album__avatar">
			            <!-- <image
			              src='../../static/logo.png'
			              mode=""
			              style="width: 32px;height: 32px;"
			            ></image> -->
						<image
						  :src='result[i-1].header'
						  mode=""
						  style="width: 32px;height: 32px;border-radius: 10rpx;"
						></image>
						
			          </view>
			          <view class="album__content">
			            <u--text
			              :text="result[i-1].Creator"
			              type="primary"
			              bold
			              size="17"
			            ></u--text>
			            <u--text
			              margin="0 0 8px 0"
			              :text="result[i-1].Content"
			            ></u--text>
						<u-album :urls="result[i-1].pics"></u-album>
			          </view>
					  
						<u-icon name="thumb-up" size="20" style="margin-top: 10rpx;" @click="star(result[i-1].PostID,i),showToast1()"></u-icon>
						<!-- <u-icon v-show="a[list1[i-1]]" name="thumb-up-fill" size="20" style="margin-top: 10rpx;" @click="star(result[i-1].PostID,showToast2())"></u-icon> -->
					  <!-- <image :src="a[list1[i-1]]" class="star" @click="star(result[i-1].PostID,showToast2())"></image> -->
					  <!-- <image v-else src="../../static/star.png" class="star" @click="star(result[i-1].PostID,showToast1())"></image> -->
					  <view style="margin-top: 7rpx;">{{result[i-1].Stars}}</view>
			        </view>
			      </view>
			    </view>
			  </view>
		</view>
			
		<u-toast ref="uToast" />
		
		<uni-fab ref="fab" :content="content" @trigger="trigger" />
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				Url:'http://101.37.175.115/api/',
				page:'1',
				TopicID:'10',
				data:{},
				src:'../../static/logo.png',
				topicSrc:'../../static/logo.png',
				HasImage:true,
				Content:'',
				result:{},
				Title:'',
				header:'',
				Creator:'',
				Time:'',
				count:'',
				PostID:'',
				stars:'',
				
				a : ["../../static/star.png",
					"../../static/stared.png"],
				
				albumWidth: 0,

				pics:[],
				
				list1:[],
				
				content: [{
						iconPath: '../../static/shequ.png',
						selectedIconPath: '../../static/shequ.png',
						text: '发帖',
						active: false
					}
				]
			}
		},
		computed: {
			getIcon() {
				return path => {
					return 'https://cdn.uviewui.com/uview/example/' + path + '.png';
				}
			},
		},
		methods:{
			showToast1() {	//点赞成功提示
                this.$refs.uToast.show({
                    message: '点赞成功',
                    type: 'success',
                })
            },
			showToast2() {	//点赞失败提示
			    this.$refs.uToast.show({
			        message: '您已经点过赞了',
			        type: 'success',
			    })
			},
			trigger(e) {	//悬浮按钮点击事件
				// console.log(e)
				this.content[e.index].active = !e.item.active
				uni.showModal({
					title: '提示',
					content:'确认要发帖吗',
					success: function(res) {
						if (res.confirm) {
							console.log('用户点击确定')
							uni.navigateTo({
								url: './createTopicPost'
							})
						} else if (res.cancel) {
							console.log('用户点击取消')
						}
					}
				})
			},
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
			getTopicID(){	//获取当前页面TopicID
				return new Promise((req,rej)=>{
					uni.getStorage({
						key: 'TopicID',
						success: function (res) {
							req(res.data)
						},
					})
				})
			},
			getTopic(){	//获取当前页面数据
				let that = this
				// console.log(that.TopicID)
				return new Promise((req,rej)=>{
					uni.request({
						url: that.Url + 'Community/Post_All' + '?token=' + that.useMsg.token + '&page=' + that.page +'&TopicID=' + this.TopicID,
						method:'GET',
						
						success: (res) => {
							req(res.data)
							console.log(that.Url + 'Community/Post_All' + '?token=' + that.useMsg.token + '&page=' + that.page +'&TopicID=' + this.TopicID)
							this.result = res.data.result
						},
						fail: (err) => {
							req(err)
						}
					})
				})
			},
			getStar(index){	//获取点赞情况
				let that = this
				let id = that.result[index].PostID
				return new Promise((req,rej)=>{
					uni.request({
						url: that.Url + 'Community/checkStar/' + '?token=' + that.useMsg.token,
						method:'POST',
						data:{
							'ID':id,
							'type':1
						},
						success: (res) => {
							
							// console.log(that.Url + 'Community/checkStar/' + '?token=' + that.useMsg.token)
							// this.list1[index] = res.data.result
							if(res.data.result){
								this.list1[index] = 1
							}else
							{
								this.list1[index]=0
							}
							console.log(res.data.result)
							req(res.data)
							// console.log(res.data.result)
						},
						fail: (err) => {
							rej(err)
						},
						
					})
				})
			},
			star(PostID,i){	//点赞事件
				let that = this
				return new Promise((req,rej)=>{
					uni.request({
						url: that.Url + 'Community/Post/' + PostID + '/Star/' + "?token=" + that.useMsg.token,
						method:'POST',
						
						success: (res) => {
							req(res.data)
							console.log(that.Url + 'Community/Post/' + PostID + '/Star/' + "?token=" + that.useMsg.token)
							// console.log(res.data.result[i])
						},
						fail: (err) => {
							req(err)
						},
					})
				})
			},
			setStorage(){	//存储数据
				uni.setStorage({
					key:'TopicID',
					data:{
						TopicID:this.TopicID
					}
				})
			}
		},
		
		async onLoad() {
			
			this.useMsg = await this.getToken()
			
			this.TopicData = await this.getTopicID()
			this.TopicID = this.TopicData.TopicID
			this.Title = this.TopicData.Title
			this.header = this.TopicData.header
			this.Creator = this.TopicData.Creator
			this.Time = this.TopicData.Time

			this.data = await this.getTopic()
			this.count = this.data.count
			this.result = this.data.result
			// console.log(this.result[0].PostID)
			
			
			for (var i = 0; i < this.count;i++){
				this.stars = await this.getStar(i)
				// console.log(this.stars.result)
				 
			}
			// console.log(this.list1)
			// console.log(this.list1[0])
		},
		
	}
</script>

<style lang="scss">
	.u-page {
			padding: 0;
		}
	
		.u-cell-icon {
			width: 36rpx;
			height: 36rpx;
			margin-right: 8rpx;
		}
	
		.u-cell-group__title__text {
			font-weight: bold;
		}
	.back{
		// background-color: #F1F1F1;
	}
	.page{
		padding: 10rpx;
		margin-top: 70rpx;
		background-color: #dcdde1;
	}
	.row{
		display: flex;
		flex-direction: row;
	}
	.title{
		
		font-size: 40rpx;
		font-weight: bold;
		
	}
	.creator{
		display: flex;
		align-items: center;
		width: 450rpx;
	}
	.time{
		display: flex;
		align-items: center;
		color: #95afc0;
	}
	.topicSrc{
		width: 400rpx;
		height: 400rpx;
		display: flex;
		flex-direction: row;
		justify-content: center;
	}
	.content{
		font-size: 30rpx;
	}
	
	.album {
	        @include flex;
	        align-items: flex-start;
	
	        &__avatar {
	             background-color: $u-bg-color;
	             padding: 5px;
	             border-radius: 3px;
	         }
	    
	        &__content {
	             margin-left: 10px;
	             flex: 1;
	         }
	    }
	.card{
		background-color: #F1F1F1;
		margin: 10rpx;
		margin-top: 20rpx;
	}
	.star{
		margin-top: 1rpx;
		height: 50rpx;
		width: 50rpx;
	}
</style>
