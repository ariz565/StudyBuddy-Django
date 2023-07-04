from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import HttpResponse, redirect, render

from .forms import *
from .models import *


# View to handle the login page
def loginPage(request):
    # Page identifier
    # NOTE: We have used same template for login and register page
    page = "login"

    # If user is already logged in, redirect to home page
    if request.user.is_authenticated:
        return redirect("home")

    # If request method is POST
    if request.method == "POST":
        # Get the email and password from the request
        email = request.POST.get("email").lower()
        password = request.POST.get("password")

        try:
            # Try to get the user object using email
            user = User.objects.get(email=email)
        except:
            # If user does not exist, show error message
            messages.error(request, "Email does not exist!")

        # Authenticate the user using email and password
        user = authenticate(request, email=email, password=password)

        # If user is not None, login the user
        if user is not None:
            login(request, user)

            # Redirect to home page
            return redirect("home")

        # Else show error message
        else:
            messages.error(request, "Email OR password is incorrect!")

    # Context dictionary
    context = {"page": page}

    # Render the login page template
    return render(request, "base/login_register.html", context)


# View to handle the logout functionality
def logoutUser(request):
    # Use the django logout method
    logout(request)

    # Redirect to home page
    return redirect("home")


# View to handle the register page
def registerPage(request):
    # If user is already logged in, redirect to home page
    if request.user.is_authenticated:
        return redirect("home")

    # For to handle the user registration data
    form = MyUserCreationForm()

    # If request method is POST
    if request.method == "POST":
        # Update the form with the request POST data
        form = MyUserCreationForm(request.POST)

        # If form is valid
        if form.is_valid():
            # Temporary save the user object
            user = form.save(commit=False)

            # Convert the username to lowercase
            user.username = user.username.lower()

            # Save the user object to database
            user.save()

            # Login the user
            login(request, user)

            # Redirect to home page
            return redirect("home")

        # Else show error message
        else:
            messages.error(request, "An error occurred during registration")

    # Context dictionary
    return render(request, "base/login_register.html", {"form": form})


# View to handle the home page
def home(request):
    # Get the search query
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    # Get all the rooms
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)
    )

    # Get the room topics
    topics = Topic.objects.all()[:5]

    # Get the room count
    room_count = rooms.count()

    # Get the messages
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    # Context dictionary
    context = {
        "rooms": rooms,
        "topics": topics,
        "topics_count": len(topics),
        "room_count": room_count,
        "room_messages": room_messages,
    }

    # Render the home page template
    return render(request, "base/home.html", context)


# View to handle the room page
def room(request, pk):
    # Get the room with query primary key
    room = Room.objects.get(id=pk)

    # Get all the messages of the room
    room_messages = room.message_set.all()

    # Get all the participants of the room
    participants = room.participants.all()

    # If request method is POST
    if request.method == "POST":
        # Create a new message object
        message = Message.objects.create(
            user=request.user, room=room, body=request.POST.get("body")
        )

        # Add the user to the participants list
        room.participants.add(request.user)

        # Redirect to the same room
        return redirect("room", pk=room.id)

    # Context dictionary
    context = {
        "room": room,
        "room_messages": room_messages,
        "participants": participants,
    }

    # Render the room page template
    return render(request, "base/room.html", context)


# View to handle the user profile page
def userProfile(request, pk):
    # Get the user with query primary key
    user = User.objects.get(id=pk)

    # Get all the rooms of the user
    rooms = user.room_set.all()

    # Get all the messages of the user
    room_messages = user.message_set.all()

    # Get all the topics
    topics = Topic.objects.all()

    # Context dictionary
    context = {
        "user": user,
        "rooms": rooms,
        "room_messages": room_messages,
        "topics": topics,
    }

    # Render the user profile page template
    return render(request, "base/profile.html", context)


