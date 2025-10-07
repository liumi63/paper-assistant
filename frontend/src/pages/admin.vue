<script setup>
import { computed, onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { loadUser } from '../utils/auth'

const router = useRouter()
const overview = ref(null)
const loading = ref(true)
const errorMessage = ref('')

const fetchOverview = async () => {
  try {
    loading.value = true
    errorMessage.value = ''
    const response = await fetch('/api/admin/overview')
    if (!response.ok) {
      const text = await response.text()
      throw new Error(text || '获取监控数据失败')
    }
    overview.value = await response.json()
  } catch (error) {
    errorMessage.value = error.message || '无法获取后台状态。'
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  const user = loadUser()
  if (!user?.is_admin) {
    router.replace('/dashboard')
    return
  }
  fetchOverview()
})

const summaries = computed(() => {
  if (!overview.value) return []
  return [
    {
      label: '应用名称',
      value: overview.value.app,
      help: '后端 FastAPI 服务名称',
    },
    {
      label: '运行时间',
      value: overview.value.uptime_human,
      help: `${overview.value.uptime_seconds} 秒`,
    },
    {
      label: '注册用户数',
      value: overview.value.users?.total ?? 0,
      help: `其中管理员 ${overview.value.users?.admins ?? 0} 人`,
    },
    {
      label: '数据库连接',
      value: overview.value.database_url,
      help: '当前使用的 DATABASE_URL',
    },
  ]
})
</script>

<template>
  <section class="admin-page">
    <header class="mb-4">
      <h1 class="h3 fw-semibold text-primary">后端监控中心</h1>
      <p class="text-muted mb-0">查看 API 服务状态、数据库连接以及用户数据统计。</p>
    </header>

    <div v-if="loading" class="placeholder-box">正在加载监控数据…</div>
    <div v-else-if="errorMessage" class="alert alert-danger">{{ errorMessage }}</div>
    <div v-else-if="overview" class="d-flex flex-column gap-4">
      <div class="row g-4">
        <div class="col-12 col-md-6 col-xl-3" v-for="summary in summaries" :key="summary.label">
          <div class="card shadow-sm border-0 h-100">
            <div class="card-body">
              <p class="text-muted text-uppercase small mb-1">{{ summary.label }}</p>
              <h4 class="fw-semibold mb-0">{{ summary.value }}</h4>
              <small class="text-muted">{{ summary.help }}</small>
            </div>
          </div>
        </div>
      </div>

      <div class="card shadow-sm border-0">
        <div class="card-body">
          <h5 class="fw-semibold mb-3">运行状态</h5>
          <ul class="list-unstyled mb-0">
            <li
              v-for="item in overview.checks"
              :key="item.title"
              class="d-flex align-items-start gap-3 mb-3"
            >
              <span :class="['status-indicator', `status-${item.status}`]"></span>
              <div>
                <p class="fw-semibold mb-1">{{ item.title }}</p>
                <p class="text-muted small mb-0">{{ item.detail }}</p>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>
 </template>

<style scoped>
.admin-page {
  padding: 1rem 0 3rem;
}

.placeholder-box {
  padding: 2rem;
  background: rgba(13, 71, 161, 0.05);
  border-radius: 1rem;
  color: #0d47a1;
}

.status-indicator {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  margin-top: 7px;
}

.status-ok {
  background: #0f9d58;
}

.status-pending {
  background: #fbbc05;
}

.status-error {
  background: #ea4335;
}
</style>
