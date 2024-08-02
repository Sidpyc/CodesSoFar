var overlay = document.querySelector('.overlay');
var box= document.querySelector('.box');
var addbtn = document.getElementById('addbtn');

addbtn.addEventListener('click',function(){
    overlay.style.display = 'block';
    box.style.display = 'block';
});

var cancelbtn = document.querySelector('#cancel-book');

cancelbtn.addEventListener('click',function(event){
    overlay.style.display = 'none';
    box.style.display = 'none';
    event.preventDefault();

});

var container = document.querySelector('.container');
var addbook= document.getElementById('add-book');
var title = document.getElementById('title');
var description = document.getElementById('description');
var author = document.getElementById('author');

addbook.addEventListener('click',function(event){

    var div= document.createElement('div');
    div.setAttribute("class", "book-container");
    div.innerHTML = `<h2>${title.value}</h2>
    <h5>${author.value}</h5>
    <p>${description.value}</p>
    <button onclick='deletebtn(event)'>Delete</Button>`
    container.append(div)
    event.preventDefault();
    overlay.style.display = 'none';
    box.style.display = 'none';

})

function deletebtn(event){

var remover= event.target.closest('div')
remover.remove();


}