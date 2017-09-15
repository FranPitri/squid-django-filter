$(function(){
    /* Sizing - media q */
    checkSize();
    $(window).resize(checkSize);
    /* items check active route */
    activeItem(window.location.pathname)
});

function checkSize() {
    if (window.matchMedia('(max-width: 576px)').matches) {
        $(".nav").removeClass('flex-column');
    } else {
        $(".nav").addClass('flex-column');
    }
}

function activeItem(location){
    $('.nav-link').each(function (i, e) {
        location.startsWith($(e).data('to')) ? $(e).addClass('active') : $(e).removeClass('active')
    })
}