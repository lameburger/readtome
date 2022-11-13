function language(lang) {

    $.ajax({ url:"/speak",
    type:"POST",
    contentType: "application/json",
    data: JSON.stringify(lang)})

}