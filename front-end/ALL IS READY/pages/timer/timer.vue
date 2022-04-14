<template>
	<view>
		<view class="top"></view>
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
			<u-list class="history_list">
				<u-list-item v-for="(item,index) in history_list" :style="{backgroundColor : color_list[item.tag]}" class="item"></u-list-item>
			</u-list>
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
					"color" : 2,
				},{
					"name" : "阅读 Passsage 1",
					"date" : "20:00",
					"percent" : "100%",
					"color" : 3,
				}],
				
				"color_list" : ["#caf982","##ec808d","##facd91"]
			}
		},
		methods: {
			
		}
	}
</script>

<style>
	.top{
		background-color: #F1F1F1;
		height: 400px;
	}
	
	.control_bar{
		background-color: #F1F1F1;
		height: 100px;
		display: flex;
		flex-direction: row;
		justify-content: center;
	}
	
	.mention{
		background-color: #5AC725;
		height: 70px;
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: center;
	}
	
	.history{
		background-color: #9ACAFC;
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
		height: 50px;
	}
</style>
