from django.shortcuts import render, get_object_or_404

from .models import Meeting, Room


def detail(request, id):
    # meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def rooms_list(request):
    # room = get_object_or_404(Room, pk=id)
    return render(request, "meetings/rooms_list.html", {"rooms": Room.objects.all()})