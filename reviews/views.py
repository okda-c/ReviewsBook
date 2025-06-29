from django.shortcuts import render, redirect

from reviews.forms import ReviewForm


def reviews(request):
    if request.method == "GET":
        form = ReviewForm()
        return render(request, 'reviews.html', {'form': form})
    elif request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            name = data.get("name")
            email = data.get("email")
            review = data.get('review')
            rating = data.get('rating')
            return redirect("reviews")
        else:
            form = ReviewForm()
            return render(request, 'reviews.html', {'form': form})
