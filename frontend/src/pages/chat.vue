<script setup>
import { ref } from 'vue'

const question = ref('')
const messages = ref([
  { role: 'assistant', content: '您好，我是 Paper Assistant，欢迎提问。' },
])

const sendMessage = () => {
  const trimmed = question.value.trim()
  if (!trimmed) return

  messages.value.push({ role: 'user', content: trimmed })
  question.value = ''

  // TODO: 调用后端对话接口获取真实回答
  messages.value.push({
    role: 'assistant',
    content: '这里会显示来自后端的回答。稍后将接入真实模型响应。',
  })
}
</script>

<template>
  <section class="chat-page">
    <header class="mb-4">
      <h1 class="h3 fw-semibold text-primary">智能问答</h1>
      <p class="text-muted mb-0">
        与论文助手对话，待接入后端后将从上传的文档提供上下文回答。
      </p>
    </header>

    <div class="card border-0 shadow-sm chat-card">
      <div class="card-body p-4 d-flex flex-column">
        <div class="flex-grow-1 overflow-auto pe-1">
          <div
            v-for="(msg, index) in messages"
            :key="index"
            class="message"
            :class="msg.role"
          >
            <span class="role-label" v-if="msg.role === 'assistant'">助手</span>
            <span class="role-label" v-else>我</span>
            <p class="mb-0">{{ msg.content }}</p>
          </div>
        </div>

        <form class="mt-3" @submit.prevent="sendMessage">
          <label class="form-label fw-semibold">你的问题</label>
          <textarea
            v-model="question"
            class="form-control"
            rows="3"
            placeholder="请输入要咨询的问题..."
          />
          <div class="d-flex justify-content-end mt-3">
            <button class="btn btn-primary" type="submit">
              发送
            </button>
          </div>
        </form>
      </div>
    </div>
  </section>
</template>

<style scoped>
.chat-page {
  max-width: 720px;
  margin: 0 auto;
  padding: 1rem 0 3rem;
  display: flex;
  flex-direction: column;
}

.chat-card {
  min-height: 480px;
}

.message {
  padding: 0.75rem 1rem;
  border-radius: 0.75rem;
  margin-bottom: 1rem;
  background-color: #f8f9fa;
  line-height: 1.6;
}

.message.assistant {
  background: linear-gradient(135deg, #e3f2fd 0%, #f5f9ff 100%);
  border: 1px solid rgba(13, 71, 161, 0.2);
}

.message.user {
  background: linear-gradient(135deg, #f1f8e9 0%, #f9fff5 100%);
  border: 1px solid rgba(76, 175, 80, 0.2);
}

.role-label {
  display: inline-block;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  color: #6c757d;
  letter-spacing: 0.02em;
  margin-bottom: 0.5rem;
}
</style>
