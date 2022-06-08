<template>
	
	<view>
		<u-navbar
		           title="组织任务"
		           @leftClick="leftClick"
		           :autoBack="true"
		       >
		       </u-navbar>
			   <view class="topBlock"></view>
		<u-notice-bar :text="text1"></u-notice-bar>
		<view class="img">
			<image src="../../static/TaskList-img.png" style="height: 200rpx;margin-top: 20rpx;margin-bottom: 20rpx;"></image>
		</view>
		
		<u-list
					@scrolltolower="scrolltolower"
					:height=200
				>
					<u-list-item
						v-for="(item, index) in indexList"
						:key="index"
					>
						<tm-listitem :value="item.due" :round="24" :shadow="12" :title="item.name" left-icon="../../static/TimeStart.png" show-left-icon left-icon-color="pink" :show-right-icon=false
						@click="seeDetail(item.name)"
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
				 text1: '最新任务',
				 indexList: [{name:"task1",due:"3000"},{name:"task2",due:"4000"},{name:"task3",due:"6000"}],
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
					console.log("loadmore")
					}
					,
					seeDetail(id){
						console.log(id)
						uni.navigateTo({
							url:"./TaskDetail"
						})
					}
			}
		
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
