function validar(){

	var Proveedor,idproducto,nombreProducto,Seleccione Categoria,Categoria;

	Proveedor= document.getElementById("Proveedor").value;
	idproducto= document.getElementById("Idproducto").value;
	nombreProducto=document.getElementById("nombreProducto").value;
	

	if(Proveedor ==="" || idproducto==="" || nombreProducto===""){
		alert("TODOS LOS CAMPOS SON OBLIGATORIOS");
		return false;
	}

	else if(Proveedor.length>30 || nombreProducto.length>40){
		alert("El nombre es muy largo");
		return false;
	}

	else if(idProducto.length>0){
		alert("Debe elegir numero mayor a 0");
		return false;
		}

	else if(isNaN(idProduto)){
		alert("Datos ingresados no son numeros");
		return false;
	}	

	
	

	

}