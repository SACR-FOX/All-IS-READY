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
					 <view class="col" v-for="(item,index) in classfily_list">
						 <view class="tag"></view>
						 <text class="theme_text">{{textFix(item.classFName,5)}}</text>
					 </view>
				</scroll-view>
			</view>
			
			<view class="card_file">
				<scroll-view scroll-y="true">
					<view class="col_right" v-for="(item,index) in file_list"  @click="read(index)">
							<image src="../../static/pdf_icon.png" class="file_img"></image>
							<view class="row">
								<view class="col_right_text">
									<text class="fname_text">{{textFix(item.Fname,10)}}</text>
									<text class="renewal_text">{{item.Renewal}}天前</text>
								</view>
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
				//fileType
				file_list: [{
					"FID" : "asaasdas",
					"Fname" : "aaaaaaaa",
					"Uri" : "asdasda",
					"Theme" : "PDF",
					"Renewal" : "1"
					
				},{
					"FID" : "aa",
					"Fname" : "bbbbbbbbbbbb",
					"Uri" : "asdasda",
					"Theme" : "PDF",
					"Renewal" : "2"
					
				},{
					"FID" : "bbb",
					"Fname" : "cccccccccccccc",
					"Uri" : "asdasda",
					"Theme" : "PDF",
					"Renewal" : "3"
					
				},{
					"FID" : "cccc",
					"Fname" : "YHY的产后护理",
					"Uri" : "asdasda",
					"Theme" : "PDF",
					"Renewal" : "4"
					
				},],
				
				classfily_list : [
					{
						"classFName" : "编译原理",
						"classFTag" : 1
					},{
						"classFName" : "BBBBBBBBB",
						"classFTag" : 1
					},{
						"classFName" : "CCCCCCCCCC",
						"classFTag" : 1
					},{
						"classFName" : "DDDDDDDDD",
						"classFTag" : 1
					},{
						"classFName" : "EEEEEEEEEE",
						"classFTag" : 1
					},
				]
			}
		},
		methods: {
			show(){
				console.log("点击分类名")
			},
			
			read(index){
				console.log("打开PDF文件+++++++"+index)
			},
			
			showDetial(){
				uni.navigateTo({
					url:'./file_detial'
				})
			},
			
			//修改过长字体
			textFix(text,length){
				if(text.length <= length){
					return text
				}else{
					return (text.slice(0,length)+'...')
				}
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

		background-color: #ffffff;
		height: 170rpx;
		border-radius: 15rpx;
		align-items: center;
		margin: 20rpx;
	}
	.col_right_text{
		margin-left: 15rpx;
		display: flex;
		align-items: flex-start;
		flex-direction: column;
		justify-content: flex-end;
		height: 80rpx;
		margin-top: 10rpx;
		/* background-color: #398ADE */
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
		height: 70rpx;
		width: 70rpx;
		margin-left: 20rpx;
	}
	.fname_text{
		font-weight: bolder;
		margin-top: 25rpx;
		font-size: 30rpx;
	}
	.renewal_text{
		font-size: 10rpx;
		color: rgba(131, 131, 131, 1.0);
	}
</style>
