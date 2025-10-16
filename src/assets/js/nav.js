//
//    Toggle Mobile Navigation
//
const navbarMenu = document.querySelector("#navigation #navbar-menu");
const hamburgerMenu = document.querySelector("#navigation .hamburger-menu");
const serviceMenu = document.querySelector("#navigation .dropdown");
const about = document.querySelector('#About\\ Us')
const contact = document.querySelector('#Contact')
const projects = document.querySelector('#Our\\ Work')
const reviews = document.querySelector('#Reviews')
const blog = document.querySelector('#Blog')
const gallery = document.querySelector('#Gallery')      

const screenWidth = window.screen.width;

//
//    Handle Scroll Events for Logo Display
//
function handleScroll() {
    const scrollY = window.scrollY;
    const body = document.body;
    const isDarkMode = body.classList.contains('dark-mode');
    const isLargeScreen = window.innerWidth >= 770; // Same breakpoint as mobile menu

    // When scrollY is 0, in light mode, and on larger screens, show dark logo
    if (scrollY === 0 && !isDarkMode && isLargeScreen) {
        body.classList.add('show-dark-logo');
    } else {
        body.classList.remove('show-dark-logo');
    }

    // Handle scroll class for navigation background
    if (scrollY > 0) {
        body.classList.add('scroll');
    } else {
        body.classList.remove('scroll');
    }
}

// Add scroll event listener
window.addEventListener('scroll', handleScroll);

// Call on page load to handle initial state
handleScroll();



hamburgerMenu.addEventListener('click', function () {
    const isNavOpen = navbarMenu.classList.contains("open");
    if (!isNavOpen) {
        hamburgerMenu.setAttribute("aria-expanded", true);
        hamburgerMenu.classList.add("clicked");
        navbarMenu.classList.add("open");
    } else {
        hamburgerMenu.setAttribute("aria-expanded", false);
        hamburgerMenu.classList.remove("clicked");
        navbarMenu.classList.remove("open");
        serviceMenu.setAttribute("aria-expanded", false);
        serviceMenu.classList.remove("open");
        if (screenWidth < 770) {
            if (about) about.style.setProperty('display', 'block', 'important')
            if (contact) contact.style.setProperty('display', 'block', 'important')
        }
    }
});

serviceMenu.addEventListener('click', function () {
    const isServiceOpen = serviceMenu.classList.contains("open");
    if (!isServiceOpen) {
        serviceMenu.setAttribute("aria-expanded", true);
        serviceMenu.classList.add("open");
        if (screenWidth < 770) {
            if (about) about.style.setProperty('display', 'none', 'important')
            if (contact) contact.style.setProperty('display', 'none', 'important')
            if (projects) projects.style.setProperty('display', 'none', 'important')
            if (reviews) reviews.style.setProperty('display', 'none', 'important')
            if (blog) blog.style.setProperty('display', 'none', 'important')
            if (gallery) gallery.style.setProperty('display', 'none', 'important')
        }


    } else {
        serviceMenu.setAttribute("aria-expanded", false);
        serviceMenu.classList.remove("open");
        if (screenWidth < 770) {
            if (about) about.style.setProperty('display', 'block', 'important')
            if (contact) contact.style.setProperty('display', 'block', 'important')
            if (projects) projects.style.setProperty('display', 'block', 'important')
            if (reviews) reviews.style.setProperty('display', 'block', 'important')
            if (blog) blog.style.setProperty('display', 'block', 'important')
            if (gallery) gallery.style.setProperty('display', 'block', 'important')
        }
    }
});