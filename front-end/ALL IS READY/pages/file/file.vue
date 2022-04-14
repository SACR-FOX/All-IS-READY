<template>
	
	<view>
		<view>
		    <u-navbar
		        title="文件资料管理"
		        @rightClick="rightClick"
		        :autoBack="true"
		    >
				<view
				    class="u-nav-slot"
				    slot="right">
				    <u-icon
				        name="../../static/upload_icon.png"
				        size="24"
				        ></u-icon>
				</view>
		    </u-navbar>
		</view>
		
		<view class="col">
			
			<view class="card_theme" @click="show()">
				<scroll-view scroll-y="true" class="scroll">
					<view class="col">
						<view class="tag"></view>
						<text class="theme_text">编译原理</text>
					</view>
					
					<view class="col">
						<view class="tag"></view>
						<text class="theme_text">数据结构</text>
					</view>
					
					<view class="col" >
						<view class="tag"></view>
						<text class="theme_text">C语言</text>
					</view>
					
					<view class="col">
						<view class="tag"></view>
						<text class="theme_text">Python</text>
					</view>
					
				</scroll-view>
			</view>
			
			<view class="card_file" @click="read()">
				<scroll-view scroll-y="true">
					<view class="col_right">
						<image src="../../static/pdf_icon.png" class="file_img"></image>
						<view class="row">
							<text class="fname_text">操作系统概念(第九版)</text>
							<text class="renewal_text">1天前</text>
						</view>
					</view>
					
					<view class="col_right">
						<image src="../../static/pdf_icon.png" class="file_img"></image>
						<view class="row">
							<text class="fname_text">计算机网络习题解答</text>
							<text class="renewal_text">5天前</text>
						</view>
					</view>
					
					<view class="col_right">
						<image src="../../static/pdf_icon.png" class="file_img"></image>
						<view class="row">
							<text class="fname_text">Qt Creator快速入门</text>
							<text class="renewal_text">7天前</text>
						</view>
					</view>
				</scroll-view>
			</view>
		</view>
		
	</view>
	
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			show(){
				console.log("点击分类名")
			},
			
			read(){
				console.log("打开PDF文件")
			}
		}
	}
</script>

<style>
	.card_theme{
		width: 250rpx;
		height: 1400rpx;
		margin: 5px;
		margin-top: 80rpx;
		background-color: rgba(241, 238, 236, 0.8);
		border-radius: 15px;
	}
	.card_file{
		width: 450rpx;
		height: 1400rpx;
		margin-top: 80rpx;
		background-color: rgba(241, 238, 236, 0.8);
		border-radius: 15px;
	}
	.scroll{
		display: ;
	}
	.tag{
		background-color: #3C9CFF;
		height: 20px;
		width: 20px;
		margin: 8px;
		margin-left: 3px;
		border-radius: 90%;
		border: 3px solid #F1F1F1;	
	}
	.col{
		display: flex;
		flex-direction: row;
	}
	.col_right{
		display: flex;
		flex-direction: row;
		margin-top: 25rpx;
	}
	.row{
		display: flex;
		flex-direction: column;
	}
	.theme_text{
		margin: 8px;
		margin-top: 17rpx;
		margin-left: 3rpx;
	}
	.file_img{
		height: 110rpx;
		width: 110rpx;
	}
	.fname_text{
		font-weight: bolder;
		margin-top: 25rpx;
		font-size: 30rpx;
	}
	.renewal_text{
		font-size: 10rpx;
		color: rgba(224, 86, 253,1.0);
	}
</style>
