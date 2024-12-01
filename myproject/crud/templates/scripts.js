// 日付を yyyy-mm-dd の形式でフォーマットする関数
function formatDate(date) {
  return date.toISOString().split('T')[0];
}

// 初期化
const selectedDateElement = document.getElementById('selected-date');
let selectedDate = new Date(); // 現在の日付

// 日付の表示を更新する関数
function updateDisplayedDate() {
  selectedDateElement.textContent = formatDate(selectedDate);
}

// 「前日」ボタンのクリックイベント
document.getElementById('prev-day-btn').addEventListener('click', () => {
  selectedDate.setDate(selectedDate.getDate() - 1); // 1日前に変更
  updateDisplayedDate();
});

// 「翌日」ボタンのクリックイベント
document.getElementById('next-day-btn').addEventListener('click', () => {
  selectedDate.setDate(selectedDate.getDate() + 1); // 1日後に変更
  updateDisplayedDate();
});

// 初期の日付表示
updateDisplayedDate();
