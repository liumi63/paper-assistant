<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const form = ref({
  name: '',
  email: '',
  password: '',
  confirmPassword: '',
})

const statusMessage = ref('')

const handleSubmit = () => {
  if (form.value.password !== form.value.confirmPassword) {
    statusMessage.value = '两次输入的密码不一致，请重新确认。'
    return
  }
  statusMessage.value = '待接入后端注册接口。当前仅展示表单。'
}

const goToLogin = () => {
  router.push('/login')
}
</script>

<template>
  <section class="auth-page">
    <div class="card border-0 shadow-sm auth-card">
      <div class="card-body p-4 p-md-5">
        <header class="mb-4 text-center">
          <h1 class="h3 fw-semibold text-primary mb-1">创建新账号</h1>
          <p class="text-muted mb-0">填写信息以开始使用 Paper Assistant</p>
        </header>

        <form @submit.prevent="handleSubmit">
          <div class="mb-3">
            <label class="form-label fw-semibold" for="registerName">姓名 / 昵称</label>
            <input
              id="registerName"
              v-model="form.name"
              class="form-control"
              type="text"
              placeholder="张三"
              required
            />
          </div>

          <div class="mb-3">
            <label class="form-label fw-semibold" for="registerEmail">邮箱</label>
            <input
              id="registerEmail"
              v-model="form.email"
              class="form-control"
              type="email"
              placeholder="name@example.com"
              required
            />
          </div>

          <div class="row g-3">
            <div class="col-12 col-md-6">
              <label class="form-label fw-semibold" for="registerPassword">密码</label>
              <input
                id="registerPassword"
                v-model="form.password"
                class="form-control"
                type="password"
                placeholder="至少 8 位密码"
                required
                minlength="8"
              />
            </div>
            <div class="col-12 col-md-6">
              <label class="form-label fw-semibold" for="registerConfirmPassword">确认密码</label>
              <input
                id="registerConfirmPassword"
                v-model="form.confirmPassword"
                class="form-control"
                type="password"
                placeholder="再次输入密码"
                required
                minlength="8"
              />
            </div>
          </div>

          <button class="btn btn-primary w-100 mt-4" type="submit">
            注册
          </button>
        </form>

        <p v-if="statusMessage" class="alert alert-info mt-3 mb-0">
          {{ statusMessage }}
        </p>

        <p class="text-center text-muted mt-4 mb-0">
          已有账号？
          <button class="btn btn-link p-0 text-decoration-none" type="button" @click="goToLogin">
            去登录
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
</style>
