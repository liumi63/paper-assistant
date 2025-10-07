<script setup>
import { ref } from 'vue'

const selectedFile = ref(null)
const fileName = ref('')
const statusMessage = ref('')

const handleFileChange = (event) => {
  const [file] = event.target.files || []
  selectedFile.value = file || null
  fileName.value = file ? file.name : ''
  statusMessage.value = ''
}

const handleUpload = () => {
  if (!selectedFile.value) {
    statusMessage.value = '请先选择要上传的论文文件。'
    return
  }
  // TODO: 接入后端上传接口
  statusMessage.value = `已暂存 ${selectedFile.value.name}，等待接入后端上传功能。`
}
</script>

<template>
  <section class="upload-page">
    <header class="mb-4">
      <h1 class="h3 fw-semibold text-primary">上传文档</h1>
      <p class="text-muted mb-0">
        选择论文 PDF 或其他支持的格式，后续将提供解析、摘要与问答能力。
      </p>
    </header>

    <div class="card border-0 shadow-sm">
      <div class="card-body p-4">
        <div class="mb-3">
          <label class="form-label fw-semibold">选择文件</label>
          <input
            class="form-control"
            type="file"
            accept=".pdf,.doc,.docx,.txt"
            @change="handleFileChange"
          />
          <div v-if="fileName" class="mt-2 text-success">
            当前选择：{{ fileName }}
          </div>
        </div>

        <button class="btn btn-primary" type="button" @click="handleUpload">
          上传文档
        </button>

        <p v-if="statusMessage" class="alert alert-info mt-3 mb-0">
          {{ statusMessage }}
        </p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.upload-page {
  max-width: 640px;
  margin: 0 auto;
  padding: 1rem 0 3rem;
}
</style>
