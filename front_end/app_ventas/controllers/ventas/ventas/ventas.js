steal(
    MODELS+'producto.js',
    CONTROLLERS+'ventas/top',
    CONTROLLERS+'ventas/buscar_productos'

).then(
    './css/style.css',
    './views/init.ejs',

function($) {



$.Controller("Ventana.Ventas",
/** @Static */ {
    pluginName : "ventana_ventas"

}, /** @Prototype */ {
    
    init : function() {
        this.element.html($.View(CONTROLLERS + 'ventas/ventas/views/init.ejs'));

        $("#top_ventas").ventas_top();
        $("#area_busqueda").ventas_buscar_productos();
    }
});




});


