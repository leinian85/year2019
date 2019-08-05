// 针对log页面定义一个对象
var log = {
    startdt: "2019-8-5",
    enddt: "2019-9-5",
    updatedt: "2019-8-5",
    anchor: "leinian"
}

// 由对象派生业务逻辑
log.submit = {
    check: function (v) {
        return v == "" ? true : false;
    },
    autohide: function (jq) {
        var t = setTimeout(function () {
            jq.hide();
        }, 2000);
    }
}

// 校验用户名和密码不能为空
function checkvalue() {
    var $username = $("#username");
    var $password = $("#password");

    var $errorname = $(".error:eq(0)");
    var $errorpwd = $(".error:eq(1)");

    if (log.submit.check($username.val())) {
        $errorname.show();
        // 2秒之后自动隐藏
        log.submit.autohide($errorname);
        return false;
    }

    if (log.submit.check($password.val())) {
        $errorpwd.show();
        // 2秒之后自动隐藏
        log.submit.autohide($errorpwd);
        return false;
    }
}

$(function () {
    var $form = $("form");
    var $btn = $(".btn>input");
})