/*
-------------------------------------------------

---   TOGGLE SIDEBAR | Vanilla Javascript

-------------------------------------------------
*/

let sidebar = document.querySelector(".sidebar");
  let logoHeader = document.querySelector("#header");
  let closeBtn = document.querySelector("#btn");
  let searchBtn = document.querySelector(".bx-search");

  closeBtn.addEventListener("click", ()=>{
    sidebar.classList.toggle("open");
    logoHeader.classList.toggle("open");
    menuBtnChange();//calling the function(optional)
  });

  searchBtn.addEventListener("click", ()=>{ // Sidebar open when you click on the search iocn
    sidebar.classList.toggle("open");
    logoHeader.classList.toggle("open");
    menuBtnChange(); //calling the function(optional)
  });

  // following are the code to change sidebar button(optional)
  function menuBtnChange() {
   if(sidebar.classList.contains("open")){
     closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");//replacing the iocns class
   }else {
     closeBtn.classList.replace("bx-menu-alt-right","bx-menu");//replacing the iocns class
   }
  }

/*
-------------------------------------------------

---   HEADER MENU SHRINK | Requires jQuery

-------------------------------------------------
*/

$(function(){
 var shrinkHeader = 21;
  $(window).scroll(function() {
    var scroll = getCurrentScroll();
      if ( scroll >= shrinkHeader ) {
           $('#header').addClass('shrink');
        }
        else {
            $('#header').removeClass('shrink');
        }
  });
function getCurrentScroll() {
    return window.pageYOffset || document.documentElement.scrollTop;
    }
});
/*---------------------------------------------------------------------------*/
var data = [
  { y: '2014', a: 50, b: 90},
  { y: '2015', a: 65,  b: 75},
  { y: '2016', a: 50,  b: 50},
  { y: '2017', a: 75,  b: 60},
  { y: '2018', a: 80,  b: 65},
  { y: '2019', a: 90,  b: 70},
  { y: '2020', a: 100, b: 75},
  { y: '2021', a: 115, b: 75},
  { y: '2022', a: 120, b: 85},
  { y: '2023', a: 145, b: 85},
  { y: '2024', a: 160, b: 95}
],
config = {
  data: data,
  xkey: 'y',
  ykeys: ['a', 'b'],
  labels: ['Total Income', 'Total Outcome'],
  fillOpacity: 0.6,
  hideHover: 'auto',
  behaveLikeLine: true,
  resize: true,
  pointFillColors:['#ffffff'],
  pointStrokeColors: ['black'],
  lineColors:['gray','red']
};
config.element = 'area-chart';
Morris.Area(config);
config.element = 'line-chart';
Morris.Line(config);
config.element = 'bar-chart';
Morris.Bar(config);
config.element = 'stacked';
config.stacked = true;
Morris.Bar(config);
Morris.Donut({
element: 'pie-chart',
data: [
{label: "رجال", value: 30},
{label: "نساء", value: 15},

]
});
/************************************************************ */
