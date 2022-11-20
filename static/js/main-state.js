/*--------------------------------------------------
All the script here will extend to all pages
---------------------------------------------------*/ 

// 1) 


function validateAll(){
    var name = $("#name").val();
    var depart = $("#depart").val();
    var city = $("#city").val();
    var stage = $("#stage").val();
    var study = $("#study").val();
    var state = $("#state").val();
    var year = $("#year").val();

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

      else if (state == ''){
          Swal.fire('Oops !',"يجب ملئ حقل  الحالة","Error");
        return false
    }

      else if (study == ''){
          Swal.fire('Oops !',"يجب ملئ حقل  الدراسة","Error");
        return false
    }

    else if (stage == ''){
          Swal.fire('Oops !',"يجب ملئ حقل  المرحلة","Error");
        return false
    }

    else {
        return true;
    }
}

$("#btn-add-state").bind("click",validateAll);


