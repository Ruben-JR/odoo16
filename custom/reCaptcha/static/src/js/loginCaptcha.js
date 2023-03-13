$("form").submit(function (event) {
  var recaptcha = $("#g-recaptcha-response").val();
  if (recaptcha === "") {
    event.preventDefault();
    document.getElementById('err').innerHTML = "Please verify Captcha";
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
