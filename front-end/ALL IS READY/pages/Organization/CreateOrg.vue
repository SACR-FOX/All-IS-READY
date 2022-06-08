<template>
	<view>
		<u-navbar
		           title="创建组织"
		           @leftClick="leftClick"
		           :autoBack="true"
		       >
		</u-navbar>
			    <view class="topBlock"></view>
				<view style="display: flex;justify-content: center;">
					<view class="bottomLayer">
						<tm-form
								@submit="submit"
								ref="formData"
								@request="success"
								method="post">
									<tm-input name="title" required title="组织名称" v-model="newOrg.OrgName"></tm-input>
								
									<tm-listitem title="组织负责人" left-icon="icon-collection-fill" show-left-icon left-icon-color="red" :show-right-icon=false value="sda"
									
									></tm-listitem>
									<tm-input :vertical="true" :height="120" title="组织简介" :maxlength="100"  :border-bottom="false" :required="false" placeholder="请输入组织介绍"  input-type="textarea" v-model="newOrg.Description" bg-color="grey-lighten-5" clear></tm-input>
								
								</tm-form>
								<view class="submit" style="display: flex; height: 90rpx; margin-top: 80rpx;justify-content: center;">
									<tm-button theme="bg-gradient-red-accent" size="g">创 建</tm-button>
								</view>
									
								

					</view>
				</view>
								
	</view>
</template>

<script>
	import tmForm from '@/tm-vuetify/components/tm-form/tm-form.vue';
	import tmInput from '@/tm-vuetify/components/tm-input/tm-input.vue';
	import tmButton from '@/tm-vuetify/components/tm-button/tm-button.vue';
	import tmListitem from '@/tm-vuetify/components/tm-listitem/tm-listitem.vue';
	
	export default {
		components: {tmForm,tmInput,tmButton,tmListitem},
		data() {
			return {
				newOrg:{
					OrgName:"",
					Description:"",
					Monitor:"",
					},
			}
		},
		methods: {
			leftClick(){
				uni.navigateTo({
					url:"./Organization"
				})
			},
		}
	}
</script>

<style>
	.topBlock{
		height: 300rpx;
	}
	.inputArea{
		display: flex;
		align-items: center;
		justify-content:fl;
	}
	.bottomLayer{
		width: 90%;
		height: 800rpx;
		background-color: #ffffff;
		border-radius: 60rpx 60rpx 60rpx 60rpx;
		padding-top: 60rpx;
	}
page{
		background-color: #f7f1e3;
	}
</style>
