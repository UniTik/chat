from django.shortcuts import render,redirect
from .models import Room,Message
from django.http import JsonResponse

def createRoom(request):
    if request.method == "POST":
        
        roomName = request.POST['room-name']
        roomUser = request.POST['room-user']
        #-----------building admin pannel------------#
        if roomName == "admin" and roomUser == "admin":
            return redirect("/adminPanel")
        #--------------------------------------------#
        if Room.objects.filter(name = roomName).exists():
            return redirect("/room/"+roomName+"?username="+roomUser)
        else:
            Room.objects.create(name =  roomName).save()
            return redirect("/room/"+roomName+"?username="+roomUser)            


    return render(request,"home.html")

def room(request,pk):
    user = request.GET.get("username")
    room = Room.objects.get(name=pk)
    messages =  Message.objects.filter(room =  room)
    return render(request,'chatRoom.html',{"messages": messages,"room":room,"user":user})

def submit(request,pk):
    user = request.GET.get('username')
    room = Room.objects.get(name=pk)
    if request.method == "POST":
        text = request.POST['message']
        if text is not "":
            Message.objects.create(text = text, room = room, user = user).save()
                    
    # return redirect("/room/"+pk+"?username="+user)
def GetMessage(request,pk):
    room = Room.objects.get(name=pk)
    messages = Message.objects.filter(room = room)
    return JsonResponse({
        "messages":list(messages.values()) # i do not know why it should have .values
    })

def adminPanel(request):
    message = []
    message.append("1.type rooms to see all existing rooms")
    message.append("2.after that you can remove them by typing remove + [room's name]")

    if request.method == "POST":
        admin_message = request.POST["message"]
        ####### posibelity of recived messages:

        roomsName = []
        room = Room.objects.all()
        for i in room:
            roomsName.append(i.name)

        for room in roomsName:
            if admin_message == "remove " + str(room):
                Room.objects.get(name = room).delete()
                message = []
                message.append(str(room) + " has been deleted")
                return render(request,'adminPanel.html',{"messages":message})
        if admin_message == "rooms":
            message = roomsName
        elif admin_message == "help":
            message = []
            message.append("1.type rooms to see all existing rooms")
            message.append("2.after that you can remove them by typing remove + [room's name]")
        elif admin_message == "exit":
            return redirect(createRoom)
        else:
            message = []
            message.append("type help if you need any help")

    return render(request,'adminPanel.html',{"messages":message})

def adminPanel_search(request):
    message = request.POST['message']
    message = message.replace("remove ",'')
    rooms = Room.objects.filter(name__contains = message)
    return JsonResponse({
        "messages":list(rooms.values())

    })