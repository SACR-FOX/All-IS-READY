<template>
	<view class="background" >
		<!-- 弹出组件 -->
		
		<u-popup @close="closePop()" @open="openPop()"
		:show="popupShow" mode="bottom" :round="10" closeable closeOnClickOverlay>
			<view class="popBac">
				<view class="input_item" >
					<u--input clearable placeholder="计划名称" v-model="pickerName">aaa</u--input>
				</view>
				<view class="date_picker" @click="datePickerShow()">
					<!-- <u--input clearable></u--input> -->
					<text v-if="date_flag">{{date_value | timeStamp}}</text>
					<text v-if="!date_flag">请选择时间</text>
					<u-datetime-picker :show="date_picker_show" v-model="date_value"
									   :minDate="time"  @confirm="datePickerConfirm()"
										@cancel="datePickerClose()" :closeOnClickOverlay="true"></u-datetime-picker>
				</view>
				<view class="input_item" @click="tag_picker_show = true">
					<text v-if="picker_tag == 0" >请选择类型</text>
					<text v-else>{{picker_tag}}</text>
					<u-picker :columns="columns"  @cancel = "tag_picker_show = false"
							@confirm="selectClass"
							:show = "tag_picker_show" v-model="picker_tag"></u-picker>
				</view>
			</view>
			<u-button text="确定" @click="addTodo()"></u-button>
		</u-popup>
		
		<!-- 上部组件，显示今日和计划列表 -->
		<view class="topbar">
			<view class="top_button">
				<view class="topB_icon">
					<view class="icon_bac" style="background-color: #3C9CFF;">
						<u-icon name="calendar" color="#FFFFFF" size="23"> </u-icon>
					</view>
					<text class="topBarNum">{{today}}</text>
					<!-- <u-text bold="" :text="order" type="info" size="20px" style="margin-bottom: 10px; margin-left: 60px;"></u-text> -->
				</view>
				<text class="topBarText">今天</text>
				<!-- <u-text text="今天" size="18px" type="" bold style="margin-left: 15px; margin-bottom: 10px;"></u-text> -->
			</view>
			<view class="top_button">
				<view class="topB_icon">
					<view class="icon_bac" style="background-color: #F56C6C;">
						<u-icon name="order" color="#FFFFFF"size="23"> </u-icon>
					</view>
					<!-- <u-text bold="" :text="order" type="info" size="20px" style="margin-bottom: 10px; margin-left: 60px;"></u-text> -->
					<text class="topBarNum">{{order}}</text>
				</view>
				<text class="topBarText">计划</text>
				<!-- <u-text text="计划" size="18px" type="" bold style="margin-left: 15px; margin-bottom: 10px;"></u-text> -->
			</view>
		</view>
		<!-- todoList 主体 -->
		<view class="list">
			<view class="center_top">
				<text style="font-size: 17px;margin-right:200px; font-weight: bold;">My List</text>
				<view style="margin-right: 10rpx; background-color: #ffffff;width: 140rpx;
							  border-radius: 10rpx; display: flex; align-items: center;justify-content: center;"
							 >
							<button  @click="inputByOrg()" style=" font-size: 10rpx;" >批量导入</button>
							 </view>
				<u-icon name="list" style="" size="25px" bold @click="classify()" ></u-icon>
			</view>
			<view  style="display: flex; flex-direction: column;justify-content: center;">
				<scroll-view style=" height: 615px;"  scroll-y="true">
					<uni-swipe-action style="margin-left: 0px; height: 615px;">
						<uni-swipe-action-item  class="list_item"
						
												v-for="(item,index) in tagFilter(list)"
												:right-options="options"
												@click = "delItem(index)"
												v-if = "item.Status">
							<view class="list_item" @click="showDetial(item.ID)">
								<view v-if="item.Tag == '1'" class="tag" style="background-color: #3C9CFF;">
								</view>
								<view v-else-if="item.Tag == '2'" class="tag" style="background-color: #F0AD4E;">
								</view>
								<view v-else class="tag" style="background-color: #DD524D;">
								</view>
								<u-text :text="textFix(item.ItemName,9)" size="20px" bold="" type=""></u-text>
								<view style="background-color: #A9E08F; height: 15px; width: 15px; margin-right: 15px; border-radius: 90%;"></view>
							</view>
						</uni-swipe-action-item>
						<uni-swipe-action-item  class="list_item"
												v-for="(item,index) in tagFilter(list)" 
												:right-options="options"
												@click = "delItem(index)"
												v-if = "!item.Status">
							<view class="list_item" @click="showDetial(item.ID)">
								<view v-if="item.Tag == '1'" class="tag" style="background-color: #3C9CFF;">
								</view>
								<view v-else-if="item.Tag == '2'" class="tag" style="background-color: #F0AD4E;">
								</view>
								<view v-else class="tag" style="background-color: #DD524D;">
								</view>
								<u-text :text="textFix(item.ItemName,9)" size="20px" bold="" type=""></u-text>
								<view v-if="!item.Status" style="background-color: #F56C6C; height: 15px; width: 15px; margin-right: 15px; border-radius: 90%;"></view>
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
			@click="showPopup()" :loading="load" >添加事项</button>
			
		</view>
	</view>
	
	
