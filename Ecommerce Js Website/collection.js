var productcontainer = document.getElementById('product');
var search=document.getElementById('search');
var products=productcontainer.querySelectorAll("div")

search.addEventListener("keyup", function(event){

    var entered=event.target.value.toUpperCase();

    for ( let count=0;count<products.length;count=count+1 ) 
    {
        var productname=products[count].querySelector("p").textContent
        if (productname.toUpperCase().indexOf(entered)<0)
        {
            products[count].style.display="none";

        }   
        else{
            products[count].style.display="block";
        } 
    }


})