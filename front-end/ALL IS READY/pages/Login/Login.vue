<template>
	<view>
		<view  class="background">
			<u-input v-model="userName" 
					 clearable placeholder="请输入用户名" 
			         shape = "circle">userName</u-input>
			<u-input v-model="passW" 
			         type = "password" clearable  
			         placeholder="请输入密码" 
			         shape = "circle">passWord</u-input>
			<button class="login_btn" @click="Login()">Login</button>
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
				
				
				//用户信息，本地存储
				userMsg : '',
				
				//系统信息
				sysInfo : "",
				//
				u : 'a',
				userName : "xycf",
				passW : "xycf001",
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
								req(err)
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
			
			async Login(){
				this.userMsg = await this.getUserMsg()
				if(this.userMsg != "err"){
					this.setStorage(this.userMsg)
					// console.log(this.userMsg.token)
					uni.reLaunch({
						url:'../community/community'
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
			this.sysInfo = await this.getSystemInfo()
			console.log(this.sysInfo.windowHeight)
		}
	}
	
	
</script>

<style>
	.background{
		background-color: #ffffff;
		height: 869px;
	}
</style>
