<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goTo = (path) => {
  router.push(path)
}

const features = [
  {
    icon: '📝',
    title: '文档解析',
    description: '自动提取摘要、章节结构与关键词，帮助快速掌握论文重点。',
  },
  {
    icon: '🧠',
    title: '上下文问答',
    description: '围绕已上传的文档精准回答问题，支持引用原文位置与扩展说明。',
  },
  {
    icon: '🚀',
    title: '写作增强',
    description: '提供改写、润色与结构建议，辅助完成科研写作与材料准备。',
  },
]
</script>

<template>
  <section class="home-page">
    <div class="hero card shadow-sm border-0">
      <div class="card-body p-5">
        <span class="badge rounded-pill text-uppercase tracking-wide mb-3 hero-badge">
          Paper Assistant
        </span>
        <h1 class="display-6 fw-semibold mb-3">
          上传论文 · 精准问答 · 辅助写作
        </h1>
        <p class="lead hero-subtitle mb-4">
          统一的平台，为学术研究提供论文解析、重点提炼与智能对话支持。
        </p>
        <div class="d-flex flex-wrap gap-3">
          <button type="button" class="btn btn-primary btn-lg px-4" @click="goTo('/upload')">
            立即上传文档
          </button>
          <button type="button" class="btn btn-outline-light btn-lg px-4 hero-outline" @click="goTo('/chat')">
            体验智能问答
          </button>
        </div>
        <p class="mt-3 mb-0 small hero-auth-link">
          已有账号？
          <button class="btn btn-link p-0 text-decoration-none hero-login-link" type="button" @click="goTo('/login')">
            直接登录
          </button>
        </p>
      </div>
    </div>

    <div class="row g-4 mt-4">
      <div class="col-12 col-lg-4" v-for="feature in features" :key="feature.title">
        <div class="card h-100 border-0 shadow-sm">
          <div class="card-body p-4">
            <div class="feature-icon rounded-circle mb-3">
              {{ feature.icon }}
            </div>
            <h5 class="fw-semibold mb-2">{{ feature.title }}</h5>
            <p class="text-secondary mb-0">
              {{ feature.description }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.home-page {
  max-width: 960px;
  margin: 0 auto;
  padding: 1rem 0 3rem;
}

.hero {
  background: linear-gradient(145deg, #0d47a1 0%, #1976d2 50%, #0aa77d 100%);
  color: #fff;
  position: relative;
  overflow: hidden;
}

.hero::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.18) 0%, rgba(255, 255, 255, 0) 65%);
  pointer-events: none;
}

.hero .card-body {
  position: relative;
  z-index: 1;
}

.hero-badge {
  background: rgba(255, 255, 255, 0.18);
  letter-spacing: 0.18em;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.88);
}

.btn-outline-light {
  border-width: 2px;
}

.hero-outline {
  color: #fff;
  border-color: rgba(255, 255, 255, 0.6);
  background-color: transparent;
}

.hero-outline:hover,
.hero-outline:focus {
  color: #0d47a1;
  background-color: rgba(255, 255, 255, 0.9);
  border-color: rgba(255, 255, 255, 0.9);
}

.hero-subtitle {
  color: rgba(255, 255, 255, 0.8);
}

.hero-auth-link {
  color: rgba(255, 255, 255, 0.82);
}

.hero-login-link {
  color: #fff;
  font-weight: 600;
}

.hero-login-link:hover,
.hero-login-link:focus {
  color: rgba(255, 255, 255, 0.9);
  text-decoration: underline;
}

.feature-icon {
  width: 52px;
  height: 52px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  background: rgba(13, 71, 161, 0.08);
  color: #0d47a1;
}
</style>
