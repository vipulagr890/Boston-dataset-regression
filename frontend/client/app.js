function onclickestimatedprice() {

    console.log("Estimate price button clicked");
    var CHAS = document.getElementById("CHAS").value;
    var bhk = document.getElementById("BHK").value;
    var PT = document.getElementById("PTRATIO").value;
    
      
    var url = "http://127.0.0.1:5000/house_price" //Use this if you are NOT using nginx which is first 7 tutorials
        //var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

    $.post(url, {
        CHAS: CHAS,
        RM: bhk,
        PTRATIO: PT
    },function(data, status) {
        console.log(data.estimated_price);
        document.getElementById("uiEstimatedPrice").innerHTML =  data.estimated_price + "$";
        console.log(status);
    });
}

