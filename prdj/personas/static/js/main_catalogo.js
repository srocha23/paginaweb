/*
let productos = [];

fetch("./productos.json")
    .then(response => response.json())
    .then(data => {
        productos = data;
        cargarProductos(productos);
    })
                <div id="container_categoria" class="container_categoria">
                            {% for producto in productos %}
                            <div class="producto_categoria">
                                <div class="producto_detalles">
                                <h3 class="titulo_producto">{{producto.nombre_producto}}</h3>
                                <p class="precio_producto">{{producto.precio}}</p>
                                <p class="precio_producto">{{producto.descripcion}}</p>
                                <p class="precio_producto">{{producto.descripcion}}</p>
                                <button class="btn__producto_categoria" id="{{producto.id}}" >Comprar ahora</button>
                                <button  class="btn__producto_categoria"><a href="detalle_producto/{{producto.id}}">Detalles</a></button>
                                </div>
                            
            </div>
            {% endfor %}
*/





const contenedorCategoria = document.querySelector();
const botonesCategorias = document.querySelectorAll(".btn__categoria");
const titulo_principal_categoria = document.querySelector("#titulo_principal_categoria");
let botonesAgregar = document.querySelectorAll(".btn__producto_categoria");
const numerito = document.querySelector("#numero");


function cargarProductos(productosElegidos) {

    contenedorCategoria.innerHTML = "";

    productosElegidos.forEach(producto => {

        const div = document.createElement("div");
        div.classList.add("producto");
        div.innerHTML = `
        <div class="producto_categoria">
        <div class="producto_detalles">
        <h3 class="titulo_producto">{{% producto.nombre_producto %}}</h3>
        <p class="precio_producto">{{producto.precio}}</p>
        <p class="precio_producto">{{producto.descripcion}}</p>
        <button class="btn__producto_categoria" id="{{producto.id}}" >Comprar ahora</button>
        <button  class="btn__producto_categoria"><a href="detalle_producto/{{producto.id}}">Detalles</a></button>
        </div>
    
</div>
        
    `;


        contenedorCategoria.append(div);

    })

    actualizarBotonesAgregar();

}

botonesCategorias.forEach(boton => {
    boton.addEventListener("click", (e) => {

        botonesCategorias.forEach(boton => boton.classList.remove("active"));
        e.currentTarget.classList.add("active");

        if (e.currentTarget.id != "todos") {

            const productoCategoria = productos.find(producto => producto.categoria.id === e.currentTarget.id);
            titulo_principal_categoria.innerText = productoCategoria.categoria.nombre;
            const productosBoton = productos.filter(producto => producto.categoria.id === e.currentTarget.id);
            cargarProductos(productosBoton);
        } else {

            titulo_principal_categoria.innerText = "Todos los productos";
            cargarProductos(productos);
        }

    })
});



function actualizarBotonesAgregar() {

    botonesAgregar = document.querySelectorAll(".btn__producto_categoria");

    botonesAgregar.forEach(boton => {
        boton.addEventListener("click", agregarAlCarrito);
    });
}



let productosEnCarrito;

let productosEnCarritoLS = localStorage.getItem("productos-en-carrito");
console.log(productosEnCarritoLS)
if (productosEnCarritoLS) {
    productosEnCarrito =  JSON.parse(productosEnCarritoLS);
    console.log(document.getElementById("carrito_productos"))
    let divProductos = document.getElementById("carrito_productos")
    console.log(productosEnCarrito);
    if(productosEnCarrito.length > 0) {
        let carritoVacio = document.getElementById("carrito_vacio")
        carritoVacio.hidden = true
    }
    productosEnCarrito.forEach(producto => {
        divProductos.innerHTML = divProductos.innerHTML +  `
        <img  class="carrito_producto_img" src="${producto.imagen}" alt="${producto.titulo}">
        <div class="carrito_producto-titulo">
            <small>Titulo</small>
            <h3>${producto.titulo}</h3>
        </div>
        <div class="carrito_producto_cantidad">
            <small>Cantidad</small>
            <p>${producto.cantidad}</p>
        </div>
            <div class="carrito_producto_precio">
                <small>Precio</small>
                <p>${producto.precio}</p>
            </div>
            <div class="carrito_producto_subtotal">
                <small>Subtotal</small>
                <p>${producto.precio * producto.cantidad}</p>
            </div>
            <button class="carrito-producto-eliminar" id="${producto.id}"><i class="fa-solid fa-trash"></i></button>
        `;
    });
    //actualizarNumerito();

} else {
    productosEnCarrito = [];
}





function agregarAlCarrito(e) {


    Toastify({
        text: "Producto agregado",
        duration: 3000,
        close: true,
        gravity: "top", // `top` or `bottom`
        position: "right", // `left`, `center` or `right`
        stopOnFocus: true, // Prevents dismissing of toast on hover
        style: {
            background: "linear-gradient(to right, #4b33a8, #785ce9)",
            borderRadius: "2rem",
            textTransform: "uppercase",
            fontSize: ".75rem"
        },
        offset: {
            x: '1.5rem', // horizontal axis - can be a number or a string indicating unity. eg: '2em'
            y: '1.5rem' // vertical axis - can be a number or a string indicating unity. eg: '2em'
        },
        onClick: function () { } // Callback after click
    }).showToast();

    const idboton = e.currentTarget.id;
    const productoAgregado = productos.find(producto => producto.id === idboton);


    if (productosEnCarrito.some(producto => producto.id === idboton)) {
        const index = productosEnCarrito.findIndex(producto => producto.id === idboton);
        productosEnCarrito[index].cantidad++;



    } else {
        productoAgregado.cantidad = 1;
        productosEnCarrito.push(productoAgregado);
    }

    actualizarNumerito();
    console.log(JSON.stringify(productosEnCarrito))
    localStorage.setItem("productos-en-carrito", JSON.stringify(productosEnCarrito));

}



function actualizarNumerito() {
    let nuevoNumerito = productosEnCarrito.reduce((acc, producto) => acc + producto.cantidad, 0);
    if(numerito) {
        numerito.innerText = nuevoNumerito;
    } else {
        numerito.innerText = "algo"
    }
}