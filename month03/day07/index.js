var infomation = [{
    name: "张三",
    age: 19
}, {
    name: "李四",
    age: 20
}];

function $$(id) {
    return document.getElementById(id);
}

function showlist() {
    var HTML = '<li>' +
        '<span>姓名</span>' +
        '<span>年龄</span>' +
        '</li>';
    for (i = 0; i < infomation.length; i++) {
        HTML += '<li>';
        HTML += '<span>' + infomation[i].name + '</span>';
        HTML += '<span>' + infomation[i].age + '</span>';
        HTML += '</li>';
    }
    return HTML;
}

$$("info").innerHTML = showlist();

$$("ad").onclick = function () {
    var name = $$("name").value;
    var age = $$("age").value;
    var ad = $$("ad");
    var info = {};
    info.name = name;
    info.age = age;
    infomation.push(info);
    $$("info").innerHTML = showlist();
}