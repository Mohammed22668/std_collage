/*--------------------------------------------------
All the script here will extend to all pages
---------------------------------------------------*/ 

// 1) for Add studnets Documents 


function validateAll(){
    var name = $("#name").val();
    var depart = $("#depart").val();
    var city = $("#city").val();
    var year_std = $("#year_std").val();
    var study_all = $("#study-all").val();
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
      else if (study_all == ''){
        Swal.fire('Oops !',"يجب ملئ حقل الدراسة","Error");
        return false
    }
    
      else if (year_std == ''){
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

// ######################## END #################################


// ######################## Start #################################
// 2 - for Add students status 
function validateAllstate(){
    var name = $("#name-state").val();
    var depart = $("#depart-state").val();
    var city = $("#city-state").val();
    var stage = $("#stage-state").val();
    var study = $("#study-state").val();
    var state = $("#state-state").val();
    var year = $("#year-state").val();

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
        else if (year == ''){
        Swal.fire('Oops !',"يجب ملئ حقل العام الدراسي","Error");
        return false
    }


    else {
        return true;
    }
}

$("#btn-add-state").bind("click",validateAllstate);



// ##########################################################

// for All students 

// 2 - for Add students status 
function validateAlldate(){
    var name = $("#name-all").val();
    var depart = $("#depart-all").val();
    var city = $("#city-all").val();
    var stage = $("#stage-all").val();
    var study = $("#study-all").val();
    var state = $("#state-all").val();
    var date = $("#date-all").val();
    var year = $("#year-all").val();

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
    
     else if (stage == ''){
          Swal.fire('Oops !',"يجب ملئ حقل  المرحلة","Error");
        return false
    }
   

      else if (study == ''){
          Swal.fire('Oops !',"يجب ملئ حقل  الدراسة","Error");
        return false
    }

   

       else if (state == ''){
          Swal.fire('Oops !',"يجب ملئ حقل  المباشرة","Error");
        return false
    }

     else if (date == ''){
          Swal.fire('Oops !',"يجب ملئ حقل  تاريخ المباشرة","Error");
        return false
    }

        else if (year == ''){
        Swal.fire('Oops !',"يجب ملئ حقل العام الدراسي","Error");
        return false
    }


    else {
        return true;
    }
}

$("#btn-add-all").bind("click",validateAlldate);