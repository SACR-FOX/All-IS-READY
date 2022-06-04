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
			
			<!-- <view v-if="HasImage">
				<image :src="topicSrc" class="topicSrc"></image>
			</view> -->
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
			            <!-- <u-album :urls="urls2"></u-album> -->
						<u-album :urls="result[i-1].pics"></u-album>
						
			          </view>
					  <view class="row">
						  <image src="../../static/star.png" class="star" @click="star(result[i-1].PostID),showToast()"></image>
						  <view style="margin-top: 7rpx;">{{result[i-1].Stars}}</view>
					  </view>
					  
					  
			        </view>
			      </view>
			    </view>
			  </view>
		</view>
			
		<u-toast ref="uToast" />
		
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
				
				albumWidth: 0,

				pics:[],
				
				
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
			showToast() {
                this.$refs.uToast.show({
                    message: '点赞成功',
                    type: 'success',
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
			getTopicID(){
				return new Promise((req,rej)=>{
					uni.getStorage({
						key: 'TopicID',
						success: function (res) {
							req(res.data)
						},
					})
				})
			},
			getTopic(){
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
			star(PostID){
				console.log(PostID)
				let that = this
				return new Promise((req,rej)=>{
					uni.request({
						url: that.Url + 'Community/Post/' + PostID + '/Star/' + "?token=" + that.useMsg.token,
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
			},
			
		},
		
		async onLoad() {
			this.useMsg = await this.getToken()
			
			this.TopicData = await this.getTopicID()
			// console.log(this.TopicData)
			this.TopicID = this.TopicData.TopicID
			this.Title = this.TopicData.Title
			this.header = this.TopicData.header
			this.Creator = this.TopicData.Creator
			this.Time = this.TopicData.Time
			
			
			
			this.data = await this.getTopic()
			this.count = this.data.count
			this.result = this.data.result
			

			
			// console.log(this.result[0].header)
				
			// console.log(this.TopicID)
			// console.log(this.Title)
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
		background-color: #F1F1F1;
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
	}
	.star{
		height: 50rpx;
		width: 50rpx;
	}
</style>
