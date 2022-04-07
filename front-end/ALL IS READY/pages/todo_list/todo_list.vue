<template>
	<view class="background" >
		<!-- 上部组件，显示今日和计划列表 -->
		<view class="topbar">
			<view class="top_button">
				<view class="topB_icon">
					<view class="icon_bac" style="background-color: #3C9CFF;">
						<u-icon name="calendar" color="#FFFFFF"size="23"> </u-icon>
					</view>
					<u-text bold="" :text="order" type="info" size="20px" style="margin-bottom: 10px; margin-left: 60px;"></u-text>
				</view>
				<u-text text="今天" size="18px" type="" bold style="margin-left: 15px; margin-bottom: 10px;"></u-text>
			</view>
			<view class="top_button">
				<view class="topB_icon">
					<view class="icon_bac" style="background-color: #F56C6C;">
						<u-icon name="order" color="#FFFFFF"size="23"> </u-icon>
					</view>
					<u-text bold="" :text="order" type="info" size="20px" style="margin-bottom: 10px; margin-left: 60px;"></u-text>
				</view>
				<u-text text="计划" size="18px" type="" bold style="margin-left: 15px; margin-bottom: 10px;"></u-text>
			</view>
		</view>
		<!-- todoList 主体 -->
		<view class="list">
			<view class="center_top">
				<u-text text="My List" style="margin-left: 23px;" bold="" size="17px"></u-text>
				<u-icon name="list" style="margin-right: 20px;" size="25px" bold @click="classify()" ></u-icon>
			</view>
			<view  style="display: flex; flex-direction: column;justify-content: center;">
				<scroll-view style=" height: 615px;"  :scroll-top="scrollTop" scroll-y="true">
					<uni-swipe-action style="margin-left: 0px; height: 615px;">
						<uni-swipe-action-item  class="list_item"
												v-for="(item,index) in list" 
												:right-options="options"
												@click = "delItem(index)">
							<view class="list_item" @click="showDetial(index)">
								<view class="tag"></view>
								<u-text :text="item" size="20px" bold="" type=""></u-text>
							</view>
						</uni-swipe-action-item>
					</uni-swipe-action>
				</scroll-view>
				
			</view>
		</view>
		<!-- 添加按钮 -->
		<view class="buttom" >
<!-- 			<u-button text="添加事项" plain="" shape="circle" 
			style="width: 360px; height: 55px;" size="250px"
			@click="addItem()"
			></u-button> -->
			<button type="default"
			style="width: 360px; height: 55px; align-items: center;" size="200px"
			@click="addItem()" :loading="load" >添加事项</button>
			
		</view>
	</view>
	
	
</template>

<script>
	export default {
		data() {
			return {
				"today" : 0,
				"order" : 0,
				//list数组，后端获得
				"list" : [],
				//左滑菜单
				"options" : [
					{
						text : "删除",
						style : {
							backgroundColor: 'rgba(255,58,49,0.8)'
						}
					}
				],
				
				
				//分类菜单显示控制
				 "show" : false,
				 "classify_list" : ['第一类', '第二类', '第三类'],
				 
				 //分类控制变量
				 // "classify" : -1
				 
				 //控制加载
				 "load" : false 
			}
		},
		methods: {
			
			//删除列表
			delItem(index){
				uni.showModal({
					title: '提示',
					content: '是否删除',
					success: res => {
						if (res.confirm) {
							this.list.splice(index, 1);
						} else if (res.cancel) {	
							console.log('用户点击取消');
						}
					}
				});
			},
			
			
			// //删除事件
			// showModal() {
			// 			this.show = true;
			// 		},
			// confirm(index) {
			// 	setTimeout(() => {
			// 		// 3秒后自动关闭
			// 		//请求接口成功后回调
			// 		this.list.splice(index, 1);
			// 		this.show = false;
			// 	}, 1000)
			// },
			
			showDetial(index){
				let that = this
				uni.navigateTo({
					url:"./list_detial?id=" + that.list[index].toString()
					
				})
			},
			
			addItem(){
				let that = this
				that.load = true
				
				uni.request({
					url:"http://127.0.0.1:8080",
					success(res)  {
						console.log("success")
						that.load = false
						var num = that.list.length
						var item = num+1;
						that.list.splice(0,0,item)
					},
					fail(res) {
						console.log("fail")
						console.log("success")
						that.load = false
						var num = that.list.length
						var item = num+1;
						that.list.splice(0,0,item)
					}
				})
				
			},
			
			classify(){
				let that = this;
				// that.show = true

				uni.showActionSheet({
					itemList: that.classify_list,
						success: function (res) {
							console.log('选中了第' + (res.tapIndex + 1) + '个按钮');
						},
						fail: function (res) {
							console.log(res.errMsg);
						}
				})
				console.log("分类")
			}
		},
		onLoad() {
			let that = this;
			//请求接口获得
			that.list = [1,2,3,4,5,6,7,8,9,0,1,2,3,4]
		}
	}
</script>

<style>
	.background{
		height: 100%;
		width: 100%;
		background-color: #F1F1F1 ;
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.topbar{
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
		margin-top: 40px;
	}
	.top_button{
		height: 80px;
		width: 180px;
		background-color: #FFFFFF;
		margin: 10px;
		border-radius: 10px;
		display: flex;
		flex-direction: column;
	}
	.icon_bac{
		width: 30px;
		height: 30px;
		border-radius: 90%;
		margin: 17px;
		margin-top: 10px;
		align-items: center;
		display: flex;
		justify-content: center;
	}
	.topB_icon{
		display: flex;
		flex-direction: row;
	}
	.list{
		
	}
	.center_top{
		display: flex;
		flex-direction: row;
		align-items: center;
		margin-bottom: 15px;
		justify-content: center;
	}
	.list_item{
		display: flex;
		flex-direction: row;
		align-items: center;
		background-color: #FFFFFF;
		width: 370px;
		height: 60px;
		border-radius: 10px;
		margin-top: 5px;
		margin-bottom: 5px;
	}
	.tag{
		background-color: #3C9CFF;
		height: 26px;
		width: 26px;
		margin: 10px;
		margin-left: 15px;
		border-radius: 90%;
		border: 3px solid #F1F1F1;
	}
	.buttom{
		height: 90px;
		display: flex;
		align-items: center;
		justify-content: center;
		margin-bottom: 10px;
	}
</style>
