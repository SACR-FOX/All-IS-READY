<template>
	<view class="circle-progress-bar" :style="{
		width: r_size + 'px',
		height: r_size + 'px',
		padding: bw_upx + 'px',
		background: border_color
	}">
		<view class="content" :style="{ background: background }">
			<view class="inner">
				<slot :pro="pro"></slot>
			</view>
		</view>
		<view class="bar" :class="{ animate: animate }" :style="{ transform: `rotate(${start * 360}deg)` }">
			<view class="back n1" v-show="show_back" :style="{ background: border_color, transform: `rotate(${(pro - 0.5) * 360}deg)` }"></view>
			
			<view class="back n1" v-show="show_back" :style="{ background: border_color, 'z-index': 3 }"></view>
			
			<view class="mask n1" :style="{ background: border_back_color, transform: `rotate(${pro * 360}deg)` }"></view>
			<view class="mask n2" :style="{ background: border_back_color }"></view>
			<view class="point s"
			:style="{
				width: bw_upx + 'px',
				height: bw_upx + 'px',
				left: `calc(50% - ${bw_upx / 2}px)`,
				background: border_color,
			}"></view>
			<view class="point e" 
			:style="{
				width: bw_upx + 'px',
				height: bw_upx + 'px',
				left: `calc(50% - ${bw_upx / 2}px)`,
				transform: `rotate(${pro * 360}deg)`,
				'transform-origin': `${bw_upx / 2}px ${size_upx / 2}px`,
				background: border_color,
			}"></view>
		</view>
	</view>
</template>

<script>
	export default {
		name:"circle-progress-bar",
		props:{
			//进度 0-1
			pro: {
				type: Number,
				default: 0,
			},
			//起始位置 0-1
			start: {
				type: Number,
				default: 0,
			},
			//圆形大小
			size: {
				type: Number,
				default: 100
			},
			//线宽度
			border_width: {
				type: Number,
				default: 5
			},
			//线颜色
			border_color: {
				type: String,
				default: '#07C160',
			},
			//线背景色
			border_back_color: {
				type: String,
				default: '#DDD',
			},
			//中心内容背景色
			background: {
				type: String,
				default: '#FFF',
			},
			//是否启用动画
			animate:{
				type: Boolean,
				default: true,
			}
		},
		data() {
			return {
				prev_pro: 0,
			};
		},
		watch:{
			pro(val, pval) {
				this.prev_pro = pval;
			}
		},
		computed:{
			r_size() {
				return this.size_upx -  (2 * this.bw_upx);
			},
			size_upx() {
				return uni.upx2px(this.size)
			},
			bw_upx() {
				return uni.upx2px(this.border_width)
			},
			show_back() {
				return this.pro > 0.5 || (this.pro == 0.5 && this.prev_pro > this.pro)
			}
		}
	}
</script>

<style lang="scss">
	.circle-progress-bar{
		border-radius: 50%;
		overflow: hidden;
		position: relative;
	}
	.content, .bar{
		height: 100%;
		width: 100%;
	}
	.content{
		border-radius: 50%;
		overflow: hidden;
		position: relative;
		z-index: 5;
	}
	.inner{
		position: absolute;
		left: 50%;
		top: 50%;
		transform: translate(-50%, -50%);
	}
	.bar, .mask, .back, .point {
		position: absolute;
	}
	.bar{
		top: 0upx;
		left: 0upx;
	}
	.mask, .back{
		top: 0upx;
		width: 50%;
		height: 100%;
	}
	.n1{
		right: 0upx;
		transform-origin: 0% 50%;
		z-index: 2;
	}
	.n2{
		left: 0upx;
		z-index: 1;
	}
	.point{
		z-index: 3;
		top: 0upx;
		border-radius: 50%;
	}
	.bar.animate {
		&, .mask, .back, .point {
			transition: transform 0.3s;
		}
	}
</style>
