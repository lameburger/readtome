function select (sel) {
    $.ajax({ url:"/read",
    type:"POST",
    contentType: "application/json",
    data: JSON.stringify(sel)})
}