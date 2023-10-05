const mobile = document.querySelector('.menu-toggle');
const mobilelink =document.querySelector('.sidebar');

mobile.addEventListener("click",function(){
    mobile.classList.toggle("is-active");
    mobilelink.classList.toggle("active");
})

mobilelink.addEventListener("click",function(){
    const menuBars =document.querySelector("is-active");
    if(Window.innerWidth<=768 && menuBars){
        mobilelink.classList.toggle("active")
    }
})


// var step = 100;
// var stepFilter = 60;
// var scrolling =true;

// $(".back").bind("click",function(a){
//     e.preventDefault();
//     $(".highlight-wrapper").animate({
//         scrollLeft:"-=" + step + "px"
//     });
// });

// $(".next").bind("click",function(e){
//     e.preventDefault();
//     $("highlight-wrapper").animate({
//         scrollLeft: "+=" + step + "px"
//     })
// })
