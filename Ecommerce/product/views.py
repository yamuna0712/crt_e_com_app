from django.shortcuts import render,redirect, get_object_or_404
from .models import ProductModel,Cart

def add_product(request):
    if request.method == 'POST':
        p_name = request.POST.get('p_name')
        p_type = request.POST.get('p_type')
        p_price = request.POST.get('p_price')
        p_quantity = request.POST.get('p_quantity')

        ProductModel.objects.create(
            p_name=p_name,
            p_type=p_type,
            p_price=p_price,
            p_quantity=p_quantity
        )

        return render(request, "success.html", {
            "message": "Product added successfully"
        })

    return render(request, "product_form.html")

def view_all_products(request):
    data = ProductModel.objects.all().values()
    return render(request, "product_list.html", {
        "product_data":list(data)
    })

def del_by_id(request,id):
    if request.method == 'POST':
        data = ProductModel.objects.filter(id=id)
        data.delete()
        return render(request, "success.html",
                      {"message": "Product deleted successfully"})
    return render(request, "product_list.html")

def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = ProductModel.objects.filter(id=product_id).first()

        if product is None:
            return render(request, "error.html", {
                "message": "Product not found"
            })

        Cart.objects.create(
            product_id=product.id,
            p_price=product.p_price
        )

        cart_items = Cart.objects.all()

        return render(request, 'cart_page.html', {
            "message": "Product added to cart successfully",
            "cart_items": cart_items
        })

    return render(request, "product_list.html")


def delete_cart_item(request, id):
    if request.method == 'POST':
        Cart.objects.filter(cart_id=id).delete()
    cart_items = Cart.objects.all()
    return render(request, 'cart_page.html', {
        "cart_items": cart_items
    })


def upd_by_id(request, id):
    product = get_object_or_404(ProductModel, id=id)

    if request.method == "POST":
        product.p_name = request.POST.get("p_name")
        product.p_type = request.POST.get("p_type")
        product.p_price = request.POST.get("p_price")
        product.p_quantity = request.POST.get("p_quantity")
        product.save()

        return redirect('/product/view_all_products/')

    return render(request, "update_product.html", {"product": product})