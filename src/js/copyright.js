function copyright(divid) {
const targetDiv = document.getElementById(divid);
  const text = targetDiv.innerText;
  const currentYear = new Date().getFullYear();
  // use '(year)' to replace
  const replacedText = text.replace('(year)', currentYear);
  targetDiv.innerText = replacedText;
}