<template>
	<view>
		
		<u-navbar
		    title="社区广场"
		    @leftClick="rightClick()"
		    >
		</u-navbar>
		
		<view style="margin-top: 80rpx;"></view>
		
		<view v-for='i in count'>
			<view class="communityItem" @click="jump(results[i-1].CommunityID,
			results[i-1].CommunityName,
			results[i-1].Description,
			timeToStr(results[i-1].Renewal),
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
							<text class="renewal">{{timeToStr(results[i-1].Renewal)}}</text>
							<!-- <text class="renewal">{{timeToStr(results[i-1].Renewal)}}</text> -->
						</view>
					</view>
				</view>
			</view>
		</view>
		
		<uni-fab ref="fab" :content="content" @trigger="trigger"/>
		
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
				PostID:'',
				
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
					}
				]
				
			}
		},
		methods: {

			rightClick(){
				uni.navigateTo({
					url:"../index/index"
				})
			},
			

			textFix(text,length){	//社区描述长度限制

				if(text.length <= length){
					return text
				}else{
					return (text.slice(0,length)+'...')
				}
			},
			trigger(e) {	//悬浮按钮点击事件
				// console.log(e)
				this.content[e.index].active = !e.item.active
				uni.showModal({
					title: '提示',
					content:'确认要创建社区吗',
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
			setStorage(id,name,desc,renewal,poster){	//跳转时储存本地数据
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
			jump(id,name,desc,renewal,poster){	//跳转到具体社区
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
			getCommunity(){	//获取当前社区数据
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
							// console.log(this.results.renewal)
							// this.CommunityName = res.data.results
						},
						fail: (err) => {
							req(err)
						}
					})
				})
			},
			timeToStr(time){	//时间转换
				let that = this;
				 // console.log(time)
				if(time == 0){
					return "刚刚"
				}
				if(time >= 3600){
					var hour = Math.floor((time/3600))
					// console.log(hour)
					var min = Math.floor(((time - hour * 3600))/60)
					// console.log(min)
				}else{
					var hour = 0 
					var min = Math.floor(((time - hour * 3600))/60)
				}
				
				if(hour.toString().length < 2)
				{
					hour = "0"+hour
				}
				if(min.toString().length < 2)
				{
					min = "0"+min
				}
				// console.log(hour)
				if(hour==0){
					return min+ "分钟前"
				}else if(hour>=24){
					var day = 0
					day = Math.floor(hour/24)
					return day + "天前"
				}else{
					return hour + "小时前"
				}
			},
		},
		async onLoad() {
			this.useMsg = await this.getToken()	//获取用户数据
			this.data = await this.getCommunity()	//获取当前页面数据

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
			 width: 520rpx;
			 padding: 5rpx;
			 font-size: 18rpx;
			 color: rgba(224, 86, 253,1.0);
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