$(".oe_signup_form").submit(function (event) {
    var recaptcha = $("#g-recaptcha-response").val();
    if (recaptcha === "") {
        event.preventDefault();
        document.getElementById('err').innerHTML = "Please check Captcha";
        var $btn = $("form").find('.oe_login_buttons > button[type="submit"]');
        $btn.attr('enabled', 'enabled');
    }
    else {
        return true;
    }
});

function verifyRecaptchaCallback() {
    $(".btn").submit.disabled = false;
    $(".btn").submit.value = "Submit";
}

function expiredRecaptchaCallback() {
    document.getElementById('err').innerHTML = "Please re-verify Captcha";
}
