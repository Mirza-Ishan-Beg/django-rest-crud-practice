from rest_framework.views import APIView
from rest_framework.response import Response

class CalculatorView(APIView):
    def post(self, request):
        op = request.data.get("operation")
        a = request.data.get("a")
        b = request.data.get("b")
        result = None

        try:
            a, b = float(a), float(b)

            if op == 'add':
                result = a + b
            elif op == 'subtract':
                result = a - b
            elif op == 'Multiply':
                result = a * b
            elif op == 'Divide':
                result = a / b
            else:
                result = "Invalid Operation"
        except Exception as e:
            result = f"Error: {e}"

        return Response({"result": result})
            
