{% extends 'base.html' %}
{% block content %}
<section class="page-header">
    <p class="kicker">Event</p>
    <h1>{{ event.title }}</h1>
    <div class="chips">
        <span class="chip">{{ event.team.name }}</span>
        <span class="chip">{{ event.event_type|capitalize }}</span>
        <span class="chip">{{ event.start_time.strftime('%b %d, %Y %I:%M %p') }}</span>
    </div>
    <p>{{ event.location }}</p>
    <p>{{ event.notes }}</p>
</section>

<section class="card" style="margin-bottom: 20px;">
    <div class="row-between">
        <div>
            <h2 class="section-title">Attendance Snapshot</h2>
            <p class="muted">Track who said they were coming and who actually showed up.</p>
        </div>
        {% if current_user.role in ['admin', 'manager'] %}
        <div class="bulk-actions">
            <form method="post" action="{{ url_for('bulk_attendance', event_id=event.id) }}">
                <input type="hidden" name="action" value="present_all_going" />
                <button class="button small" type="submit">Mark Going as Present</button>
            </form>
            <form method="post" action="{{ url_for('bulk_attendance', event_id=event.id) }}">
                <input type="hidden" name="action" value="reset_all" />
                <button class="button small secondary" type="submit">Reset Attendance</button>
            </form>
            <a class="button small secondary" href="{{ url_for('export_attendance', event_id=event.id) }}">Export CSV</a>
        </div>
        {% endif %}
    </div>
    <div class="summary-grid">
        <div class="summary-tile"><span class="muted">Present</span><strong>{{ summary.present }}</strong></div>
        <div class="summary-tile"><span class="muted">Late</span><strong>{{ summary.late }}</strong></div>
        <div class="summary-tile"><span class="muted">Absent</span><strong>{{ summary.absent }}</strong></div>
        <div class="summary-tile"><span class="muted">Excused</span><strong>{{ summary.excused }}</strong></div>
        <div class="summary-tile"><span class="muted">Unmarked</span><strong>{{ summary.unmarked }}</strong></div>
    </div>
</section>

<section class="grid two">
    <div class="card">
        <h2 class="section-title">Your RSVP</h2>
        <form method="post" action="{{ url_for('register_for_event', event_id=event.id) }}" class="inline-form">
            <select name="status">
                <option value="registered" {% if my_registration and my_registration.status == 'registered' %}selected{% endif %}>Going</option>
                <option value="maybe" {% if my_registration and my_registration.status == 'maybe' %}selected{% endif %}>Maybe</option>
                <option value="not_attending" {% if my_registration and my_registration.status == 'not_attending' %}selected{% endif %}>Not attending</option>
            </select>
            <button class="button" type="submit">Save RSVP</button>
        </form>
        <p class="footer-note muted">Admins and managers can mark actual attendance below after the event starts.</p>

        <h2 class="section-title" style="margin-top: 20px;">Roster + Attendance</h2>
        <div class="mobile-table">
            <table>
                <thead>
                    <tr>
                        <th>Member</th>
                        <th>RSVP</th>
                        <th>Attendance</th>
                        {% if current_user.role in ['admin', 'manager'] %}<th>Update</th>{% endif %}
                    </tr>
                </thead>
                <tbody>
                    {% for row in roster_rows %}
                    <tr>
                        <td>
                            <strong>{{ row.member.full_name }}</strong><br>
                            <span class="muted">{{ row.member.branch or 'Veteran' }}</span>
                        </td>
                        <td>{{ rsvp_labels.get(row.registration.status, 'No response') if row.registration else 'No response' }}</td>
                        <td>
                            {{ attendance_labels.get(row.attendance.status, 'Unmarked') if row.attendance else 'Unmarked' }}
                            {% if row.attendance and row.attendance.minutes_late %}
                                <div class="muted">{{ row.attendance.minutes_late }} min late</div>
                            {% endif %}
                            {% if row.attendance and row.attendance.notes %}
                                <div class="muted">{{ row.attendance.notes }}</div>
                            {% endif %}
                        </td>
                        {% if current_user.role in ['admin', 'manager'] %}
                        <td>
                            <form method="post" action="{{ url_for('update_attendance', event_id=event.id) }}" class="attendance-form">
                                <input type="hidden" name="user_id" value="{{ row.member.id }}" />
                                <select name="attendance_status">
                                    {% for key, label in attendance_labels.items() %}
                                    <option value="{{ key }}" {% if row.attendance and row.attendance.status == key %}selected{% elif not row.attendance and key == 'unmarked' %}selected{% endif %}>{{ label }}</option>
                                    {% endfor %}
                                </select>
                                <input type="number" name="minutes_late" min="0" placeholder="Minutes late" value="{{ row.attendance.minutes_late if row.attendance and row.attendance.minutes_late is not none else '' }}" />
                                <input type="text" name="notes" placeholder="Note" value="{{ row.attendance.notes if row.attendance and row.attendance.notes else '' }}" />
                                <button class="button small" type="submit">Save</button>
                            </form>
                        </td>
                        {% endif %}
                    </tr>
                    {% else %}
                    <tr>
                        <td colspan="4" class="muted">No team members found for this event.</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>

    <div class="card chat-card">
        <h2 class="section-title">Event Chat</h2>
        <div class="chat-box">
            {% for message in messages %}
                <div class="message">
                    <div><strong>{{ message.author.full_name }}</strong> <span class="muted">{{ message.created_at.strftime('%b %d %I:%M %p') }}</span></div>
                    <div>{{ message.content }}</div>
                </div>
            {% else %}
                <p class="muted">No event messages yet.</p>
            {% endfor %}
        </div>
        <form method="post" action="{{ url_for('event_chat', event_id=event.id) }}" class="chat-form">
            <textarea name="content" rows="3" placeholder="Message everyone about this event" required></textarea>
            <button class="button" type="submit">Send</button>
        </form>
    </div>
</section>
{% endblock %}
