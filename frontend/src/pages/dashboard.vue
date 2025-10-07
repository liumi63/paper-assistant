<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { loadUser } from '../utils/auth'

const router = useRouter()
const user = ref(loadUser())

onMounted(() => {
  const latest = loadUser()
  if (!latest) {
    router.replace('/login')
    return
  }
  user.value = latest
})
</script>

<template>
  <section class="dashboard-page">
    <header class="mb-4">
      <h1 class="h3 fw-semibold text-primary">欢迎回来 👋</h1>
      <p class="text-muted mb-0">
        {{ user?.full_name || user?.email }}，这里是你的 Paper Assistant 控制台。
      </p>
    </header>

    <div class="row g-4">
      <div class="col-12 col-lg-6">
        <div class="card border-0 shadow-sm h-100">
          <div class="card-body p-4">
            <h5 class="fw-semibold mb-2">快速开始</h5>
            <p class="text-muted small mb-4">
              上传论文、发起对话或查看最近更新，探索最新功能。
            </p>
            <div class="d-flex flex-column gap-2">
              <router-link class="btn btn-primary" to="/upload">上传新的论文</router-link>
              <router-link class="btn btn-outline-primary" to="/chat">进入智能问答</router-link>
            </div>
          </div>
        </div>
      </div>

      <div class="col-12 col-lg-6">
        <div class="card border-0 shadow-sm h-100">
          <div class="card-body p-4">
            <h5 class="fw-semibold mb-3">接下来计划</h5>
            <ul class="list-unstyled mb-0 text-muted small">
              <li class="d-flex align-items-start gap-2 mb-2">
                <span class="badge bg-primary-subtle text-primary-emphasis">1</span>
                <span>完善文件解析流程并展示摘要。</span>
              </li>
              <li class="d-flex align-items-start gap-2 mb-2">
                <span class="badge bg-primary-subtle text-primary-emphasis">2</span>
                <span>引入引用定位、参考文献管理。</span>
              </li>
              <li class="d-flex align-items-start gap-2">
                <span class="badge bg-primary-subtle text-primary-emphasis">3</span>
                <span>支持多轮对话与回答导出。</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.dashboard-page {
  padding: 1rem 0 3rem;
}

.badge {
  min-width: 28px;
  line-height: 1.2;
}
</style>
