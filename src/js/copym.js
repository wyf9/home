function copym(text, targetId, successMessage, timeout) {
  /*
  text: Text will copy / 要复制的文本(多行)
    使用 `` 包围:
      `aaa
      bbb
      ccc`
  targetId: Id of target div / 复制提示 div 的 id
  successMessage: Text will show after copy / 复制成功的提示
  timeout: Timeout in milliseconds / 等待时间（毫秒）
  */
  var target = document.getElementById(targetId);
  var originalText = target.innerHTML;

  var textarea = document.createElement("textarea");
  textarea.value = text;
  textarea.setAttribute("readonly", "");
  textarea.style.position = "absolute";
  textarea.style.left = "-9999px";
  document.body.appendChild(textarea);
  textarea.select();
  document.execCommand("copy");
  document.body.removeChild(textarea);

  target.innerHTML = successMessage;

  setTimeout(function () {
    target.innerHTML = originalText;
  }, timeout);
}