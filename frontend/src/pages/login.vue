<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const form = ref({
  email: '',
  password: '',
  remember: true,
})

const statusMessage = ref('')

const handleSubmit = () => {
  statusMessage.value = '待接入后端登录接口。当前仅展示表单。'
}

const goToRegister = () => {
  router.push('/register')
}
</script>

<template>
  <section class="auth-page">
    <div class="card border-0 shadow-sm auth-card">
      <div class="card-body p-4 p-md-5">
        <header class="mb-4 text-center">
          <h1 class="h3 fw-semibold text-primary mb-1">欢迎回来</h1>
          <p class="text-muted mb-0">登录以继续使用 Paper Assistant</p>
        </header>

        <form @submit.prevent="handleSubmit">
          <div class="mb-3">
            <label class="form-label fw-semibold" for="loginEmail">邮箱</label>
            <input
              id="loginEmail"
              v-model="form.email"
              class="form-control"
              type="email"
              placeholder="name@example.com"
              required
            />
          </div>

          <div class="mb-3">
            <div class="d-flex justify-content-between align-items-center">
              <label class="form-label fw-semibold mb-0" for="loginPassword">密码</label>
              <button class="btn btn-link btn-sm p-0 text-decoration-none" type="button" disabled>
                忘记密码？
              </button>
            </div>
            <input
              id="loginPassword"
              v-model="form.password"
              class="form-control"
              type="password"
              placeholder="请输入密码"
              required
            />
          </div>

          <div class="form-check mb-4">
            <input
              id="loginRemember"
              v-model="form.remember"
              class="form-check-input"
              type="checkbox"
            />
            <label class="form-check-label" for="loginRemember">
              记住我
            </label>
          </div>

          <button class="btn btn-primary w-100" type="submit">
            登录
          </button>
        </form>

        <p v-if="statusMessage" class="alert alert-info mt-3 mb-0">
          {{ statusMessage }}
        </p>

        <p class="text-center text-muted mt-4 mb-0">
          还没有账号？
          <button class="btn btn-link p-0 text-decoration-none" type="button" @click="goToRegister">
            去注册
          </button>
        </p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.auth-page {
  max-width: 520px;
  margin: 0 auto;
  padding: 1rem 0 3rem;
}

.auth-card {
  border-radius: 1.25rem;
}

.btn-link:disabled {
  color: rgba(13, 71, 161, 0.45);
  cursor: not-allowed;
}
</style>
