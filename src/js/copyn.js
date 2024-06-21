function copyn(text, targetId, successMessage, timeout) {
  /*
  text: Text will copy / 要复制的文本
  targetId: Id of target div / 复制提示 div 的 id
  successMessage: Text will show after copy / 复制成功的提示
  timeout: Timeout in milliseconds / 等待时间（毫秒）
  */
  var target = document.getElementById(targetId);
  var originalText = target.innerHTML;

  var input = document.createElement('input');
  input.setAttribute('value', text);
  document.body.appendChild(input);
  input.select();
  document.execCommand('copy');
  document.body.removeChild(input);

  target.innerHTML = successMessage;

  setTimeout(function() {
    target.innerHTML = originalText;
  }, timeout);
}