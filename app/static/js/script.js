document.addEventListener("DOMContentLoaded", function () {
  // 📌 菜单图标点击事件
  const menuIcon = document.getElementById('menuIcon');
  const navbar = document.getElementById('nav');

  if (menuIcon) {
    menuIcon.addEventListener('click', function () {
      navbar.classList.toggle('open');
    });

    // 📌 点击空白处关闭菜单
    document.addEventListener('click', function (event) {
      if (!navbar.contains(event.target) && navbar.classList.contains('open')) {
        navbar.classList.remove('open');
      }
    });
  }

  // 📌 搜索框交互
  const searchInput = document.querySelector('.search-box input');
  if (searchInput) {
    searchInput.addEventListener('focus', function () {
      this.parentElement.classList.add('focused');
    });
    searchInput.addEventListener('blur', function () {
      this.parentElement.classList.remove('focused');
    });
  }

  // 📌 上传表单：识别中提示
  const form = document.querySelector(".yolo-form form");
  const loading = document.getElementById("loadingMessage");

  if (form && loading) {
    form.addEventListener("submit", function () {
      loading.style.display = "block";  // ✅ 显示“识别中”提示
    });
  }
});
