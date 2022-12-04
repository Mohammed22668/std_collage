const body = document.querySelector('body'),
      sidebar = body.querySelector('nav'),
      toggle = body.querySelector(".toggle"),
      changeside = body.querySelector(".home"),
      openside = body.querySelector(".menu-bar"),
      modeSwitch = body.querySelector(".toggle-switch"),
      modeText = body.querySelector(".mode-text");


toggle.addEventListener("click" , () =>{
    sidebar.classList.toggle("close");
})
changeside.addEventListener("click" , () =>{
    sidebar.classList.add("close");
})
openside.addEventListener("click" , () =>{
    sidebar.classList.remove("close");
})
