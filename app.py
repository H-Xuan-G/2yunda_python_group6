from flask import Flask, render_template, request, redirect, url_for
from data.event_info import EVENT_NAME, EVENT_DESCRIPTION, EVENT_NOTICE
from data.options import GROUP_OPTIONS, ACTIVITY_OPTIONS
from data.page_text import WELCOME_TEXT, FORM_HINT, RESULT_TITLE
from data.registrations import DEFAULT_REGISTRATIONS

app = Flask(__name__)

# 内存中存储报名数据（Vercel 无状态，每次重启清空，仅演示用）
registrations = list(DEFAULT_REGISTRATIONS)


@app.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        event_name=EVENT_NAME,
        event_description=EVENT_DESCRIPTION,
        event_notice=EVENT_NOTICE,
        group_options=GROUP_OPTIONS,
        activity_options=ACTIVITY_OPTIONS,
        welcome_text=WELCOME_TEXT,
        form_hint=FORM_HINT,
    )


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    group = request.form.get("group", "").strip()
    activity = request.form.get("activity", "").strip()
    reason = request.form.get("reason", "").strip()

    if name and group and activity:
        registrations.append({
            "name": name,
            "group": group,
            "activity": activity,
            "reason": reason,
        })

    return redirect(url_for("result"))


@app.route("/result")
def result():
    total = len(registrations)
    # 统计各活动方向人数
    activity_count = {}
    for r in registrations:
        act = r.get("activity", "未知")
        activity_count[act] = activity_count.get(act, 0) + 1

    recent = registrations[-10:][::-1]

    return render_template(
        "result.html",
        result_title=RESULT_TITLE,
        total=total,
        activity_count=activity_count,
        recent=recent,
    )


if __name__ == "__main__":
    app.run(debug=True)
