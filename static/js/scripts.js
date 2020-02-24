$(document).ready(function () {
     var form = $('#form_buing_product');
        form.on('submit', function (e) {
        // alert("Hello! I am an alert box!!");
        e.preventDefault();
        var submit_btn = $('#submit_btn');
        var nmb = $('#namber').val();
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("name");
        var product_price = submit_btn.data("price");
        var product_image = submit_btn.data("image");

        var total_price = +product_price*+nmb;

        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
        data.image = product_image;
        var csrf_token = $('#form_buing_product [name="csrfmiddlewaretoken"]').val();

        data["csrfmiddlewaretoken"] = csrf_token;
        // data["Token"] = csrf_token;
        var url = form.attr("action");
        // console.log(data);
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function(data){
                // console.log(data);
                showCart(data);

            }
        });
        $.ajax({
            url: "/orders/basket_top/",
            type: 'POST',
            data: data,
            cache: true,
            success: function(data){
                $('#top_cart_price').text(data.cart_total_price+' '+'$');
                $('#basket_total_nmb').text("("+data.cart_nmb+")");
                console.log("basket_top");
                console.log(data.products_total_nmb);
                console.log(data.cart_total_price);
                console.log(data.cart_nmb);
            }
        });

        $("#form_buing_product").trigger("reset");

        $('#prod').modal();
        function showCart(data) {
            $('.basket-items').html(data);
            $('#prod .modal-body').html(data);
            $('#prod').modal(data);
        }
    });
//    subscribe-footer-email
     var forms = $('#subscribe-footer-email');
     forms.on('submit', function (e) {
//        alert("Hello! I am an alert box!!");
        e.preventDefault();
        var email = $('#email').val();
          console.log(email)
        var csrf_token = $('#subscribe-footer-email [name="csrfmiddlewaretoken"]').val();

        var data = {};
        data.email = email;
        data["csrfmiddlewaretoken"] = csrf_token;

         $.ajax({
            url: '/homepage/subscribe_footer/',
            type: 'POST',
            data: data,
            cache: true,
            success: function(){
                $('#subscribe-footer-email')[0].reset();
//                var info = document.querySelector('.info')
//                info.innerHTML = 'Удачно Отправлено'

                }
        }).done(setTimeout(function() {
                        $(".info").remove();
                                         }, 3000));
//        .done(function() {
//        forms.reset();
//              });
       });
//    subscribe-index-email
     var forms = $('#subscribe-index-email');
     forms.on('submit', function (e) {
//        alert("Hello! I am an alert box!!");
        e.preventDefault();
        var email = $('#email').val();
          console.log(email)
        var csrf_token = $('#subscribe-index-email [name="csrfmiddlewaretoken"]').val();

        var data = {};
        data.email = email;
        data["csrfmiddlewaretoken"] = csrf_token;

         $.ajax({
            url: '/homepage/index/',
            type: 'POST',
            data: data,
            cache: true,
            success: function(){
                $('#subscribe-index-email')[0].reset();
//                var info = document.querySelector('.info')
//                info.innerHTML = 'Удачно Отправлено'

                }
        }).done(setTimeout(function() {
                        $(".info").remove();
                                         }, 3000));
//        .done(function() {
//        forms.reset();
//              });
       });
    //подсчет сум товаров и вывод в итого в корзине и оплате
    function calculatingBasketAmount(){
        var total_order_amount = 0;
        $('.tot').each(function () {

            console.log($(this).text());

            total_order_amount += parseInt($(this).text());
        });
           $('.total_order_amount').text(total_order_amount.toFixed(2));

    };

    // подсчет количества и суммы в корзине и оплате
    $(document).on('change', "#product-in-basket-nmb",function () {
        var current_nmb = $(this).val();
        var current_tr = $(this).closest('tr');
        var current_price = parseInt(current_tr.find('.product-price').text());
        var total_amount = current_nmb * current_price;
        current_tr.find('.tot').text(total_amount.toFixed(2));


        calculatingBasketAmount();
    });

    var filterSubCategory= $('#filterSubCategory');
     console.log(filterSubCategory)
     filterSubCategory.on('submit', function (e) {
        // alert("Hello! I am an alert box!!");
        e.preventDefault();
        var subcategory = [];
        var subcategory = $('.select').val();

     console.log(subcategory)
    // your awesome code calling ajax
});









