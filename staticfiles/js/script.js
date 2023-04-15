function confirmDelete(nome, id){
    if(confirm("Você tem certeza que quer deletar "+nome+"?")==true){
        window.open("delete_person/"+id,'self')
    }
}

function confirmDeleteDoc(nome, id){
    if(confirm("Você tem certeza que quer deletar "+nome+"?")==true){
        window.open("delete_doc/"+id,'self')
    }
}