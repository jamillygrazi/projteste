var  nome  =  "João" ;
deixe  idade  =  89 ;
deixe  soma  =  idade  +  10 ;
deixe  multi  =  idade  *  2 ;
let  sub  = multi - idade ;

if ( idade  >  60 ) {
    console . log ( "Idoso" ) ;
    alerta ( "Idoso" ) ;
} senão {
    alerta ( "Futuro Idoso" ) ;
}

for ( deixe  i = 0 ;  i < idade ;  i ++ ) {
    documento . getElementById ( 'saída' ) . innerText  +=  " "  +  i  ;
}

while ( idade > 0 ) {
    console . log ( 'Menos um ponto' ) ;
    idade -- ;
}

função  sobre ( ) {
    var  aaa  =  documento . getElementById ( 'rodapé' ) . estilo . backgroundImage = "url('/static/image/urso.jpeg')" ;
    console . registro ( aaa ) ;
}
função  fora ( ) {
    documento . getElementById ( 'rodapé' ) . estilo . backgroundImage = "url('/static/image/image.jpeg')" ;
}
function  salvarIdade ( ) {
    var  idadeVar  =  documento . getElementById ( 'idadeVar' ) . valor ;
    idade  =  idadeVar ;
    if ( idade  >  60 ) {
        console . log ( "Idoso" ) ;
        alerta ( "Idoso" ) ;
    } senão {
        alerta ( "Futuro Idoso" ) ;
    }
}

função  confirmDelete ( nome ,  id ) {
    if ( confirm ( "Você tem certeza que quer deletar " + nome + "?" ) == true ) {
        janela . open ( "delete_person/" + id , 'self' )
    }
}