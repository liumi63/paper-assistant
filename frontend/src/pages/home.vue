<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goTo = (path) => {
  router.push(path)
}
</script>

<template>
  <div class="home">
    <section class="hero">
      <h1>📑 Paper Assistant</h1>
      <p>一个帮助你上传论文、提问并生成答案的科研助手。</p>
    </section>

    <section class="actions">
      <button @click="goTo('/upload')" class="btn primary">
        上传文档
      </button>
      <button @click="goTo('/chat')" class="btn secondary">
        开始聊天
      </button>
    </section>
  </div>
</template>

<style scoped>
.home {
  text-align: center;
  margin-top: 60px;
  color: #333;
}

.hero h1 {
  font-size: 2.2rem;
  margin-bottom: 12px;
  color: #42b983;
}

.hero p {
  font-size: 1.2rem;
  color: #666;
}

.actions {
  margin-top: 30px;
  display: flex;
  justify-content: center;
  gap: 16px;
}

.btn {
  border: none;
  border-radius: 6px;
  padding: 10px 20px;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.2s;
}

.btn.primary {
  background-color: #42b983;
  color: white;
}

.btn.primary:hover {
  background-color: #2c8e6d;
}

.btn.secondary {
  background-color: #f0f0f0;
  color: #333;
}

.btn.secondary:hover {
  background-color: #e0e0e0;
}
</style>
