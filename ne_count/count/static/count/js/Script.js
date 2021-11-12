 $(document).ready(function(){

   $.getJSON('static/count/js/engine.json', function(){
        console.log(engine[0])
   })

    var a = $("#header").height();
    var b = $(window).height();
    height = b-a;
    $("#parameters").css({"height":height+"px","overflow-y":"scroll"});

    let nar_st = {"1":{"nar_PS": 10724, "nar_engin_SNE": 17113, "nar_engin_PKR": 7840},
        "2":{"nar_PS": 8691, "nar_engin_SNE": 472, "nar_engin_PKR": 472},
        "3":{"nar_PS": 44607, "nar_engin_SNE": 1974, "nar_engin_PKR": 1974},
        "4":{"nar_PS": 60049, "nar_engin_SNE": 2250, "nar_engin_PKR": 2250},
        "5":{"nar_PS": 6373, "nar_engin_SNE": 15784, "nar_engin_PKR": 2050},
        "6":{"nar_PS": 6571, "nar_engin_SNE": 6575, "nar_engin_PKR": 2171},
        "7":{"nar_PS": 10947, "nar_engin_SNE": 4057, "nar_engin_PKR": 1004},
        "8":{"nar_PS": 13909, "nar_engin_SNE": 7353, "nar_engin_PKR": 565},
        "9":{"nar_PS": 12735, "nar_engin_SNE": 0, "nar_engin_PKR": 0},
        "10":{"nar_PS": 51559, "nar_engin_SNE": 4968, "nar_engin_PKR": 4968},
        "11":{"nar_PS": 81984, "nar_engin_SNE": 8290, "nar_engin_PKR": 8290},
        "12":{"nar_PS": 122083, "nar_engin_SNE": 2972, "nar_engin_PKR": 2972}}
    let engine_TO = {"1":{"count":0, '1':38 }, "2":{"count":0, '1':472 }, "3":{"count":1, '1':1 }, "4":{"count":0, '1':242 },
    "5":{"count":1, '1':0 }, "6":{"count":0, '1':100 }, "7":{"count":0, '1':1 }, "8":{"count":1, '1':61 },
    "9":{"count":0, '1':0 }, "10":{"count":1, '1':389 }, "11":{"count":0, '1':249 }, "12":{"count":0, '1':1 }}

    console.log(engine_TO)

    var json = $("#json").html();
    var obj = $.parseJSON(json);
    function count_hours(objec, obj_TO, obj_nar_st){
        for (i=(Object.keys(objec).length-1); i >= 0; i--){
            var hour = objec[i].fields.OT_in_day;
            var TO = objec[i].fields.TO;
            var numb_st_TO = objec[i].fields.station
            for (ind = 1; ind <= Object.keys(obj_nar_st).length; ind++){
                if (objec[i].fields.station == (ind)){
                    obj_nar_st[ind].nar_PS += hour;
                    obj_nar_st[ind].nar_engin_SNE += hour;
                    obj_nar_st[ind].nar_engin_PKR += hour;
                    $(".nar_st:eq("+i+")").html(obj_nar_st[ind].nar_PS);
                    $(".nar_eng_PPKR:eq("+i+")").html(obj_nar_st[ind].nar_engin_PKR);
                    $(".nar_eng_SNE:eq("+i+")").html(obj_nar_st[ind].nar_engin_SNE);
                    break
                }
            };
            var len = Object.keys(obj_TO[numb_st_TO]).length
            if (TO == true){
                obj_TO[numb_st_TO]["count"] += 1;
                if (obj_TO[numb_st_TO]["count"] >= 2){
                    obj_TO[numb_st_TO]["count"] = 0;
                    obj_TO[numb_st_TO][len] = 0;
                }
                obj_TO[numb_st_TO][len-1] += hour;
                $(".nar_eng_PTO:eq("+i+")").html(obj_TO[numb_st_TO][len-1]);
            } else {
                obj_TO[numb_st_TO][len-1] += hour;
                $(".nar_eng_PTO:eq("+i+")").html(obj_TO[numb_st_TO][len-1]);
            };

        };
    };
    count_hours(obj, engine_TO, nar_st); 
 });