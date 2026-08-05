import os
import sys
import threading
import traceback
from flask import Flask, jsonify

# -----------------------------
# Flask server برای Render
# -----------------------------

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "message": "Saeed AI Bot is running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


# -----------------------------
# اجرای موتور اصلی ربات
# -----------------------------

def start_bot():

    try:
        print("🚀 Starting Saeed AI Bot...")

        # تلاش برای اجرای فایل اصلی
        try:
            import saeed_agent

            print("✅ saeed_agent loaded")

            if hasattr(saeed_agent, "main"):
                saeed_agent.main()

            elif hasattr(saeed_agent, "run"):
                saeed_agent.run()

            else:
                print(
                    "⚠️ saeed_agent imported but no main/run function found"
                )

        except Exception as e:
            print("❌ saeed_agent error:")
            traceback.print_exc()


        # اجرای سیستم کنترل اگر موجود بود
        try:
            import saeed_control_center

            print("✅ Control center loaded")

            if hasattr(saeed_control_center, "main"):
                saeed_control_center.main()

        except Exception:
            print("⚠️ Control center not started")


    except Exception:
        print("❌ Bot startup failed")
        traceback.print_exc()



# -----------------------------
# اجرای برنامه
# -----------------------------

if __name__ == "__main__":

    # اجرای ربات در Thread جدا
    bot_thread = threading.Thread(
        target=start_bot,
        daemon=True
    )

    bot_thread.start()


    # پورت Render
    port = int(
        os.environ.get(
            "PORT",
            10000
        )
    )

    print(
        f"🌐 Web server running on port {port}"
    )


    app.run(
        host="0.0.0.0",
        port=port
    )
