from django.http import HttpResponse
from django.shortcuts import render
from moviepy.editor import ColorClip, CompositeVideoClip, TextClip

from .models import UserRequest


def generate_video(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        time = 3
        width = 100
        height = 100
        # Сохраняем запрос в базу данных
        UserRequest.objects.create(text=text)
        # Генерация видео
        background = ColorClip((width, height), color=(0, 0, 255))
        txt_clip = TextClip(text, fontsize=20, font='Arial', color='white')
        txt_clip = txt_clip.set_position(lambda t: (width+((width*2+txt_clip.w)/(time-1))-((width*2+txt_clip.w)/(time-1))*t,
                                                    height/2))
        final_clip = CompositeVideoClip([background, txt_clip],
                                        size=(width, height)
                                        ).set_duration(time)
        video_path = 'media/video.mp4'
        final_clip.write_videofile(video_path, fps=30)
        # Скачивание видео
        with open(video_path, 'rb') as f:
            response = HttpResponse(f, content_type='video/mp4')
            response['Content-Disposition'] = 'attachment; filename="video.mp4"'
            return response
    return render(request, 'running_text/index.html')


def get_list_text(request):
    user_requests = UserRequest.objects.all()
    return render(request, 'running_text/list_text.html', {'user_requests': user_requests})
