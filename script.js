var burgermenu = false;
function burgerMenu(x) {
    if (burgermenu == false) {
        x.classList.toggle("change");
        $(" .up").addClass("on");
        burgermenu = true;
    }
    else {
        x.classList.toggle("change");
        $(" .up").removeClass("on");
        burgermenu = false;
    }
}
$('.single__slide').slick({
    dots: true,
    customPaging : function(slider, i) {
        var thumb = $(slider.$slides[i]).data();
        return '<a>'+(i+1)+'</a>';
    },
    arrows : false,
    vertical: true,
    verticalSwiping: true
});
$('.double__slide').slick({
    dots: true,
    customPaging : function(slider, i) {
        var thumb = $(slider.$slides[i]).data();
        return (i+1) + "<h4> /5 </h4>";
    },
    arrows : true,
    prevArrow: "<img src='img/left.png' class='next' alt='2'><img src='img/left-active.png' class='next-active' alt='2'>",
    nextArrow: "<img src='img/right.png' class='last' alt='1'><img src='img/right-active.png' class='last-active' alt='2'>",
});
$('.fourth__slide').slick({
    dots: true,
    customPaging : function(slider, i) {
        var thumb = $(slider.$slides[i]).data();
        return ((i+1)*4) + "<h4> /16 </h4>";
    },
    arrows : true,
    prevArrow: "<img src='img/left.png' class='next' alt='2'><img src='img/left-active.png' class='next-active' alt='2'>",
    nextArrow: "<img src='img/right.png' class='last' alt='1'><img src='img/right-active.png' class='last-active' alt='2'>",
});