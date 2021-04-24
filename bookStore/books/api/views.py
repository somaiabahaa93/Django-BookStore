from rest_framework.response import Response
from rest_framework import status 
from books.models import Book
from .serializers import BookSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated,BasePermission
from rest_framework.decorators import api_view,permission_classes
# from rest_framework.parsers import JSONParser

@api_view(["POST"])
def api_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "User has been registered successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)




# class IsViewer(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.groups.filter(name="viewers").exists()



@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def index(request):
    books=Book.objects.all()
    serializer=BookSerializer(books,many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)

@api_view(["POST"])
def create(request):
     serializer=BookSerializer(data=request.data)
     if serializer.is_valid():
         serializer.save()
         return Response(data={
         "success":True,
         "message":"book has been created suceessfully"
         },status=status.HTTP_201_CREATED)
     return Response(data={
        "success":False,
         "errors":serializer.errors 
     },status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def edit(request, id):
    book=Book.objects.get(pk=id)
    serializer=BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success":True,
            "message":"book has been updated successfuly"
        },status=status.HTTP_201_CREATED)

    return Response(data={
            "success":False,
            "errors":serializer.errors
    },status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def show(request,id):
    book=Book.objects.get(pk=id)
    serializer=BookSerializer(instance=book)
    return Response(data=serializer.data,status=status.HTTP_200_OK)   

    


@api_view(["DELETE"])
def delete(request, id):
    try: 

        book=Book.objects.get(pk=id)

        book.delete()

        return Response(data={

        "success":True,

        "message":"Book has been deleted successfully",

        },

        status=status.HTTP_200_OK,

        )

    except Book.DoesNotExist: 

        return JsonResponse({'message': 'This book does not exist'}, status=status.HTTP_404_NOT_FOUND)



