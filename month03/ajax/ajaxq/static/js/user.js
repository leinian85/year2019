function checkuname(){
    var result = false;
    var xhr = createXhr();
    uname = $('#uname').val();
    url = '/user/xhr_regist?uname='+uname;
    xhr.open('get',url,false);
    xhr.onreadystatechange = function(){
        if (xhr.readyState == 4 && xhr.status == 200){
            var res = xhr.responseText;
            if( res == '0'){
                result = true;
                $('#name_msg').html("OK")
            }else if(res == '1'){
                $('#name_msg').html('用户名已存在');
            }else{
                $('#name_msg').html('无效的用户名');
            }
        }
    }
    xhr.send(null);
    return result;
}

function regist(){
    var xhr = createXhr();
    url = "/user/regist_post"
    xhr.open('post',url,false);
    xhr.onreadystatechange = function(){
        if(xhr.readyState == 4 && xhr.status == 200){
            alert(xhr.responseText);
        }
    }
    xhr.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
    var csrf = $("[name='csrfmiddlewaretoken']").val();
    var uname = $("#uname").val();
    var upwd = $("#upwd").val();
    params = 'uname='+uname+'&upwd='+upwd+'&csrfmiddlewaretoken='+csrf;
    xhr.send(params);
}

function temp(name,pwd){
html = "<div class = 'user_info'>"
html += "<div>"+name+"</div>"
html += "<div>"+pwd+"</div>"
html+= "</div>"
return html;
}


function show(){
    var xhr = createXhr();
    url="/user/show";
    xhr.open('get',url,true);
    xhr.onreadystatechange = function(){
        if (xhr.readyState==4 && xhr.status == 200){
            result = xhr.responseText;
            use_list = result.split("|")
            for(i=0;i<use_list.lenght;i++){
                user = use_list[i].split("_")
                $("#user_info").html(temp(user[0],user[1]))
            }
        }
    }
    xhr.send(null);
}