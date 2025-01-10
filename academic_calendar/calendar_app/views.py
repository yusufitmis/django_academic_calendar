from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Calendar, Event
from .forms import UserRegistrationForm, EventForm, CalendarForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .models import Calendar as CalendarModel
from datetime import datetime, timedelta
from django.http import HttpResponse



# Ana Sayfa
def index(request):
    return render(request, 'index.html')

# Takvim Listeleme
def calendar_list(request):
    calendars = Calendar.objects.all()
    return render(request, 'calendar_list.html', {'calendars': calendars})

# Etkinlik Listeleme
def event_list(request, calendar_id):
    calendar = get_object_or_404(Calendar, id=calendar_id)

    # Get the start and end dates from the GET request
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')

    # Default start and end dates if none are provided
    if start_date_str and end_date_str:
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        except ValueError:
            start_date = datetime(2024, 9, 1)
            end_date = datetime(2025, 8, 30)
    else:
        start_date = datetime(2024, 9, 1)
        end_date = datetime(2025, 8, 30)

    # Filter events based on the start_date and end_date
    events = calendar.events.filter(
        Q(start_date__gte=start_date, start_date__lte=end_date) |
        Q(start_date__isnull=True)  # Allow events with no start date
    ).filter(
        Q(end_date__lte=end_date, end_date__gte=start_date) |
        Q(end_date__isnull=True)  # Allow events with no end date
    ).order_by('start_date')

    context = {
        'calendar': calendar,
        'events': events,
        'start_date': start_date.strftime("%Y-%m-%d"),
        'end_date': end_date.strftime("%Y-%m-%d"),
    }

    return render(request, 'event_list.html', context)

# Etkinlik Ekleme (Admin için)
@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            # Form verilerini kaydet
            event = form.save(commit=False)

            # Tarih alanlarını kontrol et
            print(f"Start Date Guz: {event.start_date}")
            print(f"End Date Guz: {event.end_date}")
            print(f"Start Date Bahar: {event.start_date_bahar}")
            print(f"End Date Bahar: {event.end_date_bahar}")

            # Kaydetme işlemi
            event.save()

            # Etkinlik kaydedildikten sonra ilgili takvime yönlendirme yap
            return redirect('event_list', calendar_id=event.calendar.id)
    else:
        form = EventForm()

    return render(request, 'create_event.html', {'form': form})

# Etkinlik Güncelleme
@login_required
def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Seçilen etkinliği al
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)  # Güncelleme için formu etkinlikle doldur
        if form.is_valid():
            form.save()
            return redirect('event_list', calendar_id=event.calendar.id)
    else:
        form = EventForm(instance=event)  # Formu etkinlik bilgileriyle önceden doldur

    return render(request, 'update_event.html', {'form': form, 'event': event})
@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    calendar_id = event.calendar.id
    event.delete()  # Etkinliği sil
    return redirect('event_list', calendar_id=calendar_id)

# Kullanıcı Kaydolma
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm


# Kullanıcı Kaydolma
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Formdan gelen verileri al
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # Şifreyi hashle
            user.save()  # Kullanıcıyı kaydet

            # Kullanıcı kaydedildikten sonra, giriş sayfasına yönlendir
            return redirect('login')  # Giriş sayfasına yönlendir
        else:
            print(form.errors)  # Form hatalarını konsola yazdır
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


# Kullanıcı Giriş Yapma
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# Kullanıcı Çıkış Yapma
def logout_view(request):
    logout(request)
    return redirect('index')



from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Calendar


