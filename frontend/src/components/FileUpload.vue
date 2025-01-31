<template>
  <div>
    <h1>文件上传</h1>
    <input type="file" @change="onFileChange" />
    <button @click="uploadFile">上传</button>
    <p v-if="uploadMessage">{{ uploadMessage }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      file: null,
      uploadMessage: ''
    };
  },
  methods: {
    onFileChange(event) {
      this.file = event.target.files[0];
    },
    async uploadFile() {
      const formData = new FormData();
      formData.append('file', this.file);
      try {
        const response = await axios.post('/api/upload/', formData);
        this.uploadMessage = '文件上传成功！文件名：' + response.data.filename;
      } catch (error) {
        this.uploadMessage = '文件上传失败！';
      }
    }
  }
};
</script> 