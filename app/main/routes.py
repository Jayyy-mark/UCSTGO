from flask import Blueprint, render_template, request, jsonify
from app.models import Announcement, Event, StudentResult
# ... existing imports ...
from flask import abort  # import abort for 404 handling

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Home page"""
    announcements = Announcement.query.filter_by(is_active=True).order_by(Announcement.date_posted.desc()).limit(
        3).all()
    return render_template('index.html', announcements=announcements)

@main_bp.route('/gallery-page')
def gallery_page():
    """Full Campus Gallery Page"""
    return render_template('campus_gallery.html')

@main_bp.route('/about')
def about():
    """About Us / History / Organization Page"""
    return render_template('about.html')

# ADD THIS ROUTE
@main_bp.route('/academic')
def academic():
    """Academic Page"""
    return render_template('academic.html')


# ADD THIS ROUTE
@main_bp.route('/admission')
def admission():
    """Admission Page"""
    return render_template('admission.html')


# ... existing imports ...

# Mock Database of Announcements (For demonstration)
news_data = [
    {
        "id": 1,
        "title": "First Year Orientation Schedule 2024",
        "date": "Oct 12, 2024",
        "category": "Academic",
        "summary": "The orientation program for the new academic year begins next week.",
        "image": "https://picsum.photos/id/101/1920/1080",
        "content": "<p>The University of Computer Studies, Taungoo is pleased to announce the orientation schedule for the First Year B.C.Sc and B.C.Tech students for the 2024-2025 academic year.</p><p class='mt-4'>The program includes registration, campus tour, and a welcome session with the Rector. All new students are required to attend.</p>"
    },
    {
        "id": 2,
        "title": "UCSTGO Tech Fest 2024 Winners",
        "date": "Nov 05, 2024",
        "category": "Event",
        "summary": "Celebrating the winners of our annual innovation competition.",
        "image": "https://picsum.photos/id/180/1920/1080",
        "content": "<p>We are proud to announce the winners of the 2024 Tech Fest. The competition was fierce, with over 50 projects submitted. The judges were impressed by the quality and innovation displayed.</p><p class='mt-4'>1st Place: Team Alpha (AI Chatbot)<br>2nd Place: Team Beta (Campus Map)</p>"
    },
    {
        "id": 3,
        "title": "Library Digital Archive Upgrade",
        "date": "Nov 20, 2024",
        "category": "Notice",
        "summary": "New features added to the digital library portal.",
        "image": "https://picsum.photos/id/225/1920/1080",
        "content": "<p>The digital library has undergone a major upgrade. Users can now access over 10,000 new journals and research papers. The search functionality has also been improved for better accessibility.</p>"
    }
]


@main_bp.route('/library')
def library():
    """Library Page"""
    return render_template('library.html')


@main_bp.route('/activities')
def activities():
    """Main News and Activities Page"""
    # Pass the news data to the template
    return render_template('activities.html', news_list=news_data)


@main_bp.route('/news/<int:news_id>')
def news_detail(news_id):
    """Specific News/Announcement Detail Page"""
    # Find the specific news item (In real app, use: NewsItem.query.get_or_404(news_id))
    news_item = next((item for item in news_data if item["id"] == news_id), None)

    if not news_item:
        return "News not found", 404

    return render_template('news_detail.html', news=news_item)


# ... existing imports ...

from flask import render_template


# ... existing imports ...

@main_bp.route('/departments/<string:dept_code>')
def department_detail(dept_code):
    """Generic Department Page - shows Vision and Mission"""

    # Database of Department Information
    departments_db = {
        "cs": {
            "name": "Department of Computer Science",
            "vision": "To develop human resources who can support society by applying Computer science and technology that is capable of life-long learning and powerful problem-solving skills.",
            "mission": "To encourage the emergence of students with strong ability in self-motivation, critical thinking and problem solving to succeed in the professional field</br>To provide the required resources for research and learning courses<br>To develop ethically and technically innovative students who meet the industrial needs",
            "vision_mm": "ကွန်ပျူတာသိပ္ပံနည်းပညာရပ်များကိုအသုံးချ၍ လူမှုအဖွဲ့အစည်းကို အကျိုးပြုနိုင်ပြီး စဉ်ဆက်မပြတ် လေ့လာနိုင်စွမ်း ရှိသော၊ နည်းပညာဆိုင်ရာပြဿနာများကို ကျွမ်းကျင်စွာ ကိုင်တွယ်ဖြေရှင်းနိုင်စွမ်းရှိသော လူ့စွမ်းအား အရင်း အမြစ်များ မွေးထုတ်ပေးရန်။ ",
            "mission_mm": "အသက်မွေးဝမ်းကြောင်းနယ်ပယ်တွင်အောင်မြင်ရန် လိုအပ်သောပညာရပ်များကို မိမိကိုယ်တိုင် တက်ကြွစွာ ရှာဖွေနိုင်စွမ်းရှိသော၊ ကျိုးကြောင်းဆီလျော်စွာ စဉ်းစားဆုံးဖြတ်နိုင်စွမ်းရှိသော၊ ကြုံတွေ့ရသည့် ပြဿနာများ ကို ကျွမ်းကျင်စွာ ဖြေရှင်းနိုင်စွမ်းရှိသော ကျောင်းသား၊ ကျောင်းသူများ ပေါ်ထွန်းလာစေရေးအတွက် တွန်းအားပေးရန်။သုတေသနနှင့် ဘာသာရပ်များ လေ့လာသင်ယူရာတွင် လိုအပ်သောအရင်းအမြစ်များကို ဖြည့်ဆည်း ပေးနိုင်ရန်။နည်းပညာဆိုင်ရာကျင့်ဝတ်နှင့်အညီ တီထွင်ဖန်တီးနိုင်စွမ်းရှိသော၊ ပြင်ပလုပ်ငန်းလုပ်ငန်းခွင်၏ လိုအပ်ချက် များ နှင့်ကိုက်ညီသော ကျောင်းသား၊ ကျောင်းသူများ မွေးထုတ်ပေးရန်။",
        },
        "is": {
            "name": "Department of Information Systems",
            "vision": "To become a premier hub for Information Systems education and research, recognized for excellence in teaching and innovative applications of IT solutions.",
            "mission": "To educate and train information technology professionals capable of designing, implementing, and managing secure information systems that drive organizational success and social benefit."
        },
        "se": {
            "name": "Department of Software Engineering",
            "vision": "To be the global leader in software engineering education, advancing the state of the art in software design and development methodologies.",
            "mission": "To develop world-class software engineers capable of building high-quality, reliable, and scalable software systems for a rapidly changing technological landscape."
        },
        "nce": {
            "name": "Department of Network & Communication Engineering",
            "vision": "To empower students with cutting-edge knowledge in networking, communications, and embedded systems, preparing them to lead in the era of ubiquitous connectivity.",
            "mission": "To produce graduates who can design robust network architectures and implement efficient communication protocols to bridge the digital divide."
        },
        "csec": {
            "name": "Department of Cyber Security",
            "vision": "To create a secure cyberspace by educating the next generation of cybersecurity experts capable of protecting critical infrastructure and information assets.",
            "mission": "To advance the science and practice of cyber defense through rigorous training, innovative research, and strategic partnerships with industry leaders."
        },
        "ai": {
            "name": "Department of Artificial Intelligence",
            "vision": "To be at the forefront of the AI revolution, integrating intelligent systems into every aspect of human life to solve complex global challenges.",
            "mission": "To research and develop intelligent algorithms, machine learning models, and neural networks that mimic cognitive functions and augment human capabilities."
        },
        "es": {
            "name": "Department of Embedded Systems",
            "vision": "To drive innovation in the Internet of Things (IoT) and smart systems, creating a connected world where devices interact seamlessly and intelligently.",
            "mission": "To design and develop energy-efficient, high-performance embedded computing solutions for automotive, industrial, and consumer electronics sectors."
        },
        "rnd": {
            "name": "Department of Research & Development",
            "vision": "To be the engine of innovation for UCSTGO, facilitating cutting-edge research that addresses real-world problems through technology.",
            "mission": "To foster a research culture that encourages discovery, collaboration, and the translation of theoretical knowledge into practical applications."
        },
        "math": {
            "name": "Department of Mathematics & Physics",
            "vision": "To provide a strong foundation in mathematical sciences and physics, essential for advancing engineering and technology fields.",
            "mission": "To equip students with analytical skills and scientific reasoning capabilities necessary to support the advancement of computer science and engineering disciplines."
        }
    }

    # Get department data or 404
    dept_data = departments_db.get(dept_code)

    if not dept_data:
        return "Department Not Found", 404

    return render_template('departments.html', department=dept_data)

@main_bp.route('/research')
def research():
    """Research and Publications Page"""
    # You can fetch a list of publications here later
    # publications = Publication.query.order_by(Publication.date.desc()).all()
    # return render_template('research.html', publications=publications)

    # For now, we just render the template with static content
    return render_template('research.html')




# ... existing routes ...

@main_bp.route('/activity/<int:activity_id>')
def activity_detail(activity_id):
    """Show Gallery for a specific Activity"""

    # Mock Data for Demonstration (Replace this with Database query in production)
    activities_data = {
        1: {
            "title": "2025 Inter-University Race",
            "date": "March 15, 2025",
            "description": "Our athletes competed against 10 universities, bringing home gold medals in the 100m and relay events. A day of sportsmanship and excellence.",
            "images": [
                "https://picsum.photos/seed/race1/800/600",
                "https://picsum.photos/seed/race2/800/600",
                "https://picsum.photos/seed/race3/800/600",
                "https://picsum.photos/seed/race4/800/600",
                "https://picsum.photos/seed/race5/800/600",
                "https://picsum.photos/seed/race6/800/600"
            ]
        },
        2: {
            "title": "Tech Innovation Week 2024",
            "date": "Nov 20, 2024",
            "description": "A week-long showcase of student projects, hackathons, and robotics demonstrations. Students from various departments presented cutting-edge solutions to real-world problems.",
            "images": [
                "https://picsum.photos/seed/tech1/800/600",
                "https://picsum.photos/seed/tech2/800/600",
                "https://picsum.photos/seed/tech3/800/600",
                "https://picsum.photos/seed/tech4/800/600"
            ]
        },
        3: {
            "title": "Annual Cultural Festival",
            "date": "Oct 10, 2024",
            "description": "Celebrating diversity through music, dance, and traditional food fairs. Students showcased their heritage through colorful costumes and performances.",
            "images": [
                "https://picsum.photos/seed/cult1/800/600",
                "https://picsum.photos/seed/cult2/800/600",
                "https://picsum.photos/seed/cult3/800/600",
                "https://picsum.photos/seed/cult4/800/600",
                "https://picsum.photos/seed/cult5/800/600"
            ]
        }
    }

    activity = activities_data.get(activity_id)

    if activity is None:
        abort(404)  # Return 404 if ID doesn't exist

    return render_template('activity_gallery.html', activity=activity)

@main_bp.route('/api/check-result', methods=['POST'])
def check_result():
    """API Endpoint for Alumni Checker"""
    roll_no = request.form.get('rollNo')
    student = StudentResult.query.filter_by(roll_no=roll_no).first()

    if student:
        return jsonify({'status': 'success', 'data': student.to_dict()})
    else:
        return jsonify({'status': 'error', 'message': 'Record not found'}), 404