def export_calendar(request, calendar_id):
    calendar = get_object_or_404(Calendar, id=calendar_id)

    # ICS dosyasını UTF-8 olarak ayarlıyoruz
    response = HttpResponse(content_type='text/calendar; charset=utf-8')
    response['Content-Disposition'] = f'attachment; filename="{calendar.name}_takvimi.ics"'

    # ICS dosyası başlangıcı
    response.write("BEGIN:VCALENDAR\n")
    response.write("VERSION:2.0\n")
    response.write("CALSCALE:GREGORIAN\n")
    response.write(f"PRODID:-//YourCompany//NONSGML v1.0//EN\n")

    # Her etkinlik için
    for event in calendar.events.all():
        response.write("BEGIN:VEVENT\n")
        response.write(f"UID:{event.id}@yourcompany.com\n")  # Benzersiz ID
        response.write(f"SUMMARY:{event.title}\n")

        # Güz dönemi tarihlerini ekleyelim (start_date ve end_date)
        if event.start_date and event.end_date:
            response.write(f"DTSTART:{event.start_date.strftime('%Y%m%dT%H%M%S')}\n")
            response.write(f"DTEND:{event.end_date.strftime('%Y%m%dT%H%M%S')}\n")
        elif event.start_date:
            response.write(f"DTSTART;VALUE=DATE:{event.start_date.strftime('%Y%m%d')}\n")
        if event.end_date:
            response.write(f"DTEND;VALUE=DATE:{event.end_date.strftime('%Y%m%d')}\n")

        # Bahar dönemi tarihlerini ekleyelim (start_date_bahar ve end_date_bahar)
        if event.start_date_bahar and event.end_date_bahar:
            response.write(f"DTSTART;VALUE=DATE:{event.start_date_bahar.strftime('%Y%m%d')}\n")
            response.write(f"DTEND;VALUE=DATE:{event.end_date_bahar.strftime('%Y%m%d')}\n")
        elif event.start_date_bahar:
            response.write(f"DTSTART;VALUE=DATE:{event.start_date_bahar.strftime('%Y%m%d')}\n")
        if event.end_date_bahar:
            response.write(f"DTEND;VALUE=DATE:{event.end_date_bahar.strftime('%Y%m%d')}\n")

        response.write("END:VEVENT\n")

    # ICS dosyası sonu
    response.write("END:VCALENDAR\n")

    return response
def export_vcs_calendar(request, calendar_id):
    # Takvimi ID'ye göre al
    calendar = get_object_or_404(Calendar, id=calendar_id)

    # VCS dosyasını oluşturacak HTTP yanıtını başlat
    response = HttpResponse(content_type='text/vcalendar')
    response['Content-Disposition'] = f'attachment; filename="{calendar.name}_takvimi.vcs"'

    # Takvim başlık bilgileri
    response.write("BEGIN:VCALENDAR\n")
    response.write("VERSION:2.0\n")
    response.write(f"SUMMARY:{calendar.name} Takvimi\n")
    response.write("PRODID:-//YourCompany//NONSGML v1.0//EN\n")
    response.write("CALSCALE:GREGORIAN\n")  # Takvim tipi

    # Her etkinlik için VCS formatında veri ekle
    for event in calendar.events.all():
        response.write("BEGIN:VEVENT\n")
        response.write(f"SUMMARY:{event.title}\n")

        # Başlangıç tarihi
        if event.start_date:
            response.write(f"DTSTART:{event.start_date.strftime('%Y%m%dT%H%M%S')}\n")
        # Bitiş tarihi
        if event.end_date:
            response.write(f"DTEND:{event.end_date.strftime('%Y%m%dT%H%M%S')}\n")

        # Bahar dönemi başlangıç tarihi
        if event.start_date_bahar:
            response.write(f"DTSTART;VALUE=DATE:{event.start_date_bahar.strftime('%Y%m%d')}\n")
        # Bahar dönemi bitiş tarihi
        if event.end_date_bahar:
            response.write(f"DTEND;VALUE=DATE:{event.end_date_bahar.strftime('%Y%m%d')}\n")

        # Etkinlik bitişi
        response.write("END:VEVENT\n")

    # Takvim bitişi
    response.write("END:VCALENDAR\n")

    return response  # Bu satır tek başına yeterlidir


@login_required
def add_calendar(request):
    if request.method == 'POST':
        form = CalendarForm(request.POST)
        if form.is_valid():
            form.save()  # Takvimi kaydet
            return redirect('calendar_list')  # Takvimler listesine yönlendir
    else:
        form = CalendarForm()

    return render(request, 'add_calendar.html', {'form': form})


@login_required
def delete_calendar(request, calendar_id):
    calendar = get_object_or_404(Calendar, id=calendar_id)

    # Takvimi sil
    calendar.delete()

    # Takvimler listesine yönlendir
    return redirect('calendar_list')



