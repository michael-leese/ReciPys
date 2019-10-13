$(document).ready(function(){

    //add recipy form
    $(".add-form-input > input").addClass("textarea-form");
    $("p > textarea").addClass("textarea-form");
    $("p > label").addClass("strong");
    $("#creator").attr("placeholder", "Your Username...");
    $("#title").attr("placeholder", "ReciPy Title...");
    $("#description").attr("placeholder", "Enter a short description here...");
    $("#ingredients").attr("placeholder", "List, one per line");
    $("#ingredients").attr("wrap", "off");
    $("#instructions").attr("placeholder", "Enter instructions here chef...");
    $("#tags").attr("placeholder", "Keywords, must be split with commas...");
    $("#imageLink").attr("placeholder", "E.g https://myimage.com/lasagna.jpg");


});