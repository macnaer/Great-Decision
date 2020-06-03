//Variable
var main = document.getElementById('main');
var small_slike = document.getElementsByClassName('small-slike');
var slike = document.getElementsByClassName('slike')[0];
var left = document.getElementsByClassName('left')[0];
var right = document.getElementsByClassName('right')[0];

for (var i = 0; i < small_slike.length; i++) {
  small_slike[i].addEventListener('click', run);
}

function run() {
  var displ = this.getAttribute("src");
  main.setAttribute("src", displ);
}

if (left) {
  left.addEventListener("click", lft);
}
if (right) {
  right.addEventListener("click", rght);
}
var pos = 0;

function lft() {
  if (pos != null) {
    if (pos == 0) {
    } else {
      pos += 150;
      slike.style.marginLeft = pos + 'px';
      slike.style.transition = 'all 1s';
    }
  }
}

function rght() {
  if (pos != null) {
    pos -= 150;
    slike.style.marginLeft = pos + 'px';
    slike.style.transition = 'all 1s';
    if (pos == -2400) {
      pos = 150;
    }
  }
}
