// ハンバーガーメニューの開閉を切り替える
function toggleMenu() {
  const sidebar = document.getElementById('sidebar');
  sidebar.classList.toggle('active');
}

// サイドバー以外の領域をクリックしたときにメニューを閉じる処理
window.addEventListener('click', function (event) {
  const sidebar = document.getElementById('sidebar');
  const hamburger = document.querySelector('.hamburger');

  // サイドバーとハンバーガーアイコン以外がクリックされた場合
  if (!sidebar.contains(event.target) && !hamburger.contains(event.target)) {
    if (sidebar.classList.contains('active')) {
      sidebar.classList.remove('active');
    }
  }
});
