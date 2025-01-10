# Akademik Takvim Uygulaması / Academic Calendar Application

Bu proje, Django framework'ü kullanılarak geliştirilmiş bir akademik takvim yönetim uygulamasıdır.  
This project is an academic calendar management application developed using the Django framework.

## Özellikler / Features

- Kullanıcı kayıt ve giriş sistemi  
  - User registration and login system  
- Akademik takvim oluşturma ve yönetme  
  - Create and manage academic calendars  
- Etkinlik ekleme, güncelleme, silme  
  - Add, update, and delete events  
- Tarihe göre etkinlik filtreleme  
  - Filter events by date  
- Takvimi **ICS** ve **VCS** formatlarında dışa aktarma  
  - Export the calendar in **ICS** and **VCS** formats  
- Kullanıcı dostu arayüz  
  - User-friendly interface  

## Gereksinimler / Requirements

- Python 3.8+  
- Django 4.x  
- SQLite (veya başka bir veritabanı)  
- Bootstrap (CDN ile)
- 
## Kullanım / Usage

### Admin / Admin   
Yönetici girişi yaptıktan sonra:  
- **Takvim** ekleyebilir, güncelleyebilir ve silebilirsiniz.  
- **Etkinlikler** ekleyebilir, düzenleyebilir ve kaldırabilirsiniz.
After logging in as admin:  
- You can add, update, and delete **calendars**.  
- You can add, edit, and remove **events**.

### Ziyaretçi / Visitor   
Ziyaretçi giriş yapmadan:  
- **Takvim** listeleyebilir, seçilen takvimde gezinebilir.  
- **Etkinlikler**'i listeleyebilir. Etkinlikleri belirli bir aya veya güne göre filtreleyebilir. 

### ICS ve VCS Dışa Aktarma / ICS and VCS Export  
Bir takvimin tüm etkinliklerini:  
- **ICS** veya **VCS** formatında indirebilirsiniz.  

Export all events of a calendar in:  
- **ICS** or **VCS** format.  

## Ekran Görüntüleri / Screenshots  

### Ana Sayfa / Home Page  
![Ana Sayfa](https://github.com/yusufitmis/django_academic_calendar/blob/main/images/visitor_home.PNG)  
 

### Takvim Listesi / Calendar List  
![Ziyaretçi Takvim Listesi / Visitor Calendar List](https://github.com/yusufitmis/django_academic_calendar/blob/main/images/visitor_calendars.PNG)  
![Admin Takvim Listesi / Admin Calendar List](https://github.com/yusufitmis/django_academic_calendar/blob/main/images/admin_calendars.PNG)  

### Etkinlik Yönetimi / Event Management  
![Add Event](https://github.com/yusufitmis/django_academic_calendar/blob/main/images/admin_add_events.PNG)  
![Update Event](https://github.com/yusufitmis/django_academic_calendar/blob/main/images/admin_update_events.PNG)  

### Giriş Yap ve Kayıt Ol / Login and Register  
![Add Event](https://github.com/yusufitmis/django_academic_calendar/blob/main/images/login.PNG)  
![Update Event](https://github.com/yusufitmis/django_academic_calendar/blob/main/images/register.PNG) 

## Kurulum / Installation

1. Depoyu klonlayın:  
   Clone the repository:  
   ```bash
   git clone https://github.com/username/academic-calendar.git
   cd academic-calendar
   
## Katkı Sağlama / Contribution  

Katkıda bulunmak isterseniz:  
1. Bu repoyu fork edin.  
2. Yeni bir branch oluşturun: `git checkout -b feature-name`.  
3. Değişikliklerinizi yapın ve commit edin: `git commit -m "Feature açıklaması"`.  
4. Branch'i push edin: `git push origin feature-name`.  
5. Bir pull request oluşturun.  

If you'd like to contribute:  
1. Fork this repository.  
2. Create a new branch: `git checkout -b feature-name`.  
3. Make your changes and commit them: `git commit -m "Feature description"`.  
4. Push your branch: `git push origin feature-name`.  
5. Create a pull request.  