//    сортировка по цене



     // $(document).on('click', ".order-id",function (e){
     //     e.preventDefault();
     //     var data = {};
     //     var order_id = $(this).data("order_id");
     //     var order_total_price = $(this).data("order_total_price");
     //     console.log(order_total_price);
     //     $('#number-order').text(order_id);
     //     $('#order-total-price').text(order_total_price);
     //     var csrf_token = $('#order-item [name="csrfmiddlewaretoken"]').val();
     //     data["csrfmiddlewaretoken"] = csrf_token;
     //     data.order_id = order_id;
     //     $.ajax({
     //        url: "/order/",
     //        type: 'POST',
     //        data: data,
     //        cache: true,
     //        success: function(data){
     //            console.log("modal");
     //            showOrder(data);
     //
     //        }
     //    });
     //     $('#order').modal();
     // function showOrder(data) {
     //        $('#order .modal-body').html(data);
     //        $('#order').modal(data);
     //    }
     // });
     // вывод в модальное окно описание продукта
     // $(document).on('click', "#product-view",function (e){
     //     e.preventDefault();
     //     var data = {};
     //     var product_id = $(this).data("product_id");
     //     console.log(product_id);
     //     var csrf_token = $('#produc-modal [name="csrfmiddlewaretoken"]').val();
     //     data["csrfmiddlewaretoken"] = csrf_token;
     //     data.product_id = product_id;
     //     $.ajax({
     //        url: "/productview/",
     //        type: 'POST',
     //        data: data,
     //        cache: true,
     //        success: function(data){
     //            console.log("modal");
     //            showProduct(data);
     //
     //        }
     //    });
     //     $('#product_modal').modal();
     // function showProduct(data) {
     //        $('#product_modal .modal-body').html(data);
     //        $('#product_modal').modal(data);
     //    }
     // });
     // вывод в модальное окно wishlist продукта
     // $(document).on('click', "#product-wishlist",function (e){
     //     e.preventDefault();
     //     var data = {};
     //     var product_id = $(this).data("product_id");
     //     var name = $(this).data("name");
     //     console.log(product_id);
     //     var csrf_token = $('#produc-modal [name="csrfmiddlewaretoken"]').val();
     //     data["csrfmiddlewaretoken"] = csrf_token;
     //     data.product_id = product_id;
     //     data.name = name;
     //     $.ajax({
     //        url: "/wishlist/",
     //        type: 'POST',
     //        data: data,
     //        cache: true,
     //        success: function(data){
     //            console.log("modal");
     //            showWishlist(data);
     //
     //        }
     //    });
     //     $('#wishlist').modal();
     // function showWishlist(data) {
     //        $('#wishlist .modal-body').html(data);
     //        $('#wishlist').modal(data);
     //    }
     // });
     // добавлени в корзину из модального окна
     // $(document).on('click', ".add-to-cart-modal",function (e){
     //     e.preventDefault();
     //     var nmb = $('#namber').val();
     //     var data = {};
     //     var product_id = $(this).data("product_id");
     //     var csrf_token = $('#form_buing_product [name="csrfmiddlewaretoken"]').val();
     //     data["csrfmiddlewaretoken"] = csrf_token;
     //     data.product_id = product_id;
     //     data.nmb = nmb;
     //     console.log('modal work');
     //
     //     $.ajax({
     //        url: "/basket_adding/",
     //        type: 'POST',
     //        data: data,
     //        cache: true,
     //        success: function(data){
     //            console.log("modal");
     //            console.log(data);
     //            showCart(data);
     //
     //        }
     //    });
     //     $.ajax({
     //        url: "/basket_top/",
     //        type: 'POST',
     //        data: data,
     //        cache: true,
     //        success: function(data){
     //            $('#top_cart_price').text(data.cart_total_price+' '+'$');
     //            $('#basket_total_nmb').text("("+data.cart_nmb+")");
     //            console.log("basket_top");
     //            console.log(data.products_total_nmb);
     //            console.log(data.cart_total_price);
     //            console.log(data.cart_nmb);
     //        }
     //    });
     //     $('#prod').modal();
     //    function showCart(data) {
     //        $('.basket-items').html(data);
     //        $('#prod .modal-body').html(data);
     //        $('#prod').modal(data);
     //    }
     // });
// $(document).on('change', ".sort",function () {
//       $
//    });
$(".fancybox").fancybox({
        openEffect: "none",
        closeEffect: "none"
    });

     $(".zoom").hover(function(){

		$(this).addClass('transition');
	}, function(){

		$(this).removeClass('transition');
	});
$('.carousel').carousel()
});

