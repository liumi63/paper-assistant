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
          <div class="d-flex flex-column flex-lg-row align-items-lg-center gap-2 ms-lg-3 mt-3 mt-lg-0">
            <router-link to="/login" class="btn btn-outline-light btn-sm fw-semibold px-3">登录</router-link>
            <router-link to="/register" class="btn btn-light btn-sm fw-semibold cta-btn px-3">注册</router-link>
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
      <div class="container py-4 text-center">
        <div class="d-flex justify-content-center align-items-center gap-2 mb-3">
          <span class="logo">📑</span>
          <span class="fw-semibold fs-5">Paper Assistant</span>
        </div>
        <a
          class="footer-link btn btn-outline-light btn-sm px-3"
          href="https://github.com/liumi63/paper-assistant"
          target="_blank"
          rel="noopener"
        >
          GitHub
        </a>
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
  background: linear-gradient(180deg, #0c2f6f 0%, #0f3b88 100%);
  color:#fff;
}
.footer-link{ color:rgba(215,227,255,.92); text-decoration:none; }
.footer-link:hover{ color:#0c2f6f; background-color:#fff; }

/* 轻阴影的表情 Logo */
.logo{ filter: drop-shadow(0 2px 8px rgba(0,0,0,.25)); }
</style>
