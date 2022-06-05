<template>
	<view>
		
		<u-navbar
		    title="社区广场"
		    @rightClick="rightClick"
		    :autoBack="true">
		</u-navbar>
		
		<view style="margin-top: 80rpx;"></view>
		
		<view v-for='i in count'>
			<view class="communityItem" @click="jump(results[i-1].CommunityID,
			results[i-1].CommunityName,
			results[i-1].Description,
			results[i-1].Renewal,
			results[i-1].Poster)">
				<view class="row">
					<view v-if="HasImage">
						<image :src='results[i-1].Poster' class="image"></image>
					</view>
					<view class="col">
						<view class="row">
							<text class="communityName">{{results[i-1].CommunityName}}</text>
							<text class="postCount">{{results[i-1].PostCount}}</text>
						</view>
						<view class="row">
							<text class="description">{{textFix(results[i-1].Description,30)}}</text>
							<text class="renewal">{{results[i-1].Renewal}}天前</text>
						</view>
					</view>
				</view>
			</view>
		</view>
		
		<uni-fab ref="fab" :content="content" @trigger="trigger" @fabClick="fabClick" />
		
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				Url:'http://101.37.175.115/api/',
				count:{},
				data:{},
				HasImage:true,
				Poster:'../../static/logo.png',
				CommunityName:{},
				CommunityID:{},
				results:{},
				
				Description:{},
				PostCount:'158',
				Renewal:'2天前',
				Renewal:'2天前',
				useMsg : {},
				page:'1',
				
				content: [{
						iconPath: '../../static/shequ.png',
						selectedIconPath: '../../static/shequ.png',
						text: '创建社区',
						active: false
					},
					// {
					// 	iconPath: '../../static/huati.png',
					// 	selectedIconPath: '../../static/huati.png',
					// 	text: '创建话题',
					// 	active: false
					// },
				]
				
			}
		},
		methods: {
			textFix(text,length){
				if(text.length <= length){
					return text
				}else{
					return (text.slice(0,length)+'...')
				}
			},
			trigger(e) {
				// console.log(e)
				this.content[e.index].active = !e.item.active
				uni.showModal({
					title: '提示',
					content: `您${this.content[e.index].active ? '选中了' : '取消了'}${e.item.text}`,
					success: function(res) {
						if (res.confirm) {
							console.log('用户点击确定')
							uni.navigateTo({
								url: 'createCommunity'
							})
						} else if (res.cancel) {
							console.log('用户点击取消')
						}
					}
				})
			},
			setStorage(id,name,desc,renewal,poster){
				// console.log(name)
				uni.setStorage({
					key : 'communityID',
					data : {
						CommunityID:id,
						CommunityName:name,
						Description:desc,
						Renewal:renewal,
						Poster:poster,
					},
				})
			},
			jump(id,name,desc,renewal,poster){
				this.setStorage(id,name,desc,renewal,poster)
				uni.navigateTo({
					url:'../communityTopic/communityTopic',
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
			getCommunity(){
				let that = this
				return new Promise((req,rej)=>{
					uni.request({
						url: that.Url + 'Community/Action' + '?token=' + that.useMsg.token +'&page=' +that.page,
						method:'GET',
						data:{

						},
						success: (res) => {
							req(res.data)
							console.log(that.Url + 'Community/Action' + '?token=' + that.useMsg.token +'&page=' +that.page)
							// console.log(res.data.results[0].CommunityName)
							this.count = res.data.count
							this.results = res.data.results
							// this.CommunityName = res.data.results
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
			// console.log(this.useMsg.token)
			this.data = await this.getCommunity()
			// console.log(this.data.results[0].CommunityName)
		}
	}
</script>

<style lang="scss">
	.row{
		display: flex;
		flex-direction: row;
	}
	.col{
		display: flex;
		flex-direction: column;
	}
	 .communityItem{
		 padding: 10rpx;
		 .image{
			 height: 90rpx;
			 width: 90rpx;
			 border-radius: 180rpx;
		 }
		 .communityName{
			 padding: 5rpx;
		 }
		 .description{
			 width: 560rpx;
			 padding: 5rpx;
			 font-size: 18rpx;
			 color: #95afc0;
		 }
		 .renewal{
			 padding: 5rpx;
			 font-size: 18rpx;
			 color: #95afc0;
		 }
		 .postCount{
			 margin-top: 7rpx;
			 font-size: 12rpx;
			 color: #686de0;
		 }
	 }
</style>