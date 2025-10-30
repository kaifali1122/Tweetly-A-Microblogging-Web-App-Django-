# Import functions to render pages, handle redirects, and get data safely
from django.shortcuts import render, get_object_or_404, redirect

# Import the tweet model (your database table)
from .models import tweet

# Import the tweetForm (your form to create/edit tweets)
from .forms import tweetForm,  userRegistrationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# ---------- HOME PAGE ----------
def index(request):
    # Load and show the 'index.html' page when user visits the site root
    return render(request, 'index.html')


# ---------- SHOW ALL TWEETS ----------
def tweet_list(request):
    # Get all tweets from database, newest ones first
    tweets = tweet.objects.all().order_by('-created_at')

    # Send those tweets to the HTML page 'tweet_list.html'
    return render(request, 'tweet_list.html', {'tweets': tweets})

@login_required
# ---------- CREATE A NEW TWEET ----------
def tweet_created(request):
    # If user submits the form (via POST method)
    if request.method == 'POST':
        # Create a form with submitted data and uploaded images
        form = tweetForm(request.POST, request.FILES)

        # Check if the form data is valid
        if form.is_valid():
            # Don’t save yet (we’ll add user manually first)
            new_tweet = form.save(commit=False)

            # Set the tweet’s user as the currently logged-in user
            new_tweet.user = request.user

            # Now save the tweet into database
            new_tweet.save()

            # After saving, go back to the list of all tweets
            return redirect('tweet_list')
    else:
        # If it’s a normal page visit (GET request), show an empty form
        form = tweetForm()

    # Show the tweet form page (either empty or with errors)
    return render(request, 'tweet_form.html', {'form': form})

@login_required
# ---------- EDIT AN EXISTING TWEET ----------
def tweet_edit(request, tweet_id):
    # Try to find the tweet by ID, but only if it belongs to this user
    tweet_instance = get_object_or_404(tweet, pk=tweet_id, user=request.user)

    # If user submitted the edit form
    if request.method == 'POST':
        # Load form with the new data and existing tweet instance
        form = tweetForm(request.POST, request.FILES, instance=tweet_instance)

        # Validate the form
        if form.is_valid():
            # Don’t save yet, we’ll reattach user just in case
            tweet_instance = form.save(commit=False)

            # Make sure user info is correct
            tweet_instance.user = request.user

            # Save updated tweet
            tweet_instance.save()

            # Redirect to tweet list after edit
            return redirect('tweet_list')
    else:
        # If it’s a GET request, show form with old data pre-filled
        form = tweetForm(instance=tweet_instance)

    # Render the same tweet_form page for editing
    return render(request, 'tweet_form.html', {'form': form})

@login_required
# ---------- DELETE A TWEET ----------
def tweet_delete(request, tweet_id):
    # Get tweet by ID but only if it belongs to the logged-in user
    tweet_instance = get_object_or_404(tweet, pk=tweet_id, user=request.user)

    # If user confirms delete by submitting form (POST)
    if request.method == 'POST':
        # Delete the tweet from the database
        tweet_instance.delete()

        # Redirect to the list page after deletion
        return redirect('tweet_list')

    # Otherwise, show a confirmation page before deleting
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet_instance})



def register(request):
    if request.method == 'POST':
        form= userRegistrationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
        
    else:
        form = userRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
