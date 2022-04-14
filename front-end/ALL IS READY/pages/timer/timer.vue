<template>
	<view>
		<view class="top">
			<circle-progress-bar :pro="pro" 
								  size="500" border_width = "30"
								  border_color = "#faa200" border_back_color="#fae9ca"
								  >
				<view class="timer_center">
					<u--text :text = "history_list[0].name" bold style="margin-left: 70px;"></u--text>
					<u--text :text = "history_list[0].date" style="margin-left: 50px;" bold size = "50"></u--text>
					<u--text :text = "history_list[0].percent" bold style="margin-left: 130px;" size = "20"></u--text>
				</view>
			</circle-progress-bar>
		</view>
		<view class="control_bar">
			<view class="tabbar" style="margin-right: 110px;">
				<u-icon name="pause-circle" color="#55aaff" size="60px"></u-icon>
				<text>暂停</text>
			</view>
			<view class="tabbar">
				<u-icon name="play-circle" color="#55aaff" size="60px"></u-icon>
				<text>开始</text>
			</view>
		</view>
		<view class="mention">
			<u--text :text = "'今天已完成' + learning_time + '小时'" bold size = "25" style="margin-left:110px;"></u--text>
		</view>
		<view class="history">
			<u--text text = "历史定时" size = "18" bold style="margin-left: 20px;"></u--text>
				<scroll-view class="history_list" :scroll-top="scrollTop" scroll-y="true">
					<view v-for="(item,index) in history_list" >
						<view class="item" :style="{backgroundColor : color_list[item.color] }">
							<u--text :text = "item.name" style="margin-left: 20px; width: 150px;" bold size = "20"></u--text>
							<u--text :text = "item.date" bold size = "20" style="margin-left: 20px;"></u--text>
							<u--text :text = "item.percent" bold size = "20"></u--text>
						</view>
					</view>
				</scroll-view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				"learning_time" : 0,
				"history_list" : [{
					"name" : "阅读 Passsage 1",
					"date" : "20:00",
					"percent" : "100%",
					"color" : 0,
				},{
					"name" : "口语 Part 1",
					"date" : "1:20:00",
					"percent" : "0%",
					"color" : 1,
				},{
					"name" : "阅读 Passsage 1",
					"date" : "20:00",
					"percent" : "100%",
					"color" : 2,
				},{
					"name" : "阅读 Passsage 1",
					"date" : "20:00",
					"percent" : "100%",
					"color" : 2,
				},{
					"name" : "阅读 Passsage 1",
					"date" : "20:00",
					"percent" : "100%",
					"color" : 2,
				},{
					"name" : "阅读 Passsage 1",
					"date" : "20:00",
					"percent" : "100%",
					"color" : 2,
				}],
				
				"color_list" : ["#caf982","#ec808d","#facd91"],
				pro : 0.6
			}
		},
		methods: {
			
		}
	}
</script>

<style>
	.history_list{
		height: 250px;
	}
	.timer_center{
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.top{
		background-color: #F1F1F1;
		height: 400px;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	
	.control_bar{
		background-color: #F1F1F1;
		height: 100px;
		display: flex;
		flex-direction: row;
		justify-content: center;
	}
	
	.mention{
		background-color: #F1F1F1;
		height: 70px;
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: center;
	}
	
	.history{
		background-color: #F1F1F1;
		height: 325px;
	}
	.tabbar{
		margin: 20px;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	
	.item{
		height: 70px;
		background-color: #000000;
		margin-top: 10px;
		display: flex;
		flex-direction: row;
	}
</style>
