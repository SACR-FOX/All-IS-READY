<template>
	<view>
		
		<view class="background">
			<view style="background-color: rgba(255,255,255,0.7); height: 1625rpx;">
				
				<view class="top">
					<u-avatar 
					src="" class="header"
					size="150rpx">
						
					</u-avatar>
				</view>
				
				<view class="input">
					<view class="input-msg" style="">
						
						<input style="height: 50rpx; margin-left: 30rpx;" 
						placeholder="请输入用户名 " 
						v-model="userName"/>
					</view>
					<view class="input-msg" >
						
						<input style="height: 50rpx; margin-left: 30rpx;" 
						placeholder="请输入密码" 
						password="" v-model="passW"/>
					</view>
					
				</view>
				<button class="login_btn" @click="Login()">Login</button>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				//接口获取token
				Url : "http://101.37.175.115/api/",
				token : "",
				
				backGroundImage : "",

				//用户信息，本地存储
				userMsg : '',

				//系统信息
				sysInfo : "",
				//
				u : 'a',
				userName : "",
				passW : "",
				
				//background
				backGroundImg : {},
			}
		},
		methods: {


			Pa(){
				console.log(this.userName)
			},
			//http://101.37.175.115/api/User/Login
			getUserMsg(){
				let that = this
				return new Promise((req,rej) =>{
					uni.request({
							method:"POST",
							url: that.Url + "User/Login",
							data:{
								"username" : that.userName,
								"password" : that.passW,
							},

							success: (res) => {

								if(res.data.code == 200){
									req(res.data)
								}else{
									req("err")
								}

							},

							fail: (err) => {
								req(404)
							}

						})
				})

			},
			
			getStorage(){
				return new Promise((req,rej) =>{
					uni.getStorage({
						key:"userMsg",
						success:(res)=>{
							console.log("success")
							this.userMsg = res.data
							uni.reLaunch({
								url:"../index/index"
							})
							req("success")
						},
						fail: (err) => {
							req(404)
						}
					})
				})
			},
			
			

			getSystemInfo(){
				return new Promise((req, rej) => {
					uni.getSystemInfo({
						success: function (res) {
							req(res)
						}
					});
				})
			},
			
			getBackGround(){
				let that = this
				return new Promise((req,rej)=>{
					uni.getImageInfo({
						src: "http://101.37.175.115/static/bg/bg9.jpg",
						success: (res) => {
							console.log(res)
							req(res)
						}
					})
				})
			},

			async Login(){
				this.userMsg = await this.getUserMsg()
				if(this.userMsg != "err"){
					this.setStorage(this.userMsg)

					console.log("success")
					uni.reLaunch({
						url:"../index/index"
					})
				}else{
					console.log("err")
				}
			},

			setStorage(userMsg){
				uni.setStorage({
					key : "userMsg",
					data: userMsg
				})
			},

		},
		async onLoad() {
			// let that = this
			// that.token = await that.getToken();
			// console.log(that.token)
			//查看是否已经登录成功
			await this.getStorage()
			this.backGroundImg = await this.getBackGround()
			this.sysInfo = await this.getSystemInfo()
			console.log(this.sysInfo.windowHeight)

		}
	}


</script>

<style>
	
	
	.background{
		background : url("http://101.37.175.115/static/bg/bg9.jpg");
		background-color: rgba(255,255,255,0.5);
		background-size:cover;
		height:1625rpx;
		z-index: -1;
		
		
	}
	
	.top{
		height: 400rpx;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	
	.header{

	}
	
	.input{
		
		display: flex;
		flex-direction: column;
		
		
	}
	.input-msg{
		height: 90rpx;
		margin-top: 100rpx;
		margin: 50rpx;
		border-radius: 35rpx;
		background-color:rgba(255, 255, 255, 0.95);
		display: flex;
		align-items: center;
		outline: #000000;
		outline-width: medium;
		box-shadow: 1px 1px 2px #E5E5E5, 0 0 25px #faf3e9, 0 0 5px #f9ecd4;
		
	}
	
	.login_btn{
		margin: 50rpx;
		border-radius: 35rpx;
	}
</style>
