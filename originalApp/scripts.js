// ハンバーガーメニューの開閉を切り替える
function toggleMenu() {
  const sidebar = document.getElementById('sidebar');
  sidebar.classList.toggle('active');
}

// サイドバー以外の領域をクリックしたときにメニューを閉じる処理
window.addEventListener('click', function(event) {
  const sidebar = document.getElementById('sidebar');
  const hamburger = document.querySelector('.hamburger');

  // サイドバーとハンバーガーアイコン以外がクリックされた場合
  if (!sidebar.contains(event.target) && !hamburger.contains(event.target)) {
      if (sidebar.classList.contains('active')) {
          sidebar.classList.remove('active');
      }
  }
});

// カレンダーの表示・非表示を切り替える
function toggleCalendar() {
  const calendar = document.getElementById('calendar');
  if (calendar.style.display === 'none') {
      calendar.style.display = 'block';
  } else {
      calendar.style.display = 'none';
  }
}

// 選択した日付を表示エリアに反映する
function updateDate() {
  const selectedDate = document.getElementById('selected-date');
  const calendar = document.getElementById('calendar');
  selectedDate.value = calendar.value;
}

// ページロード時に本日の日付を初期化
window.onload = function() {
  const today = new Date().toISOString().split('T')[0];
  document.getElementById('selected-date').value = today;
  document.getElementById('calendar').value = today;
};

// メンバー選択モーダルを開く
function openMemberModal() {
  const modal = document.getElementById('memberModal');
  modal.style.display = 'block';
}

// メンバー選択モーダルを閉じる
function closeMemberModal() {
  const modal = document.getElementById('memberModal');
  modal.style.display = 'none';
}

// メンバーの選択結果を反映する（仮の実装）
function submitMembers() {
  const selectedMembers = [];
  const checkboxes = document.querySelectorAll('.member-list input[type="checkbox"]:checked');
  
  checkboxes.forEach((checkbox) => {
      selectedMembers.push(checkbox.value);
  });

  console.log("選択されたメンバー: ", selectedMembers); // 選択されたメンバーをコンソールに表示
  closeMemberModal();
}

// モーダル外をクリックして閉じる処理
window.onclick = function(event) {
  const modal = document.getElementById('memberModal');
  if (event.target == modal) {
      modal.style.display = 'none';
  }
};

// 班指定モーダルを開く
function openTeamModal() {
  const modal = document.getElementById('teamModal');
  modal.style.display = 'block';
}

// 班指定モーダルを開く
function openTeamModal() {
  const modal = document.getElementById('teamModal');
  modal.style.display = 'block';
}

// 班指定モーダルを閉じる
function closeTeamModal() {
  const modal = document.getElementById('teamModal');
  modal.style.display = 'none';
}

// 曖昧検索モーダルを開く
function openSearchModal() {
  const modal = document.getElementById('searchModal');
  modal.style.display = 'block';
}

// 曖昧検索モーダルを閉じる
function closeSearchModal() {
  const modal = document.getElementById('searchModal');
  modal.style.display = 'none';
}

// 検索処理（仮実装）
function search() {
  const query = document.getElementById('search-box').value;
  console.log("検索クエリ: ", query);
  // 実際の検索ロジックをここに追加
}

// 氏名をクリックして詳細情報を表示する
function openInfoPopup(team, name, phone, mail) {
  document.getElementById('popup-team').textContent = team;
  document.getElementById('popup-name').textContent = name;
  document.getElementById('popup-phone').textContent = phone;
  document.getElementById('popup-mail').textContent = mail;
  document.getElementById('infoPopup').style.display = 'block';
}

// 詳細ポップアップを閉じる
function closeInfoPopup() {
  document.getElementById('infoPopup').style.display = 'none';
}

// 選択された申請情報を承認する処理
function approveSelection() {
  const checkboxes = document.querySelectorAll('.select-info:checked');
  if (checkboxes.length > 0) {
      alert("選択された申請情報を承認しました。");
      // 実際の承認処理のロジックをここに追加
  } else {
      alert("承認する申請情報を選択してください。");
  }
}

// 選択された申請情報を取り消す処理
function cancelSelection() {
  const checkboxes = document.querySelectorAll('.select-info:checked');
  if (checkboxes.length > 0) {
      alert("選択された申請情報を取り消しました。");
      // 実際の取り消し処理のロジックをここに追加
  } else {
      alert("取り消す申請情報を選択してください。");
  }
}

// 変更フォームを開く（モーダル）
function openChangeForm(group, name, tel, mail) {
  document.getElementById('changeGroup').value = group;
  document.getElementById('changeName').value = name;
  document.getElementById('changeTel').value = tel;
  document.getElementById('changeMail').value = mail;
  document.getElementById('changeFormModal').style.display = 'block';
}

// 変更フォームを閉じる
function closeChangeForm() {
  document.getElementById('changeFormModal').style.display = 'none';
}

// 新規登録フォームを開く（モーダル）
function openNewForm() {
  document.getElementById('newFormModal').style.display = 'block';
}

// 新規登録フォームを閉じる
function closeNewForm() {
  document.getElementById('newFormModal').style.display = 'none';
}

// 変更を送信
function submitChange() {
  alert("変更を送信しました！");
  closeChangeForm();
}

// ユーザーを削除
function deleteUser() {
  if (confirm("本当に削除しますか？")) {
      alert("ユーザーが削除されました！");
      closeChangeForm();
  }
}

// 新規登録を送信
function submitNew() {
  alert("新規登録が完了しました！");
  closeNewForm();
}