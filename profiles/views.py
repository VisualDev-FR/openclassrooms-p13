from django.shortcuts import render, redirect
import logging

from profiles.models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat
# libero pulvinar eget. Fusc faucibus, urna quis auctor pharetra, massa dolor cursus
# neque, quis dictum lacus d
def index(request):
    """
    Display a list of all available profiles
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet neque quis,
# pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt, dolor id
# facilisis fringilla, eros leo tristique lacus, it. Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    """
    Display details of a given Profile

    Args:
    --------
    username: str
        the username of the Profile to display
    """
    try:
        profile = Profile.objects.get(user__username=username)
        context = {"profile": profile}
        return render(request, "profiles/profile.html", context)

    except Exception as e:
        logging.error(f"error while accessing {username} : {str(e)}")
        return redirect("profiles:index")