</template>

<script>
	export default {
		data() {
			return {
				"today" : 10,
				"order" : 1,
				//list数组，后端获得
				"list" : [],
				"list_classify" : [],
				//左滑菜单
				"options" : [
					{
						text : "完成",
						style : {
							backgroundColor: 'rgba(255, 170, 0, 0.8)'
						}
					}
				],
				
				
				//分类菜单显示控制
				 "show" : false,
				 "classify_list" : ['第一类', '第二类', '第三类',"未完成","已完成","取消分类"],
				 
				 //分类控制变量
				 "tag" : -1,
				 
				 //控制加载
				 "load" : false ,

				 //弹出组件控制
				 "popupShow" : false,
				
				
				pickerName : "",
				//date选择控制
				"date_picker_show" : false,
				"time" : 1649389163,
				 "date_value" : Number(new Date()),
				 "date_flag" : false, //是否选择时间 
				 
				 //tag选择器控制
				"tag_picker_show" : false,
				"columns": [['第一类', '第二类', '第三类']],
				"C_tag" : "null",
				"picker_tag" : 0,
				
				//用户信息
				userMsg : [],
				Url : "http://101.37.175.115/api/",
			}
		},
		methods: {
			
			//显示时间选择器
			datePickerShow(){
				// this.getTimeNow()
				this.date_picker_show = true
				
			},
			//关闭时间选择器
			datePickerClose(){
				this.date_picker_show = false
				
			},
			//点击确定按钮获取时间
			datePickerConfirm(){
				this.date_flag = true
				this.date_picker_show = false;
				
			},
			//获取当前时间
			getTimeNow(){
				var value = this.date_value
				var date = new Date(parseInt(value)); //时间戳为10位需*1000，时间戳为13位的话不需乘1000
				this.yearN = date.getFullYear();
				this.monN = ("0" + (date.getMonth() + 1)).slice(-2);
				this.dayN = ("0" + date.getDate()).slice(-2);
				this.hourN = ("0" + date.getHours()).slice(-2);
				this.minN = ("0" + date.getMinutes()).slice(-2);
			},
			
			//批量导入
			inputByOrg(){
				uni.request({
					url: this.Url + "ToDoList/GroupImport?token=" + this.userMsg.token,
					method:"POST",
					data:{
						OrgID : this.userMsg.OrgID
					},
					success: (res) => {
						console.log(res.data)
						this.getList()
					}
				})
			},
			
			//删除列表
			//-->完成
			delItem(index){
				uni.showModal({
					title: '提示',
					content: '是否已经完成此事项',
					success: res => {
						if (res.confirm) {
							// this.list.splice(index, 1);
							uni.request({
								url:this.Url + "ToDoList/Action/"+ this.list[index].ID + "/Done/?token=" + this.userMsg.token,
								method: "PUT",
								// http://101.37.175.115/api/ToDoList/Action/<ID>/Done/
								success: (res) => {
									this.list[index].Status = true
									console.log(res.data)
								},
								fail: (err) => {
									console.log("err")
								}
							})
						} else if (res.cancel) {	
							console.log('用户点击取消');
						}
					}
				});
			},
			
			//获取UUID
			getUUID() {
				return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
					var r = Math.random() * 16 | 0,
						v = c == 'x' ? r : (r & 0x3 | 0x8);
					return v.toString(16);
					});
			},
			
			
			
			//点击跳转
			showDetial(UID){
				let that = this
				uni.navigateTo({
					url:"./list_detial?id=" + UID.toString()
				})
			},
			
			
			//显示添加界面
			showPopup(){
				this.date_flag = false
				let that = this
				that.load = true
				that.popupShow = true
			},
			//关闭添加界面
			closePop() {
					this.popupShow = false
					this.load = false
			    // console.log('close');
			},
			
			//
			selectClass(e){
				this.tag_picker_show = false
				this.date_flag = 1
				this.picker_tag = e["value"]["0"]
					
				if(this.picker_tag == "第一类"){
					this.picker_tag = 1
				}else if(this.picker_tag == "第二类"){
					this.picker_tag = 2
				}else if(this.picker_tag == "第三类"){
					this.picker_tag = 3
				}
				console.log(this.picker_tag)
			},
			
			//添加事项
			addTodo(){
				let that =this
				if(!this.date_flag){
					console.log("err")
					return false
				}else if(this.picker_tag == 0){
					console.log("err")
					return false
				}else if(this.pickerName == ""){
					console.log("err")
					return false
				}
				
				uni.request({
					method:"POST",
					url:this.Url + "ToDoList/Action/?token="+this.userMsg.token,
					data:{
							"OrgID": -1,
						    "UID": this.userMsg.UID,
						    "ItemName": this.pickerName,
						    "UUID": 7,
						    "Tag": this.picker_tag,
						    "Time": Math.floor(this.date_value/1000)
					},
					success: (res) => {
						let item = {
							"OrgID": -1,
							"UID": this.userMsg.UID,
							"ItemName": this.pickerName,
							"UUID": 7,
							"Tag": this.picker_tag,
							"Time": Math.floor(this.date_value/1000)
						}
						that.date_value = Number(new Date())
						that.picker_tag = 0
						that.pickerName = ""
						// console.log("/" + this.date_value/1000)
						console.log(res.data)
						that.list.splice(0,0,item)
						that.list_classify = that.list
						that.load = false
						that.popupShow = false
					}
				})
			},
			
			
			//点击确定按钮后
			//调用接口
			addItem(){
				let that = this
				// uni.request({
				// 	url:"http://127.0.0.1:8080",
				// 	success(res)  {
				// 		console.log("success")
				// 		that.load = false
				// 		var num = that.list.length
				// 		var item = num+1;
				// 		that.list.splice(0,0,item)
				// 	},
				// 	fail(res) {
				// 		console.log("fail")
				// 		console.log("success")
				// 		that.load = false
				// 		var num = that.list.length
				// 		var item = num+1;
				// 		that.list.splice(0,0,item)
				// 	}
				// })
				
				let tag = Math.ceil(Math.random()*3);
				let item = {"ID":Math.ceil(Math.random()*100),"ItemName": "DEMO","OrgId":1,"Status":true,"time":"2022.1.1","tag" : tag}
				that.list.splice(0,0,item)
				that.list_classify = that.list
				that.load = false
			},

			
			//点击分类按钮
			classify(){
				let that = this;
				// that.show = true

				uni.showActionSheet({
					itemList: that.classify_list,
						success: function (res) {
							that.tag = res.tapIndex+1
						},
						fail: function (res) {
							console.log(res.errMsg);
						}
				})
				// console.log("分类")
			},
			
			tagFilter(list) {
				let that = this
				var result = []
				if( that.tag <= 3 && that.tag > 0){
					 result = list.filter(item =>{
						 if(that.tag ==3 ){
							 return item.Tag >= 3
						 }else{
							 return item.Tag == that.tag
						 }
						
					})
				}else if( that.tag == 4){
					result = list.filter(item =>{
						return !item.Status
						
					})
				}else if( that.tag == 5){
					result = list.filter(item =>{
						return item.Status
					})
				}else{
					result = list
				}
				
				return result;
			},
			getUserMsg(){
				return new Promise((req,rej) =>{
					uni.getStorage({
						key:"userMsg",
						success:(res)=>{
							console.log("success")
							this.userMsg = res.data
							req("success")
						},
						fail: (err) => {
							console.log("err")
							uni.reLaunch({
								url:"../Login/Login"
							})
						}
					})
				})
			},
			
			getList(){
				let that = this
				return new Promise((req,rej)=>{
					uni.request({
						url:that.Url + "ToDoList/All?token=" + that.userMsg.token,
						success: (res) => {
							console.log(res.data.length)
							req(res.data)
						}
					})
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

		},
	
		
		async onLoad() {
			let that = this;
			
			await that.getUserMsg()
			that.list = await that.getList()
			console.log(that.userMsg.OrgID)
			// for(var i = 1;i <= 10 ; i++){
			// 	let tag = Math.ceil(Math.random()*3);
			// 	// "ID": 2,
			// 	// "ItemName": "偷懒",
			// 	// "OrgID": -1,
			// 	// "Status": false,
			// 	// "Tag": 6,
			// 	// "Time": 1649424695
			// 	let item = {"ID":i,"ItemName": "DEMO","OrgID":1,"Status":false,"Time": 1649424695,"tag" : 2}
			// 	that.list.splice(0,0,item)
			// }
			
			
			that.list_classify = that.list
			// let item = {"ID":i,"itemName": "DEMO1","OrgId":1,"Status":true,"time":"2022.1.1","tag" : tag,"UUID" : ""}
			// that.list.splice(0,0,item)
			//请求接口获得
			
			//时间戳获取
			var timestamp=Math.ceil((new Date().getTime()))
			that.time = timestamp
			// console.log(timestamp)
			
			// console.log("UUID")
			// console.log(this.uuidv4())
			

			
		},
		filters:{
			timeStamp: function(value) {
				var date = new Date(value); //时间戳为10位需*1000，时间戳为13位的话不需乘1000
				var year = date.getFullYear();
				var month = ("0" + (date.getMonth() + 1)).slice(-2);
				var sdate = ("0" + date.getDate()).slice(-2);
				var hour = ("0" + date.getHours()).slice(-2);
				var minute = ("0" + date.getMinutes()).slice(-2);
				// var second = ("0" + date.getSeconds()).slice(-2);
				// 拼接
				var result = year + "-" + month + "-" + sdate + " " + hour + ":" + minute ;
				// 返回
				return result;
			},
			
		}
	}
</script>

<style>
	.topBarNum{
		font-size: 20px;
		font-weight: bold;
		color: #BBBCBE;
		margin-left: 80px;
		margin-top: 10px;
	}
	.topBarText{
		font-size: 18px;
		font-weight: bold;
		margin-left: 13px;
		margin-bottom: 7px;
	}
		
	.input_item{
		height: 50px;
		width: 350px;
		margin-top: 20px;
		/* margin-bottom: 20px; */
	}
	.date_picker{
		display: flex;
		flex-direction: row;
		height: 50px;
		width: 350px;
		margin-top: 20px;
		align-items: center;
		justify-content: center;
	}
	
	.popBac{
		display: flex;
		flex-direction: column;
		height: 300px;
		align-items: center;
		justify-content: center;
	}
	.input{
		width: 150px;
		
	}
	
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