# Decorator to check if the user is authenticated
@login_required(login_url="login")
def createRoom(request):
    # Form to handle the room data
    form = RoomForm()

    # Get all the topics
    topics = Topic.objects.all()

    # If request method is POST
    if request.method == "POST":
        # Get the topic name from the request
        topic_name = request.POST.get("topic")

        # Get or create the topic object
        topic, created = Topic.objects.get_or_create(name=topic_name)

        # Create a new room object and save it to database
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get("name"),
            description=request.POST.get("description"),
        )

        # Redirect to home page
        return redirect("/")

    # Context dictionary
    context = {"form": form, "topics": topics}

    # Render the create room page template
    return render(request, "base/room_form.html", context)


# Decorator to check if the user is authenticated
@login_required(login_url="login")
def updateRoom(request, pk):
    # Get the room with query primary key
    room = Room.objects.get(id=pk)

    # Get the room details from database
    form = RoomForm(instance=room)

    # Get all the topics
    topics = Topic.objects.all()

    # If the user is not the host of the room
    if request.user != room.host:
        # User not allowed to access this page
        return HttpResponse("You are not allowed here!")

    # If request method is POST
    if request.method == "POST":
        # Get the topic name from the request
        topic_name = request.POST.get("topic")

        # Get or create the topic object
        topic, created = Topic.objects.get_or_create(name=topic_name)

        # Update the form with the request POST data
        form = RoomForm(request.POST, instance=room)

        # Update the room object
        room.topic = topic
        room.name = request.POST.get("name")
        room.description = request.POST.get("description")

        # Save the room object
        room.save()

        # If the form is valid
        return redirect("/")

    # Context dictionary
    context = {"form": form, "topics": topics, "room": room}

    # Render the update room page template
    return render(request, "base/room_form.html", context)


# Decorator to check if the user is authenticated
@login_required(login_url="login")
def deleteRoom(request, pk):
    # Get the room with query primary key
    room = Room.objects.get(id=pk)

    # If the user is not the host of the room
    if request.user != room.host:
        # User not allowed to access this page
        return HttpResponse("You are not allowed here!")

    # If request method is POST
    if request.method == "POST":
        # Delete the room
        room.delete()

        # Redirect to home page
        return redirect("home")

    # Context dictionary
    context = {"obj": room}

    # Render the delete room page template
    return render(request, "base/delete.html", context)


# Decorator to check if the user is authenticated
@login_required(login_url="login")
def deleteMessage(request, pk):
    # Get the message with query primary key
    message = Message.objects.get(id=pk)

    # If the user is not the author of the message
    if request.user != message.user:
        # User not allowed to access this page
        return HttpResponse("You are not allowed here!")

    # If request method is POST
    if request.method == "POST":
        # Delete the message
        message.delete()

        # Redirect to home page
        return redirect("home")

    # Context dictionary
    context = {"obj": message}

    # Render the delete message page template
    return render(request, "base/delete.html", context)


# Decorator to check if the user is authenticated
@login_required(login_url="login")
def updateUser(request):
    # Get the user details from database
    user = request.user

    # Initialize the user form with the user details
    form = UserForm(instance=user)

    # If request method is POST
    if request.method == "POST":
        # Update the form with the request POST data
        form = UserForm(request.POST, request.FILES, instance=user)

        # If the form is valid
        if form.is_valid():
            # Save the user object
            form.save()

            # Redirect to user profile page
            return redirect("user-profile", pk=user.id)

    # Render the update user page template
    return render(request, "base/update-user.html", {"form": form})


# Decorator to check if the user is authenticated
def topicsPage(request):
    # Get the search query
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    # Get all the topics
    topics = Topic.objects.filter(name__icontains=q)

    # Context dictionary
    context = {"topics": topics, "topics_count": len(topics)}

    # Render the topics page template
    return render(request, "base/topics.html", context)


# Decorator to check if the user is authenticated
def activityPage(request):
    # Get all the messages
    room_messages = Message.objects.all()

    # Context dictionary
    context = {"room_messages": room_messages}

    # Render the activity page template
    return render(request, "base/activity.html", context)
