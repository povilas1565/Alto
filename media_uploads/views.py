# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MediaFile
from .forms import MediaUploadForm

def home(request):
    # Display public media on the home page
    public_media = MediaFile.objects.filter(is_public=True)[:12]  # Limit to 12 items
    return render(request, 'media_uploads/home.html', {'media_files': public_media})

@login_required
def dashboard(request):
    # Display user's media files
    user_media = MediaFile.objects.filter(user=request.user)
    return render(request, 'media_uploads/dashboard.html', {'media_files': user_media})

@login_required
def upload_media(request):
    if request.method == 'POST':
        form = MediaUploadForm(request.POST, request.FILES)
        if form.is_valid():
            media = form.save(commit=False)
            media.user = request.user
            media.save()
            messages.success(request, 'Your media has been uploaded successfully!')
            return redirect('media_uploads:dashboard')
    else:
        form = MediaUploadForm()
    
    return render(request, 'media_uploads/upload_media.html', {'form': form})

@login_required
def media_detail(request, pk):
    # Get the media file object
    media = get_object_or_404(MediaFile, pk=pk)
    
    # Check if user has permission to view
    if not media.is_public and media.user != request.user:
        messages.error(request, "You don't have permission to view this media.")
        return redirect('media_uploads:dashboard')
        
    return render(request, 'media_uploads/media_detail.html', {'media': media})

@login_required
def delete_media(request, pk):
    media = get_object_or_404(MediaFile, pk=pk)
    
    # Only the owner can delete the media
    if media.user != request.user:
        messages.error(request, "You don't have permission to delete this media.")
        return redirect('media_uploads:dashboard')
    
    if request.method == 'POST':
        media.file.delete()  # Delete the actual file
        media.delete()  # Delete the database record
        messages.success(request, 'Your media has been deleted.')
        return redirect('media_uploads:dashboard')
        
    return render(request, 'media_uploads/delete_media.html', {'media': media})