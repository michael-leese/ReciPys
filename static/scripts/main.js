$(document).ready(function(){

    //add recipy form
    $(".add-form > input").addClass("textarea-form");
    $(".add-form > textarea").addClass("textarea-form");
    $(".add-form > label").addClass("strong");
    $("#creator").attr("placeholder", "Your Username...");
    $("#title").attr("placeholder", "ReciPy Title...");
    $("#description").attr("placeholder", "Enter a short description here...");
    $("#ingredients").attr("placeholder", "List, one per line");
    $("#ingredients").attr("wrap", "off");
    $("#instructions").attr("placeholder", "Enter instructions here chef...");
    $("#tags").attr("placeholder", "Keywords, must be split with commas...");
    $("#imageLink").attr("placeholder", "E.g https://myimage.com/lasagna.jpg");

    //registration form
    $(".reg-form > input").addClass("textarea-form");
    $(".reg-form > label").addClass("strong");
    $("#username").attr("placeholder", "Choose a Username...");
    $("#password").attr("placeholder", "Choose a Password...");
    $("#password2").attr("placeholder", "Confirm Password...");
    $("#firstname").attr("placeholder", "Enter first name...");
    $("#lastname").attr("placeholder", "Enter last name...");
    $("#dob").attr("placeholder", "Enter dd/mm/yyyy...");
    $("#email").attr("placeholder", "Enter your email...");

    //login form
    $(".log-form > input").addClass("textarea-form");
    $(".log-form > label").addClass("strong");
    $("#username").attr("placeholder", "Enter your Username...");
    $("#password").attr("placeholder", "Enter your Password...");
});