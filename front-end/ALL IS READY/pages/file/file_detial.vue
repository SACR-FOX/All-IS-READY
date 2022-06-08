<template>
	<view>
		<u-navbar
		    title="帖子"
		    @rightClick="rightClick"
		    :autoBack="true">
		</u-navbar>
		<web-view :src="Url" ></web-view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				"Url":"http://all-is-ready-file-storage.oss-cn-hangzhou.aliyuncs.com/userPDF/1/%E7%BC%96%E8%AF%91%E5%8E%9F%E7%90%86/%E7%AC%AC1%E8%AE%B2%20%E7%BB%AA%E8%AE%BA.pdf?OSSAccessKeyId=LTAI5tGWHb9WqaX55jRKoPyv&Expires=1654356557&Signature=bcYPh6gi8ybaUUdyZeawtns3ZBU%3D"
			}
		},
		methods: {
			
		}
	}
</script>

<style>

</style>
