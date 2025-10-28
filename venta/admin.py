from django.contrib import admin
from .models import Producto, Cliente, Venta, DetalleVenta


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "sku", "precio", "stock", "activo")
    search_fields = ("nombre", "sku")
    list_filter = ("activo",)
    ordering = ("nombre",)
    list_per_page = 25


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email")
    search_fields = ("nombre", "email")


class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1
    autocomplete_fields = ("producto",)
    readonly_fields = ("subtotal",)
    fields = ("producto", "cantidad", "precio_unitario", "subtotal")


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    date_hierarchy = "fecha"
    list_display = ("id", "cliente", "fecha", "anulada", "total_display")
    search_fields = ("cliente__nombre", "id")
    list_filter = ("anulada",)
    inlines = [DetalleVentaInline]

    @admin.display(description="Total", ordering="id")
    def total_display(self, obj):
        return f"${obj.total:,.0f}"

