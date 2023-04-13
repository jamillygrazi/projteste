var name = "João";
let age = 89;
let soma = age + 10;
let multi = age * 2;
let sub =multi-age;

if(age > 60){
    console.log("Idoso");
    alert("Idoso");
}else{
    alert("Futuro Idoso");
}

for(let i=0; i<age; i++){
    document.getElementById('output').innerText += " " + i ;
}

while(age>0){
    console.log('Menos um ponto');
    age--;
}

function saveAge(){
    var ageVar = document.getElementById('ageVar').value;
    age = ageVar;
    if(age > 60){
        console.log("Idoso");
        alert("Idoso");
    }else{
        alert("Futuro Idoso");
    }
}

function confirmDelete(nome, id){
    if(confirm("Você tem certeza que quer deletar "+nome+"?")==true){
        window.open("delete_person/"+id,'self')
    }
}