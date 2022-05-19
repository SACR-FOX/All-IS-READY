<template>
	<view class="container">
		<view style="height: 200px;"></view>
		<canvas :style="{width: canvasW + 'px', height: 460 + 'rpx'}"  canvas-id="firstCanvas" id="firstCanvas" ></canvas>
	</view>
</template>


<script>
	
	export default {
		components: {},
		data() {
			return {
				src : null,
				canvasW:0, // 画布宽
				canvasH:0, // 画布高
				
				leftImg : {}, //做图
				profileImg : {}, //头像
				logoImg : {}, //商大logo
				qrImag : {}, //二维码
				
				leftImgSrc : 'https://s2.loli.net/2022/04/24/e4qk2aD6Hj3RmBT.jpg', //做图
				profileImgSrc : '../../static/avatar.jpg', //头像
				logoImgSrc : 'https://s2.loli.net/2022/04/24/uGFO6zTxnAY39pE.png', //商大logo
				qrImagSrc : 'https://s2.loli.net/2022/04/20/Od26AZyTq9LtNcb.jpg', //二维码
				
				SystemInfo : {}, //设备信息
				
				lineOne : '忆往昔，墨湖畔',
				lineTwo : '湖光柳影  潋滟水波',
				lineThree : '倒映出你最  美的青春年华',
				
				w : 0 //px 转 rpx 转换率
				
			};
		},
		
		async onLoad(){
			let that = this
			
			//获取设备信息
			this.SystemInfo = await this.getSystemInfo();
			
			
			//获取W rpx*w = px
			this.w = this.SystemInfo.windowWidth/750
			console.log(this.w)
			
			let w = that.w
			
			// :style="{'height': canvasW*w},{'weight':canvasH*w}"
			
	
			
			//获取图片缓存
			this.leftImg = await this.ImageInfo(this.leftImgSrc)
			this.logoImg = await this.ImageInfo(this.logoImgSrc)
			// this.profileImg = await this.ImageInfo(this.profileImgSrc)
			this.qrImag = await this.ImageInfo(this.qrImagSrc)
			 
			/*
			...
			*/
		   
		   //获取画布宽高
		    this.canvasW = this.SystemInfo.windowWidth; // 画布宽度
		    this.canvasH = this.leftImg.height //画布高度，依照左图高度
			

			
			console.log(200*w)
		   
		    if(this.leftImg.errMsg == 'getImageInfo:ok'  
			   && this.SystemInfo.errMsg == 'getSystemInfo:ok'
			    ){
			    console.log('ok')
				setTimeout(()=>{
					
					var ctx = uni.createCanvasContext("firstCanvas") //引号里自定义
					
					ctx.weight = 0
					
					ctx.setFillStyle("#f9f9f9")
					ctx.fillRect(0,0,that.canvasW,460*w)
					
					
					//左图设置
					ctx.drawImage(that.leftImg.path,0,0,450*w,460*w)
				
					
					// //渐变
					// const grd = ctx.createLinearGradient(0, 0, 420*w, 0)
					// grd.addColorStop(0,'rgba(255,255,255,0)')
					// grd.addColorStop(1,'rgba(255,255,255,1)')
					// ctx.setFillStyle(grd)
					// ctx.fillRect(0,0,450*w,480*w)
					
					//logo
					ctx.drawImage(that.logoImg.path,450*w,0,(that.canvasW-450*w),90*w)
					//To:
					ctx.setFontSize(18)
					ctx.setFillStyle('#333');
					ctx.fillText('To:',460*w,140*w)
					//from
					ctx.setFontSize(11)
					ctx.setFillStyle('#000000');
					ctx.fillText("From:",460*w,420*w)
					ctx.fillText("浙江工商大学校友会",460*w,450*w)
					//QR
					ctx.drawImage(that.qrImag.path,(that.canvasW - 90*w),(460*w - 90*w),90*w,90*w)
					//邮编
					ctx.setStrokeStyle('#ffffff')
					ctx.strokeRect(20*w,20*w,25*w,25*w)
					ctx.strokeRect(55*w,20*w,25*w,25*w)
					ctx.strokeRect(90*w,20*w,25*w,25*w)
					ctx.strokeRect(125*w,20*w,25*w,25*w)
					ctx.strokeRect(160*w,20*w,25*w,25*w)
					ctx.strokeRect(195*w,20*w,25*w,25*w)

					//头像
					//蒙版
					ctx.save()
					ctx.beginPath()
					ctx.arc(603*w,148*w,38*w,0,2 * Math.PI)
					ctx.clip()
					ctx.drawImage(that.profileImgSrc,565*w,110*w,76*w,76*w)
					ctx.restore()
					
					// ctx.arc(603*w,153*w,91.65/2*w,0,2 * Math.PI )
					// ctx.setFillStyle('#ee000b')
					// ctx.fill()
					
					
					//(730+480)*w/2 - that.lineOne.length*20*w
					//诗
					
					console.log((730+480)*w/2 - that.lineOne.length*20*w)
					
					ctx.setFontSize(19*w)
					ctx.setFillStyle('#3a3a3a');
					console.log(that.lineOne.length)
					//ctx.fillText(that.lineOne,(730+480)*w/2 - ((that.lineOne.length-that.getBlockNum(that.lineOne))+(that.getBlockNum(that.lineOne)/2))/2*19*w,233*w)
					ctx.fillText(that.lineOne,(730+480)*w/2 - ((that.lineOne.length-that.getBlockNum(that.lineOne))+(that.getBlockNum(that.lineOne)/2))/2*19*w,233*w)
					ctx.fillText(that.lineTwo,(730+480)*w/2 - ((that.lineTwo.length-that.getBlockNum(that.lineTwo))+(that.getBlockNum(that.lineTwo)/2))/2*19*w,278*w)
					
					ctx.fillText(that.lineThree,(730+480)*w/2 - ((that.lineThree.length-that.getBlockNum(that.lineThree))+(that.getBlockNum(that.lineThree)/2))/2*19*w,323*w)
					
					//线
					
					ctx.beginPath()

					ctx.moveTo(480*w, 245*w)
					ctx.lineTo(730*w, 245*w)
					ctx.moveTo(480*w, 290*w)
					ctx.lineTo(730*w, 290*w)
					ctx.moveTo(480*w, 335*w)
					ctx.lineTo(730*w, 335*w)
					ctx.setStrokeStyle('#818181')
					ctx.stroke()
				
					
					
					
					ctx.draw(true,(rej) =>{
						uni.canvasToTempFilePath({ // 保存canvas为图片
							canvasId:'firstCanvas',
							quality:1,
							destWidth:that.canvasW/(w*w),
							destHeight: 460/w,
							fileType:'jpg',
							complete: (res) => {
								console.log(res.tempFilePath)
								//调用这个函数保存到相册
								// uni.saveImageToPhotosAlbum({
								// 	filePath:res.tempFilePath,
									
								// 	complete: (res) => {
								// 		console.log("success")
								// 	}
								// })
							}
						})
					})
				},1000)
		    }else{
			    console.log('err')
		    }
		
			
			// ctx.setFillStyle('#f10040');
		
		
			
			
		},
		onReady() {
			
		},
		methods: {
			canvasIdErrorCallback: function (e) {
						console.error(e.detail.errMsg)
			},
			
			//缓存
			// image : 图片地址
			 ImageInfo(image){
				return new Promise((req,rej) =>{
					uni.getImageInfo({
						src: image,
						success: (res) => {
							req(res)
							
						}
					})
				})
			},
			
			// 获取设备信息
			getSystemInfo(){
				return new Promise((req, rej) => {
					uni.getSystemInfo({
						success: function (res) {
							req(res)
						}
					});
				})
			},
			
			getBlockNum(str){
				var strS =  str.match(/ /g)
				if(strS == null ){
					return 0
				}else{
					let kongge = str.match(/ /g).length // 空格 6
					
					return kongge
				}
				
			}
	
		},
		
		
		

	};
	
	
</script>


<style lang="scss">
	
</style>


