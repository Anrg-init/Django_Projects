from django.shortcuts import render

class MclassMid:
    def __init__(self,get_response):
        self.get_response = get_response
        print("middleware initizialled .....")

    def __call__(self,request):
        print("before middlewar calling")
        response = self.get_response(request)
        print("after middleware calling")
        return response
    



#funciton based view and this is generarlly universal like apply on all tempalates and pages

# def my_midu(get_response):
#     print("one time initiallizing......")

#     def my_func(request):
#         print("before view running")
#         response = get_response(request)
#         print("after view run")   
#         return response
#     return my_func


#Another Example baby:

# def my_midu(get_response):
#     print("middlefinder inistiziallingsgldkj..........")

#     def my_func(request):
#         print("before view")
#         response = render(request, 'core/uc.html')
#         print("after view")
#         return response
#     return my_func







✅ Django Middleware Hooks (All Important Ones)

Middleware mainly has 3 hooks:

🔹 1. __init__(self, get_response)

👉 Runs once when server starts
👉 Used for setup / initialization

🔹 2. __call__(self, request)

👉 Runs every request
👉 Main middleware execution

Flow:

Before view → code before get_response

After view → code after get_response

🔹 3. Optional Hook Methods (Process Hooks)

These run only if you define them:

✅ process_view(self, request, view_func, view_args, view_kwargs)

👉 Runs just before view function

✅ process_exception(self, request, exception)

👉 Runs when view throws error

✅ process_template_response(self, request, response)

👉 Runs when response contains render() template
👉 Lets you modify template response