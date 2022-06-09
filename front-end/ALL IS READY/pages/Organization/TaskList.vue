<template>
	
	<view>
		<u-navbar
		           title="组织任务"
		           @leftClick="leftClick"
		           
		       >
		       </u-navbar>
			   <view class="topBlock"></view>
		<u-notice-bar :text="text1"></u-notice-bar>
		<view class="img">
			<image src="../../static/TaskList-img.png" style="height: 200rpx;margin-top: 20rpx;margin-bottom: 20rpx;"></image>
		</view>
		
		<u-list
					@scrolltolower="scrolltolower"
					:height=400
				>
					<u-list-item
						v-for="(item, index) in TaskList"
						:key="index"
					>
						<tm-listitem v-if="item.Status" :disabled= false :value="item.TimeDue" :round="24" :shadow="12" :title="item.TaskName" left-icon="../../static/fabu.png" show-left-icon left-icon-color="pink" :show-right-icon=false
						@click="seeDetail(item.TaskID)"
						></tm-listitem>
						<tm-listitem v-if="!item.Status" :disabled= true :value="item.TimeDue" :round="24" :shadow="12" :title="item.TaskName" left-icon="../../static/fabu.png" show-left-icon left-icon-color="pink" :show-right-icon=false
						@click="seeDetail(item.TaskID)"
						></tm-listitem>
					</u-list-item>
				</u-list>
		
	</view>
</template>

<script>
	import tmListitem from '@/tm-vuetify/components/tm-listitem/tm-listitem.vue';
	
	export default {
		components: {tmListitem,},
		data() {
			return {
				prefix:"http://101.37.175.115/api/",
				page:1,
				userInfo:{},
				 text1: '最新任务',
				 TaskList: [],
				 next:false,
				 previous:false,
				 count:0,
			}
		},
		methods: {
			leftClick(){
				uni.navigateTo({
					url:"./Organization"
				})
			},
				scrolltolower() {
							this.loadmore()
						},
				loadmore() {
					var that=this
					console.log("loadmore")
					if (this.$data.next==true){
						this.$data.page=this.$data.page+1
							uni.request({
								url: that.prefix + 'Organization/Task/All' + '?token=' + that.usrInfo.token+'&page='+that.page,
								method:'GET',
								
								success: (res) => {
									that.$data.TaskList=that.$data.TaskList.push.apply(that.$data.TaskList,res.data.data)  
									that.$data.next=res.data.next
									that.$data.previous=res.data.previous
									that.$data.count=res.data.count
									
								},		
								
							})
						}
					}
					,
					seeDetail(id){
						console.log(id)
						uni.navigateTo({
							url:"./TaskDetail?TaskID="+id
						})
					},
					getUserInfo(){
						return new Promise((req,rej)=>{
							uni.getStorage({
								key: 'userMsg',
								success: function (res) {
										req(res.data)
									},
							})
						})
					},
					
					getTaskList(){
						var that=this;
						return new Promise((req,rej)=>{
							uni.request({
								url: that.prefix + 'Organization/Task/All' + '?token=' + that.usrInfo.token+'&page='+that.page,
								method:'GET',
								
								success: (res) => {
									that.$data.TaskList=res.data.data
									that.$data.next=res.data.next
									that.$data.previous=res.data.previous
									that.$data.count=res.data.count
									that.$data.text1="最新任务："+res.data.data[0].TaskName
									
								},		
								
							})
							
						})
					},
					
					},
					async onLoad() {
						this.usrInfo = await this.getUserInfo()
						console.log(this.usrInfo.token)
						await this.getTaskList()
						
					},
			}
				
	
</script>

<style>
	.topBlock{
		height: 80rpx;
	}
	.img{
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.ListItem{
		
	}
</style>
