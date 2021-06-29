from rest_framework.response import Response
from rest_framework.views import APIView

class root(APIView):

  def get(self, request):
    return Response({"msg": "This is MyTodoApi"})
