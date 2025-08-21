<script setup>
// 根组件仅做全局框架：Header + <router-view/> + Footer
</script>

<template>
  <div class="d-flex flex-column min-vh-100">
    <!-- Header / Navbar -->
    <nav class="navbar navbar-expand-lg app-navbar sticky-top shadow-sm">
      <div class="container">
        <!-- 品牌 -->
        <router-link to="/" class="navbar-brand d-flex align-items-center gap-2 text-white text-decoration-none">
          <span class="logo">📑</span>
          <span class="fw-semibold">Paper Assistant</span>
        </router-link>

        <!-- 折叠按钮（移动端） -->
        <button
          class="navbar-toggler border-0"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#mainNavbar"
          aria-controls="mainNavbar"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <!-- 折叠区域 -->
        <div class="collapse navbar-collapse" id="mainNavbar">
          <ul class="navbar-nav ms-auto align-items-lg-center gap-lg-2">
            <li class="nav-item">
              <router-link to="/" class="nav-link px-3" exact-active-class="active">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/upload" class="nav-link px-3" exact-active-class="active">Upload</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/chat" class="nav-link px-3" exact-active-class="active">Chat</router-link>
            </li>
          </ul>
          <div class="d-flex ms-lg-3 mt-3 mt-lg-0">
            <router-link to="/upload" class="btn btn-light btn-sm fw-semibold cta-btn">开始使用</router-link>
          </div>
        </div>
      </div>
    </nav>

    <!-- 页面内容（由路由切换） -->
    <main class="flex-grow-1 py-4">
      <div class="container">
        <router-view />
      </div>
    </main>

    <!-- Footer -->
    <footer class="app-footer mt-auto">
      <div class="container py-4">
        <div class="row g-4">
          <div class="col-12 col-md-5">
            <div class="d-flex align-items-center gap-2 mb-2">
              <span class="logo">📑</span><span class="fw-semibold">Paper Assistant</span>
            </div>
            <p class="text-white-50 mb-0">
              让学术写作更高效：上传论文、精准问答、引用标注与改写增强。
            </p>
          </div>
          <div class="col-6 col-md-3">
            <h6 class="text-uppercase text-white-50">产品</h6>
            <ul class="list-unstyled small mb-0">
              <li><router-link to="/upload" class="footer-link">文档上传</router-link></li>
              <li><router-link to="/chat" class="footer-link">智能问答</router-link></li>
              <li><a class="footer-link" href="#" aria-disabled="true">写作增强</a></li>
            </ul>
          </div>
          <div class="col-6 col-md-4">
            <h6 class="text-uppercase text-white-50">联系</h6>
            <ul class="list-unstyled small mb-0">
              <li><a class="footer-link" href="#" aria-disabled="true">Privacy</a></li>
              <li><a class="footer-link" href="#" aria-disabled="true">Terms</a></li>
              <li><a class="footer-link" href="#" aria-disabled="true">Support</a></li>
            </ul>
          </div>
        </div>

        <hr class="border-light-subtle my-4" />

        <div class="d-flex flex-column flex-sm-row justify-content-between align-items-center gap-2">
          <small class="text-white-50">© 2025 Paper Assistant</small>
          <div class="d-flex gap-3">
            <a class="footer-link small" href="#" aria-label="Twitter">Twitter</a>
            <a class="footer-link small" href="https://github.com/liumi63/paper-assistant" aria-label="GitHub">GitHub</a>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<style scoped>
/* 顶部导航自定义渐变背景 */
.app-navbar{
  background: linear-gradient(90deg, #0d47a1 0%, #1976d2 35%, #0aa77d 100%);
}
.navbar .navbar-brand, .navbar .nav-link{ color:#fff; }
.navbar .nav-link{ position: relative; opacity:.9; }
.navbar .nav-link:hover{ opacity:1; }
.navbar .nav-link.active{ font-weight:600; }
/* 激活/悬停下划线动画 */
.navbar .nav-link::after{
  content:"";
  position:absolute;
  left:10px; right:10px; bottom:6px; height:2px;
  background: rgba(255,255,255,.85);
  transform: scaleX(0);
  transform-origin: left;
  transition: .25s ease;
}
.navbar .nav-link:hover::after,
.navbar .nav-link.active::after{ transform: scaleX(1); }

/* CTA 圆角胶囊 */
.cta-btn{ border-radius: 999px; }

/* 页脚渐变 + 文本颜色 */
.app-footer{
  background:
    radial-gradient(800px 400px at 15% 0%, rgba(255,255,255,.08), transparent 60%),
    linear-gradient(180deg, #0b2a66 0%, #0f3b88 80%, #0b2a66 100%);
  color:#fff;
}
.footer-link{ color:#d7e3ff; text-decoration:none; }
.footer-link:hover{ color:#fff; text-decoration:underline; }

/* 轻阴影的表情 Logo */
.logo{ filter: drop-shadow(0 2px 8px rgba(0,0,0,.25)); }
</style>
