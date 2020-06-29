const hamburger = document.querySelector(".hamburger");
const closeMenu = document.querySelector(".close-menu");
const menu = document.querySelector(".menu");
const mobileNav = document.querySelector(".navbar-mobile__nav");
const overlay = document.querySelector(".overlay");
const navbar = document.querySelector("#navbar");
const navbarLeft = document.querySelector("#navbar-left");
const navbarNav = document.querySelector("#navbar-nav");

menu.addEventListener("click", () => {
    if(mobileNav.style.opacity === "1") {
        mobileNav.style.height = "0";
        mobileNav.style.opacity = "0";
        mobileNav.style.pointerEvents = "none";
        overlay.style.display = "none";   
        closeMenu.style.display = "none"; 
        hamburger.style.display = "flex";  
    } else {
        mobileNav.style.height = "100%";
        mobileNav.style.opacity = "1";
        mobileNav.style.pointerEvents = "all"; 
        overlay.style.display = "flex";
        closeMenu.style.display = "flex";
        hamburger.style.display = "none";     
    }
});

overlay.addEventListener("click", () => {
    mobileNav.style.height = "0";
    mobileNav.style.opacity = "0";
    mobileNav.style.pointerEvents = "none";
    overlay.style.display = "none";
    closeMenu.style.display = "none"; 
    hamburger.style.display = "flex"; 
});