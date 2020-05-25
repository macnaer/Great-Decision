var caro = document.getElementById('carousel')
var left_btn = document.getElementById('carou_left')
var right_btn = document.getElementById('carou_right')
var text_p = document.querySelectorAll('.text_rew')
var root = document.getElementById('root')
var index = 0
var text_slide = [];

for (var i = 0; i < text_p.length; i ++){
    text_slide[i] = text_p[i];
}

root.innerHTML = text_p[0].innerHTML
root.style.textAlign="center";
root.style.marginTop="25px";

left_btn.addEventListener('click', function(){
    index -- ;
        if(index < 0){
            index = (text_slide.length - 1);
        }
        root.innerHTML = text_p[index].innerHTML;
})
right_btn.addEventListener('click', function(){
    index ++ ;
        if(index == text_slide.length){
            index = 0;
        }
        root.innerHTML = text_p[index].innerHTML;
})