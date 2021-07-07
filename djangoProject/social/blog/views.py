from .forms import NewPostForm
from django.shortcuts import redirect, render
from .models import Post
from django.contrib.auth.decorators import login_required 
from django.contrib import messages

@login_required(login_url = 'register')
def home(request):
    #try organizing by user in addition to date_posted
    context = {'posts': Post.objects.all().order_by('-date_posted'),
    'post_form': NewPostForm(),}
    return render(request, 'blog/home.html', context)

# Create your views here.
@login_required(login_url = 'register')
def newPost(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        form.instance.user = request.user
        if (form.is_valid()):
            form.save()
            messages.success(request, f'Posted')
    return redirect('blog-home')

@login_required(login_url='register')
def editPost(request,id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        # if user hits update, then update
        post.content = request.POST['content']
        post.save() # update post
        messages.success(request, f'Successfully updated post')
        return redirect('blog-home')
    # if user is still updating form, then show form with current content

    form = NewPostForm(instance=post) # empty form with post info
    return render(request, 'blog/update.html', {'form':form,'id':id})

@login_required(login_url='register')
def deletePost(register, id):
    #get the post using it's id and delete it
    Post.objects.get(id=id).delete()
    #Bring us back to blog-home
    return redirect("blog-home")


