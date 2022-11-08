/*--------------------------------------------------
All the script here will extend to all pages
---------------------------------------------------*/ 

// 1) 


function validateAll(){
    var name = $("#name").val();
    var depart = $("#depart").val();
    var city = $("#city").val();
    var year = $("#year").val();
    var to = $("#to").val();
    var Dnumber = $("#Dnumber").val();
    var Ddate = $("#Ddate").val();

    if (name == ''){
          Swal.fire('Oops !',"يجب ملئ حقل الاسم.","Error");
        return false
    }

     else if (depart == ''){
          Swal.fire('Oops !',"يجب ملئ حقل القسم","Error");
        return false
    }

    else if (city == ''){
          Swal.fire('Oops !',"يجب ملئ حقل المحافظة","Error");
        return false
    }
    
      else if (year == ''){
        Swal.fire('Oops !',"يجب ملئ حقل سنة التخرج","Error");
        return false
    }
    
      else if (to == ''){
          Swal.fire('Oops !',"يجب ملئ حقل (الى)","Error");
        return false
    }
       else if (Dnumber == ''){
          Swal.fire('Oops !',"يجب ملئ حقل رقم الوثيقة","Error");
        return false
    }
       else if (Ddate == ''){
          Swal.fire('Oops !',"يجب ملئ حقل تاريخ الوثيقة","Error");
        return false
    }

    else {
        return true;
    }
}

$("#btn-add").bind("click",validateAll);


// 2 ) Script name accept only letters
// $(document).ready(function(){
//   jQuery('input[name="name]').keyup(function(){
//     var letter = jQuery(this).val();
//     var allow = letter.replace(/[^a-zAZ _]/g, '');
//     jQuery(this).val(allow);
//   });
//   $("input").on("keypress", function(e){
//     if (e.which===32 && ! this.value.length)
//     e.preventDefault();
//   });

// });



// // 9 ) first name + last name 
// $(document).ready(function(){
//   $("#name").keyup(function(){
//     var name = $("#name").val();
//     if (name.split(' ').length == 3){
//        Swal.fire("Opsss ! ","Put only first and last name.","info");
//        $("#name").val("");
//         return false;
//     }

//   });
// });