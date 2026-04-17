# Warrior-app
# Lightning Warriors Hockey – Enhanced MVP

A mobile-friendly starter web app for a 500-person veteran hockey organization with:

- Member registration and login
- Role-based access (`admin`, `manager`, `member`)
- Team creation and team membership
- Event creation and RSVP / registration
- Attendance tracking by event
- Bulk attendance actions for captains/managers
- Attendance export to CSV
- Team chat and event chat
- Member directory for admins/managers
- SQLite database for simple local deployment

## Tech stack

- Python
- Flask
- SQLite
- Jinja templates + responsive CSS

## Quick start

```bash
cd lightning-warriors-hockey
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app app.py seed
flask --app app.py run
```

Open `http://127.0.0.1:5000`

## Seed accounts

- Admin: `admin@lightningwarriorshockey.org`
- Password: `ChangeMe123!`

- Manager: `manager@example.com`
- Password: `Password123!`

- Member: `member@example.com`
- Password: `Password123!`

## New in this version

1. Responsive mobile-first navigation and layouts
2. Touch-friendly forms and buttons
3. Attendance statuses: present, late, absent, excused, unmarked
4. RSVP and attendance tracked separately
5. Bulk mark all “Going” players as present
6. CSV export for attendance reports
7. Dashboard attendance visibility for users

## Suggested next upgrades

1. Email / SMS notifications for event reminders
2. Approval workflow for new members
3. Waivers, dues, and payment tracking
4. Real-time chat with WebSockets
5. Captains / assistant captains permissions
6. Push notifications in a mobile app shell
7. Image uploads for player profiles and teams
8. Schedule import from Google Calendar / rink feeds
9. Tournament roster lock / waitlist
10. Live scorekeeping or bench availability

## Notes

This is a working enhanced MVP meant to help you validate the workflow quickly. For production, add:

- stronger auth controls
- password reset
- audit logging
- backups
- rate limiting
- moderation controls
- object storage for files/images
- stronger form validation
- environment-based secrets
- cloud hosting
