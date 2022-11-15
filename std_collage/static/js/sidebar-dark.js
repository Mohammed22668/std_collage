const body = document.querySelector('body'),
      sidebar = body.querySelector('nav'),
      move = body.querySelector(".menu-bar"),
      searchBtn = body.querySelector(".search-box"),
      modeSwitch = body.querySelector(".toggle-switch"),
      modeText = body.querySelector(".mode-text");
      let toggle = document.querySelector("#btn");

      toggle.addEventListener("click" , () =>{
    sidebar.classList.toggle("close");
})
move.addEventListener("click" , () =>{
    sidebar.classList.remove("close");
})
searchBtn.addEventListener("click" , () =>{
    sidebar.classList.remove("close");
})

modeSwitch.addEventListener("click" , () =>{
    body.classList.toggle("dark");
    
    if(body.classList.contains("dark")){
        modeText.innerText = "Light mode";
    }else{
        modeText.innerText = "Dark mode";
        
    }
});


