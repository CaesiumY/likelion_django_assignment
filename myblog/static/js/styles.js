$(document).ready(function () {
    $(window).on('resize', function () {
        if ($(window).width() > 768) {
            $('.main.menu').visibility({
                type: 'fixed'
            });
        }
    }).resize();

    $("input:text").click(function () {
        $(this).parent().find("input:file").click();
    });

    $('input:file', '.ui.action.input').on('change', function (e) {
        var name = e.target.files[0].name;
        $('input:text', $(e.target).parent()).val(name);
    });

    $('.close').on('click', function () {
        $(this).closest('.message').transition('fade');
    });

    $('.ui.dropdown')
        .dropdown();

    $('.right.menu.open').on("click", function (e) {
        e.preventDefault();
        $('.ui.vertical.menu').toggle();
    });
});

console.log('js 내부에서:')
console.log(i_now)