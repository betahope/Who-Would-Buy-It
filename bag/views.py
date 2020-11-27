from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view to show users the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Allow users to add a quantity of the specified product to their shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
