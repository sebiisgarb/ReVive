from django.shortcuts import render
from .forms import ImageUploadForm
from .utils import ImageRestorer
import os

# Încarcă modelul pre-antrenat
MODEL_PATH = "models/ColorizeArtistic_gen.pth"
restorer = ImageRestorer(model_path=MODEL_PATH)

def restore_image_view(request):
    restored_image_path = None

    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Salvează imaginea încărcată
            uploaded_image = form.cleaned_data['image']
            input_path = f"media/{uploaded_image.name}"
            output_path = f"media/restored_{uploaded_image.name}"

            with open(input_path, 'wb') as f:
                for chunk in uploaded_image.chunks():
                    f.write(chunk)

            # Restaurează imaginea
            restored_image_path = restorer.restore_image(input_path, output_path)

    else:
        form = ImageUploadForm()

    return render(request, 'restoration/index.html', {
        'form': form,
        'restored_image': restored_image_path
    })
